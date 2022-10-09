from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import random
from pygame import mixer
from gpiozero import Robot
import pygame
from time import sleep
import time
pygame.mixer.init()
playsa = pygame.mixer.music
robot = Robot(left=(24, 23), right=(17, 27))
def happysmile():
    
    print("                            ████████████████████                           ")
    print("                    ██████████████████████████████████                     ")
    print("                ████████████▒▒            ░░██████████████                 ")
    print("              ██████████                          ██████████░░             ")
    print("            ████████                                  ██████████           ")
    print("          ██████                                          ██████▒▒         ")
    print("        ██████                                              ████████       ")
    print("      ██████                                                  ████████     ")
    print("    ██████                                                      ██████     ")
    print("    ██████                                                      ██████     ")
    print("  ██████                                                          ██████   ")
    print("  ██████                                                            ████   ")
    print("  ████                  ██████              ██████                  ██████ ")
    print("██████                ██████████          ██████████                  ████ ")
    print("██████                ██████████          ██████████                  ████ ")
    print("████                  ██████████          ██████████                  ████ ")
    print("████                    ██████              ██████                    ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("██████                                                                ████ ")
    print("██████              ██                              ██                ████ ")
    print("  ████            ██████                          ██████            ████   ")
    print("  ██████            ██████                      ████████            ████   ")
    print("  ██████            ██████████              ██████████            ██████   ")
    print("    ██████              ██████████████████████████              ██████     ")
    print("    ██████░░              ██████████████████████                ██████     ")
    print("      ██████                  ██████████████                  ████████     ")
    print("      ▒▒██████                                              ████████       ")
    print("        ████████                                          ████████         ")
    print("          ████████                                      ████████           ")
    print("            ██████████                              ██████████             ")
    print("                ██████████                    ▒▒██████████                 ")
    print("                    ████████████████████████████████████                   ")
    print("                        ████████████████████████                           ")
    print("                                                                           ")

def sadsmile():
    print("                            ████████████████████                           ")
    print("                    ██████████████████████████████████                     ")
    print("                ████████████▒▒            ░░██████████████                 ")
    print("              ██████████                          ██████████░░             ")
    print("            ████████                                  ██████████           ")
    print("          ██████                                          ██████▒▒         ")
    print("        ██████                                              ████████       ")
    print("      ██████                                                  ████████     ")
    print("    ██████                                                      ██████     ")
    print("    ██████                                                      ██████     ")
    print("  ██████                                                          ██████   ")
    print("  ██████                                                            ████   ")
    print("  ████                  ██████              ██████                  ██████ ")
    print("██████                ██████████          ██████████                  ████ ")
    print("██████                ██████████          ██████████                  ████ ")
    print("████                  ██████████          ██████████                  ████ ")
    print("████                    ██████              ██████                    ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("████                                                                  ████ ")
    print("██████                                                                ████ ")
    print("██████                        ██████████████                          ████ ")
    print("  ████                    ██████████████████████                    ████   ")
    print("  ██████                ██████████████████████████                  ████   ")
    print("  ██████             ██████████           ██████████              ██████   ")
    print("    ██████          ██████                    ████████          ██████     ")
    print("    ██████░░       ██████                         ██████        ██████     ")
    print("      ██████        ██                              ██        ████████     ")
    print("      ▒▒██████                                              ████████       ")
    print("        ████████                                          ████████         ")
    print("          ████████                                      ████████           ")
    print("            ██████████                              ██████████             ")
    print("                ██████████                    ▒▒██████████                 ")
    print("                    ████████████████████████████████████                   ")
    print("                        ████████████████████████                           ")
    print("                                                                           ") 
    no_got_it()

# def distance():
#     # set Trigger to HIGH
#     GPIO.output(GPIO_TRIGGER, True)
 
#     # set Trigger after 0.01ms to LOW
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
 
#     StartTime = time.time()
#     StopTime = time.time()
 
#     # save StartTime
#     while GPIO.input(GPIO_ECHO) == 0:
#         StartTime = time.time()
 
#     # save time of arrival
#     while GPIO.input(GPIO_ECHO) == 1:
#         StopTime = time.time()
 
#     # time difference between start and arrival
#     TimeElapsed = StopTime - StartTime
#     # multiply with the sonic speed (34300 cm/s)
#     # and divide by 2, because there and back
#     distance = (TimeElapsed * 34300) / 2
 
#     return distance



def Welcome():
    happysmile()
    obj = gTTS(text='أهلا وسهلا بك',lang='ar')
    obj.save('Welcome.mp3')
    playsa.load('Welcome.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    obj = gTTS(text='روبوت البسمة هنا لأجلك',lang='ar')
    obj.save('Welcome1.mp3')
    playsa.load('Welcome1.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue

    obj = gTTS(text='كيف يمكنني مساعدتك',lang='ar')
    obj.save('Welcome2.mp3')
    playsa.load('Welcome2.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
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
    speech()

def student():
    x = open('3.txt','r',encoding='utf-8')
    stud = random.choice(x.readlines())
    obj = gTTS(text=stud,lang='ar')
    obj.save('stud.mp3')
    playsa.load('stud.mp3')
    playsa.play()
    while playsa.get_busy() == True:
        continue
    speech()


def speech():
    # setup()
    happysmile()
    # dist = distance()
    # print ("Measured Distance = %.1f cm" % dist)
    # if dist < 100: # check if the ogject is too close to sensor
    #     obj = gTTS(text='انتبه امامي عائق',lang='ar')
    #     obj.save('door.mp3')
    #     playsa.load('door.mp3')
    #     playsa.play()
    #     while playsa.get_busy() == True:
    #         continue
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

            elif word == 'انا طالب' or word == 'طالب':
                student()

            elif word == 'مرحبا' or word == 'مرحب' or word == 'مرحبن' :
                obj = gTTS(text='أهلا وسهلا بك',lang='ar')
                obj.save('Welcome.mp3')
                playsa.load('Welcome.mp3')
                playsa.play()
                while playsa.get_busy() == True:
                    continue
                robot.forward(0.5)
                sleep(2)
                robot.right(0.2)
                sleep(1)
                robot.forward(0.5)
                sleep(2)
                robot.right(0.2)
                sleep(1)
                robot.forward(0.5)
                sleep(2)
                robot.right(0.2)
                sleep(1)
                robot.forward(0.5)
                sleep(2)
                robot.right(0.2)
                sleep(1)
                robot.stop()
                speech()
                
            elif (word == 'للامام' or word == 'للأمام' or word == 'الامام' or word == 'امام' or word == 'تقدم' or word == 'قدم'):
                robot.forward(0.5)
                sleep(20)
                robot.stop()
                print("Forward done")
                speech()

            elif (word == 'للخلف' or word == 'للوراء' or word == 'ارجع' or word == 'تراجع' or word == 'خلف'):
                robot.backward(0.5)
                sleep(20)
                robot.stop()
                print("Backward done")
                speech()

            elif (word == 'اليمين' or word == 'انعطف يمينً' or word == 'انعطي لليمين' or word == 'يمين' or word == 'مين' or word == 'يمن'):
                robot.right(0.2)
                sleep(1)
                robot.stop()
                print('Right done')
                speech()

            elif (word == 'لليسار' or word == 'الى اليسار' or word == 'يسار' or word == 'انعطف لليسار'or word == 'ياسر'):
                robot.left(0.2)
                sleep(1)
                robot.stop()
                print('Left done')
                speech()

            elif (word == "ارقص" or word == "ارقص لي" or word == "ارقصلي" or word == "رقص"):
                robot.forward(0.5)
                sleep(3)
                robot.stop()
                robot.backward(0.5)
                sleep(1)
                robot.stop()
                robot.forward(0.5)
                sleep(1)
                robot.stop()
                robot.backward(0.5)
                sleep(0.5)
                robot.stop()
                robot.right(0.2)
                sleep(3)
                robot.stop()
                robot.left(0.2)
                sleep(5)
                robot.stop()
                robot.backward(0.5)
                sleep(4)
                robot.stop()
                robot.right(0.2)
                sleep(3)
                robot.stop()
                robot.left(0.2)
                sleep(6)
                robot.stop()
                robot.backward(0.5)
                sleep(0.5)
                robot.stop()
                robot.left(0.2)
                sleep(0.7)
                robot.stop()
            
        else:
            sadsmile()

    except sr.UnknownValueError as U:
        # print(U)
        no_got_it()

    except sr.RequestError as R:
        # print(R)
        no_got_it()

Welcome()


