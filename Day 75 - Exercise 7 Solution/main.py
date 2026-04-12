import os

files = os.listdir("clutterFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterFoldere/{file}.txt", f"clutterFolder/{i}.png")
        i = i+1