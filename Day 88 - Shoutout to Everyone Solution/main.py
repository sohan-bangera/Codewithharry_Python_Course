import win32com.client as wincl

spk = wincl.Dispatch("SAPI.SpVoice")

while (userInput := input("Enter the word: ")) != "No":
    spk.Speak(userInput)