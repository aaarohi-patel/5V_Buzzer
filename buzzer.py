#Libraries
import RPi.GPIO as GPIO
from time import sleep

# ===== Buzzer Pin sensor pin setting ==================
#set buzzer - pin 22
buzzerPin = 22
#set ground to pin 6


def cleanBoard():
    print("Cleaning up!")
    # Release resources - clean up the board setting
    GPIO.cleanup()


def setup():
    # Disable warnings (optional)
    GPIO.setwarnings(False)
    # set the GPIO to the BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # ===== LED sensor pin setting ==================
    GPIO.setup(buzzerPin, GPIO.OUT)
    
def BeepOn():
    GPIO.output(buzzerPin, GPIO.HIGH)
    
def BeepOff():
    GPIO.output(buzzerPin, GPIO.LOW)
    
def TestBuzzer():
    for i in range (1, 6):
        print("Beepo")
        BeepOn()
        sleep(0.5)  #delay in 5 sec
        print("No Beepo")
        BeepOff()
        sleep(0.5)
        
# main part
if __name__ == "__main__":
    setup()
    TestBuzzer()
    cleanBoard()
    
