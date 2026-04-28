# Importing the win32com as wincl
import win32com.client as wincl

# This is the different accent, 0, 1
speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
spk.Rate = 4
vcs = spk.GetVoices()
SVSFlag = 0
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
l = ["Sohan", "Athul", "Sowrabha", "Aditya"]

for val in l:
    spk.Speak(f"Shoutout to {val}", SVSFlag)


