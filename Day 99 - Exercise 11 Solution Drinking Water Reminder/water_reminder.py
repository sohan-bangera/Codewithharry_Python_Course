import os
import time 

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

while True:
  # Speak reminder
  os.system("powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Hey Harry drink water')\"")
  
  # Show popup
  os.system('powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show(\'Hey Harry, Drink water\', \'Water Reminder\')"')
  
  time.sleep(REPEAT_INTERVAL)