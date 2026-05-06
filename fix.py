import os, subprocess

# super loop through all folders
# for each item:
# if ffprobe -i <item> contains "timescale not set"
# run  ffmpeg -i <input> -map 0:v -map 0:a -c copy <some output>
file_name = ""

def probe_files(path):
    # Need to build full path
    files = os.listdir(path)
    for file in files:
        new_path = os.path.join(path, file)
        if not os.path.isdir(new_path):
            output = subprocess.run(['/usr/bin/ffprobe','-i',new_path], capture_output=True)
            print(new_path)
            if "timescale not set" in str(output.stdout):
                print("\n\n\n",new_path)
                exit(0)
        else:
            probe_files(new_path)

# probe_files("/nfs/media/Music/Kansas")
output = subprocess.run(['/usr/bin/ffprobe','-i','/nfs/media/Music/Kansas/Point of Know Return/1-05 Closet Chronicles.m4a'], capture_output=True)
print(output)