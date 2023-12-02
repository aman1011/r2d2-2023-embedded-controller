#!/bin/sh

sudo rfcomm bind rfcomm0 98:D3:32:30:DC:46
#ls -l
#qjoypad PS3_Rev2 &
#qjoypad /home/pi/Desktop/new_ps3_layout.lyt
sleep 1
#cd /home/pi/Desktop/r2d2/Desktop/2023R2
python3 RPi4MasterScriptDirect.py

sleep 10000
