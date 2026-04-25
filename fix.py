import os

# super loop through all folders
# for each item:
# if ffprobe -i <item> contains "timescale not set"
# run  ffmpeg -i <input> -map 0:v -map 0:a -c copy <some output>
