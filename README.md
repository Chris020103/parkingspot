# Parkingspot

The parkingspot module is made for people that want to check if the parking spot is available. By using a pressed sensor, lightbulb and thingspeak you can now see if the parking spot is free or not. By this way you can see if your parking spot is available or not and when the car leaves so you can place your car at that position

# Demo



https://github.com/Chris020103/parkingspot/assets/74050913/9b825b66-3720-487a-9d5b-99334ae68679

This demo showcasing the working of the raspberry pi with the view in thingspeak. I shortend the video a bit because of the 15 seconds delay that is on thingspeak.

# Proces

Problem Statement:
For owners of a parking garage or the people that wants to park there can in the parking garage it is now visible where the open parking places are en which one already in use. For the owners it is now possible to see if there is still a parking spot free for new clients. And if not than dont open the port for some new clients.

Implementation:
Add thingspeak for showing the green light when the parking is free
Show a light for the free place and when the place is used dont show the light.

Challenges and Solutions:
My biggest challenge for this project was that i had a sensor named "Ultrasonische sensor - RCW-0001" And I tried to get it working with the breadboard. But I didn't had the matching resisstors so I had to make a decission to get back to the button sensor to get it done. 

Here is an image of the sensor in the breadboard:
![IMG_3143](https://github.com/Chris020103/parkingspot/assets/74050913/45f6ae72-127e-4518-b254-c4443b1f4239)

# Requirements
Raspberry Pi 3 model A+ (or above)
Lightbulb 
Button
Raspbian 11 (or above)
Python 3.9.2 (or above)

# Installation

To get the parking spot working you have to do the following things

1. Setup Raspberry pi
  * Install Raspbian 11 on your Raspberry Pi.
  * Ensure Python 3.9.2 is installed.
2. Add the needed components to the raspberry PI
  * Connect the button to GPIO17 on the raspberry
  * Connect the light on GPIO4 on the raspberry
  This all by using a breadboard for the grounded function
3. Add a script on the desktop of the raspberry named script.py
  * In terminal do the following: 'cd Desktop', 'python3 script.py'

# Usage
Place the included script file in the script.py on the raspberry pi and run the script in the terminal.

From there try it out with pressing the button and hold it down like there is a car standing on the button

Go to thingspeak and see the result:
<img width="462" alt="image" src="https://github.com/Chris020103/parkingspot/assets/74050913/199ec01a-e7cd-47a8-96dc-11cedecde066">

# Conclusion

In this project I learned about scripting with Phyton. And how to work with the breadboard because I didn't know before. Afterall the parking spot manager is a easy working method to have an overview about your parking spot. So you dont have to go all the way to your parking spot but you can see it now on your own device.

Monitoring:

You can see the parking spot in thingspeak by https://thingspeak.com/channels/2380073/private_show

# References

https://www.raspberrypi.com/software/
https://www.youtube.com/
https://chat.openai.com/


