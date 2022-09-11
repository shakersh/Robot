from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import time
import random
from pygame import mixer
# from gpiozero import Motor , DistanceSensor
# from gpiozero import AngularServo
import pygame
pygame.mixer.init()
playsa = pygame.mixer.music

# motor1 = Motor(18,19,27)
# motor2 = Motor(22,23,24)
# sensor = DistanceSensor(echo=20, trigger=21)
# servo_1 = AngularServo(9, min_angle=0, max_angle=180)
# servo_2 = AngularServo(10, min_angle=0, max_angle=180)

# distance = 300 #high value at first to not make errors

# pygame.init()
# global image_number
# image_number = 0

# def getDistance():
#     global distance
#     distance = sensor.distance * 100


# def show_image():
#     FBS = 30 # the display frams per second
#     #surface = pygame.display.set_mode((1366,769))
#     surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#     clock = pygame.time.Clock()
#     display_run = True
#     while display_run:
#         clock.tick(FBS) # control the loop speed
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 display_run = False
          
#         get_pressed = pygame.key.get_pressed()
#         if(get_pressed[pygame.K_ESCAPE]):
#             display_run = False
#         elif(get_pressed[pygame.MOUSEWHEEL]):
#             display_run = False
                
        
#         #select image
#         if(image_number == 0):
#             displayimage = pygame.image.load(r'exp1.jpg')
#         elif(image_number == 1):
#             displayimage = pygame.image.load(r'exp2.jpg')
#         elif(image_number == 2):
#             displayimage = pygame.image.load(r'Albasma_logo.jpg')

        
#         surface.fill((0,0,0))
#         surface.blit(displayimage, (0,0))
#         pygame.display.update()
                
#     pygame.quit()


# def hands_up():
#     servo_1.angle = 100
#     servo_2.angle = 100

# def hands_down():
#     servo_1.angle = 10
#     servo_2.angle = 10


def Welcome():
    # hands_up()
    obj = gTTS(text='أهلا وسهلا بك',lang='ar',slow=False)
    obj.save('Welcome.mp3')
    playsa.load('Welcome.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    playsa.unload()
    obj = gTTS(text='روبوت البسمة هنا لأجلك',lang='ar',slow=False)
    obj.save('Welcome1.mp3')
    playsa.load('Welcome1.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    playsa.unload()

    obj = gTTS(text='كيف يمكنني مساعدتك',lang='ar',slow=False)
    obj.save('Welcome2.mp3')
    playsa.load('Welcome2.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    playsa.unload()
    # hands_down()
    speech()

def no_got_it():

    z = open(r'C:/Users/shake/Desktop/Al Bassmah projects/2.txt','r',encoding='utf-8')
    no_got_it = random.choice(z.readlines())
    obj = gTTS(text=no_got_it,lang='ar',slow=False)
    obj.save('no_got_it.mp3')
    playsa.load('no_got_it.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    playsa.unload()
    speech()

def speech():
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print('Say somethings ...... ^_^')
        audio=r.listen(src)
    try:
        word= r.recognize_google(audio,language='ar-AR')
        print(word)
        a = open(r'C:/Users/shake/Desktop/Al Bassmah projects/1.txt', "r",encoding='utf-8').readlines()
        line_number = 0
        for file in a :
            line_number+=1
            if word in file.strip():
                print(file.strip())
                next_line = a[line_number]
                print(next_line)
                obj= gTTS(text=next_line,lang='ar',slow=False)
                obj.save('question.mp3')
                playsa.load('question.mp3')
                playsa.play()
                while playsa.get_busy() == True:
                    continue
                playsa.unload()
                os.remove('question.mp3')
                speech()
            # elif (word == 'للامام' or word == 'للأمام' or word == 'الامام' or word == 'امام'):
            #     er = 0
            #     #while sensor value < 20cm
            #     while (er <=5):
            #         if (distance) >100 :
            #             print("FORWARD METHOD")
            #             motor1.forward(0.7)
            #             motor2.forward(0.7)
            #             time.sleep(1)
            #             er = er +1
            #         else:
            #             image_number = 1
            #             hands_up()
            #             os.system('obstacles.wav&')
            #             time.sleep(2)
            #             hands_down()
                        
            #     #stop motor
            #     motor1.stop()
            #     motor2.stop()
            #     time.sleep(1)
            #     #let motor stop
            #     print("FORWARD done")
            # elif (word == 'للخلف' or word == 'للوراء' or word == 'ارجع' or word == 'تراجع'):
            #     pass
            # elif (word == 'لليمين' or word == 'انعطف يمينً' or word == 'انعطي لليمين' or word == 'يمين'):
            #     pass
            # elif (word == 'لليسار' or word == 'الى اليسار' or word == 'يسار' or word == 'انعطف لليسار'):
            #     pass
            
        else:
            no_got_it()
    except sr.UnknownValueError as U:
        print(U)
        no_got_it()
    except sr.RequestError as R:
        print(R)
        no_got_it()

Welcome()
