import sounddevice as sd
import soundfile as sf
import random
import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#switch and PIR motion sensor to activate sound
SWITCH_PIN = 17
PIR_PIN = 23

GPIO.setmode(GPIO.BCM) #channel numbers on the Broadcom SOC
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#use your own sound files here- many types excepted (wave, mp3, etc)
def playSlappy():
    slappymp3 = [] #declare list
    slappymp3 = ["didyahmissme-slappy_JackBlack.mp3",\
"dummy-slappy_JackBlack.mp3",\
"ginv-me-goosebumps-slappy_JackBlack.mp3",\
"hello-slappy_JackBlack.mp3",\
"laugh_long-slappy_JackBlack.mp3",\
"laugh_short-slappy_JackBlack.mp3",\
"pulling_strings-slappy_JackBlack.mp3",\
"slappy_unhappy-slappy_JackBlack.mp3",\
"whats_the_plan-slappy_JackBlack.mp3"]
    listLength = len(slappymp3)
    indexToPlay = random.randint(0,listLength-1)
    fileToPlay = slappymp3[indexToPlay]
    print("playing: ",fileToPlay)
    data, fs = sf.read(fileToPlay)
    sd.play(data, fs)
    sd.wait()

#infinate loop, when button pushed or PIR sensor activated, random sound file played

while (True):
    PIRState=GPIO.input(PIR_PIN)
    if GPIO.input(PIR_PIN):
        print('PIR Input was HIGH')
    else:
        print('PIR Input was LOW')
    button1State=GPIO.input(SWITCH_PIN)
    #print("button state: ",button1State)
    if(button1State==False):
        playSlappy()

GPIO.cleanup()
