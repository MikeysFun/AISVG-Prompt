import requests
import dotenv
import os
import shutil
from time import sleep

dotenv.load_dotenv()

uberduck_auth = (os.getenv("API_KEY"), os.getenv("API_SECRET"))

scriptfile = input("Insert the file containing the script: ")
characters = []
lines = []

# DO NOT EDIT BEYOND THIS LINE

path = f'./{scriptfile.replace(".txt","")}'

if not os.path.exists(path):
    os.makedirs(path)
else:
    shutil.rmtree(path)
    os.makedirs(path)

with open(scriptfile, 'r') as script:
    text = script.read().replace(": "," - ").replace("""

""","~").split("~")
    for line in text:
        t2 = line.split(" - ")
        characters.append(t2[0])
        lines.append(t2[1])

char2 = []

# SpongeBob = spongebob
# Mr. Krabs = mr-krabs
# Plankton = plankton
# Patrick = patrick
# Sandy = sandy-cheeks
# Squidward = squidward
# Narrator = the-french-narrator
# Karen = karen-the-computer

for charact in characters:
    if charact == "SpongeBob":
        char2.append("spongebob")
        
    if charact == "Mr. Krabs":
        char2.append("mr-krabs")
        
    if charact == "Plankton":
        char2.append("plankton")
        
    if charact == "Patrick":
        char2.append("patrick")
        
    if charact == "Sandy":
        char2.append("sandy-cheeks")
        
    if charact == "Squidward":
        char2.append("squidward")

    if charact == "Narrator":
        char2.append("the-french-narrator")

    if charact == "Karen":
        char2.append("karen-the-computer")

for i in range(len(lines)):
        audio = requests.post(
            "https://api.uberduck.ai/speak-synchronous",
            json=dict(speech=lines[i], voice=char2[i]),
            auth=uberduck_auth,
        ).content
        with open(f'{scriptfile.replace(".txt","")}/{i}_audio_{char2[i]}.wav', "wb") as f:
            f.write(audio)
with open(f'concat.txt', "w") as file:
    for i in range(len(lines)):
        file.write(f"file '{scriptfile.replace('.txt','')}/{i}_audio_{char2[i]}.wav'\n")
        file.write("file 'silence.wav'\n")

os.system(f"ffmpeg -f concat -safe 0 -i concat.txt -c:a libmp3lame -b:a 192k -ar 44100 -ac 2 -af aresample=44100 {scriptfile.replace('.txt','')}.mp3")