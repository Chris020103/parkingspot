import RPi.GPIO as GPIO
import time
import requests

# ThingSpeak API settings
writeAPIkey = "SBJO41ICX74LP075"  # Replace with your channel write API key
url = "https://api.thingspeak.com/update"

# GPIO setup
GPIO.setmode(GPIO.BCM)
lightPin = 4
buttonPin = 17

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to track button state and timing
buttonPressedTime = None
buttonState = 1  # Initial state to send to ThingSpeak as 1 (no car parked)
lastPeriodicUpdateTime = time.time()  # Initialize with the current time for periodic updates

def updateThingSpeak(value, immediate=False):
    global lastPeriodicUpdateTime
    queries = {"api_key": writeAPIkey, "field1": value}
    r = requests.get(url, params=queries)
    if r.status_code == requests.codes.ok:
        if value == 0:
            print("Data Sent: A car is parked here")
        elif value == 1:
            print("Data Sent: No car is parked here")
        if immediate:
            lastPeriodicUpdateTime = time.time()  # Reset the timer for periodic updates after an immediate update
    else:
        print("Error Code: " + str(r.status_code))

# Set initial state on ThingSpeak when script starts
updateThingSpeak(1, immediate=True)  # Now sending 1 at start indicating no car is parked

while True:
    current_time = time.time()
    if GPIO.input(buttonPin) == GPIO.LOW:  # Button pressed (car parked)
        if buttonPressedTime is None:
            buttonPressedTime = current_time
            if buttonState != 0:
                updateThingSpeak(0, immediate=True)  # Immediately send 0 when a car is detected
                buttonState = 0
                GPIO.output(lightPin, GPIO.LOW)  # Turn off light when car is parked
    else:  # Button released (no car parked)
        if buttonState != 1 or current_time - lastPeriodicUpdateTime >= 30:
            updateThingSpeak(1)  # Send 1 every 30 seconds to indicate no car is parked
            buttonState = 1
            GPIO.output(lightPin, GPIO.HIGH)  # Turn on light when no car is parked
        buttonPressedTime = None

    # Ensure an update every 30 seconds regardless of button state
    if current_time - lastPeriodicUpdateTime >= 30:
        updateThingSpeak(buttonState)

    time.sleep(0.1)  # Small delay to prevent CPU overuse
