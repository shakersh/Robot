from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import random
from pygame import mixer
import RPi.GPIO as GPIO
import pygame
from time import sleep
pygame.mixer.init()
playsa = pygame.mixer.music
Motor1A = 16
Motor1B = 18
Motor1C = 38
Motor2A = 11
Motor2B = 13
Motor2C = 40

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1C,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2C,GPIO.OUT)

def StopM():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1C,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2C,GPIO.LOW)

def ForwardM():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1C,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2C,GPIO.HIGH)

def BackM():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1C,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2C,GPIO.HIGH)

def RightM():
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2C,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1C,GPIO.HIGH)

def LeftM():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1C,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2C,GPIO.HIGH)
# sensor = DistanceSensor(echo=20, trigger=21)
# servo_1 = AngularServo(9, min_angle=0, max_angle=180)
# servo_2 = AngularServo(10, min_angle=0, max_angle=180)


# pygame.init()
#global image_number
#image_number = 0



#def show_image():
#    FBS = 30 # the display frams per second
#    surface = pygame.display.set_mode((1366,769))
#    surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#    clock = pygame.time.Clock()
#    display_run = True
#    while display_run:
#        clock.tick(FBS) # control the loop speed

#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                display_run = False
#
#        get_pressed = pygame.key.get_pressed()
#        if(get_pressed[pygame.K_ESCAPE]):
#            display_run = False
#        elif(get_pressed[pygame.MOUSEWHEEL]):
#            display_run = False
#

#        select image
#        if(image_number == 0):
#            displayimage = pygame.image.load(r'exp1.jpg')
#        elif(image_number == 1):
#            displayimage = pygame.image.load(r'exp2.jpg')
#        elif(image_number == 2):
#            displayimage = pygame.image.load(r'Albasma_logo.jpg')


#        surface.fill((0,0,0))
#        surface.blit(displayimage, (0,0))
#        pygame.display.update()

#    pygame.quit()


#def hands_up():
#    servo_1.angle = 100
#    servo_2.angle = 100


def Welcome():
 #   hands_up()
    GPIO.cleanup()
    obj = gTTS(text='أهلا وسهلا بك',lang='ar')
    obj.save('Welcome.mp3')
    playsa.load('Welcome.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    #playsa.unload()
    obj = gTTS(text='روبوت البسمة هنا لأجلك',lang='ar')
    obj.save('Welcome1.mp3')
    playsa.load('Welcome1.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    #playsa.unload()

    obj = gTTS(text='كيف يمكنني مساعدتك',lang='ar')
    obj.save('Welcome2.mp3')
    playsa.load('Welcome2.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    #playsa.unload()
    # hands_down()
    speech()

def no_got_it():

    z = open('2.txt','r',encoding='utf-8')
    no_got_it = random.choice(z.readlines())
    obj = gTTS(text=no_got_it,lang='ar')
    obj.save('no_got_it.mp3')
    playsa.load('no_got_it.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    #playsa.unload()
    speech()

def speech():
    setup()
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print('Say somethings ...... ^_^')
        audio=r.listen(src,timeout=3,phrase_time_limit=3)
    try:
        word= r.recognize_google(audio,language='ar-AR')
        print(word)
        a = open('1.txt', "r",encoding='utf-8').readlines()
        line_number = 0
        for file in a :
            line_number+=1
            if word in file.strip():
                print(file.strip())
                next_line = a[line_number]
                print(next_line)
                obj= gTTS(text=next_line,lang='ar')
                obj.save('question.mp3')
                playsa.load('question.mp3')
                playsa.play()
                while playsa.get_busy() == True:
                    continue
                playsa.unload()
                os.remove('question.mp3')
                speech()
            elif (word == 'للامام' or word == 'للأمام' or word == 'الامام' or word == 'امام' or word == 'تقدم'):

                ForwardM()
                sleep(10)
                StopM()
                print("Forward done")
                GPIO.cleanup()
                speech()
            elif (word == 'للخلف' or word == 'للوراء' or word == 'ارجع' or word == 'تراجع' or word == 'خلف'):
                BackM()
                sleep(10)
                StopM()
                print("Backward done")
                GPIO.cleanup()
                speech()
            elif (word == 'لليمين' or word == 'انعطف يمينً' or word == 'انعطي لليمين' or word == 'يمين'):
                RightM()
                sleep(10)
                StopM()
                print('Right done')
                GPIO.cleanup()
                speech()
            elif (word == 'لليسار' or word == 'الى اليسار' or word == 'يسار' or word == 'انعطف لليسار'or word == 'ياسر'):
                LeftM()
                sleep(10)
                StopM()
                print('L eft done')
                GPIO.cleanup()
                speech()
            elif (word == "ارقص" or word == "ارقص لي" or word == "ارقصلي" or word == "رقص"):
                ForwardM()
                sleep(3)
                StopM()
                BackM()
                sleep(1)
                StopM()
                ForwardM()
                sleep(1)
                StopM()
                BackM()
                sleep(0.5)
                StopM()
                RightM()
                sleep(3)
                StopM()
                LeftM()
                sleep(5)
                StopM()
                BackM()
                sleep(4)
                StopM()
                RightM()
                sleep(3)
                StopM()
                LeftM()
                sleep(6)
                StopM()
                BackM()
                sleep(0.5)
                StopM()
                LeftM()
                sleep(0.7)
                StopM()
                GPIO.cleanup()
        else:
            GPIO.cleanup()
            no_got_it()
    except sr.UnknownValueError as U:
        print(U)
        GPIO.cleanup()
        no_got_it()
    except sr.RequestError as R:
        print(R)
        GPIO.cleanup()
        no_got_it()

Welcome()


