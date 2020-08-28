from tkinter import *
import pygame
import pyttsx3

#- inicializar pygame
pygame.init()

#- inicializar pyttsx3
engine = pyttsx3.init()
# voz de mujer en ingles
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female / 0 for male
# velocidad (palabras por minuto)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)     # setting up new voice rate (normal 200)

#- ventana con tkinter
root = Tk()
root.title('Alphabet Application')
root.geometry('1352x652+0+10')
root.config(background='white')

str1 = StringVar()
str1.set('Welcome to PyPiao Academy')
frame1 = Frame(root, bg='white')
frame1.grid()

#- imagen del centro
Disp = Canvas(frame1, width=160, height=120, bg='white')
Disp.grid(row=1, column=3)
img = PhotoImage(file='Images/Icon.png')
Image = Disp.create_image(85,62,image=img)

imgClear = PhotoImage(file='Images/Icon.png')
def reset():
    str1.set('Welcome to PyPiao Academy')
    Disp.create_image(85,62,image=imgClear)
    engine.say('Welcome to PyPiao Academy')
    engine.runAndWait()


#- llamar a las imagenes
imgA = PhotoImage(file='Images/Apple.png')
def alphabet_A():
    str1.set('A is for Apple')
    Disp.create_image(85,62,image=imgA)
    engine.say('A is for Apple')
    engine.runAndWait()

imgB = PhotoImage(file='Images/Banana.png')
def alphabet_B():
    str1.set('B is for Banana')
    Disp.create_image(85,62,image=imgB)
    engine.say('B is for Banana')
    engine.runAndWait()

imgC = PhotoImage(file='Images/Cocoa.png')
def alphabet_C():
    str1.set('C is for Cocoa')
    Disp.create_image(85,62,image=imgC)
    engine.say('C is for Cocoa')
    engine.runAndWait()

imgD = PhotoImage(file='Images/Damson.png')
def alphabet_D():
    str1.set('D is for Damson')
    Disp.create_image(85,62,image=imgD)
    engine.say('D is for Damson')
    engine.runAndWait()

imgE = PhotoImage(file='Images/Elderberry.png')
def alphabet_E():
    str1.set('E is for Elderberry')
    Disp.create_image(85,62,image=imgE)
    engine.say('E is for ElderBerry')
    engine.runAndWait()

imgF = PhotoImage(file='Images/Fig.png')
def alphabet_F():
    str1.set('F is for Fig')
    Disp.create_image(85,62,image=imgF)
    engine.say('F is for Fig')
    engine.runAndWait()

imgG = PhotoImage(file='Images/Guava.png')
def alphabet_G():
    str1.set('G is for Guava')
    Disp.create_image(85,62,image=imgG)
    engine.say('G is for Guava')
    engine.runAndWait()

imgH = PhotoImage(file='Images/HuckleBerry.png')
def alphabet_H():
    str1.set('H is for HuckleBerry')
    Disp.create_image(85,62,image=imgH)
    engine.say('H is for HuckleBerry')
    engine.runAndWait()

imgI = PhotoImage(file='Images/Ita palm.png')
def alphabet_I():
    str1.set('I is for Ita palm')
    Disp.create_image(85,62,image=imgI)
    engine.say('I is for Ita palm')
    engine.runAndWait()

imgJ = PhotoImage(file='Images/Jujube.png')
def alphabet_J():
    str1.set('J is for Jujube')
    Disp.create_image(85,62,image=imgJ)
    engine.say('J is for Jujube')
    engine.runAndWait()

imgK = PhotoImage(file='Images/Kumquat.png')
def alphabet_K():
    str1.set('K is for Kumquat')
    Disp.create_image(85,62,image=imgK)
    engine.say('K is for Kumquat')
    engine.runAndWait()

imgL = PhotoImage(file='Images/Lime.png')
def alphabet_L():
    str1.set('L is for Lime')
    Disp.create_image(85,62,image=imgL)
    engine.say('L is for Lime')
    engine.runAndWait()

imgM = PhotoImage(file='Images/Mango.png')
def alphabet_M():
    str1.set('M is for Mango')
    Disp.create_image(85,62,image=imgM)
    engine.say('M is for Mango')
    engine.runAndWait()

imgN = PhotoImage(file='Images/Nance.png')
def alphabet_N():
    str1.set('N is for Nance')
    Disp.create_image(85,62,image=imgN)
    engine.say('N is for Nance')
    engine.runAndWait()

imgO = PhotoImage(file='Images/Orange.png')
def alphabet_O():
    str1.set('O is for Orange')
    Disp.create_image(85,62,image=imgO)
    engine.say('O is for Orange')
    engine.runAndWait()

imgP = PhotoImage(file='Images/Papaya.png')
def alphabet_P():
    str1.set('P is for Papaya')
    Disp.create_image(85,62,image=imgP)
    engine.say('P is for Papaya')
    engine.runAndWait()

imgQ = PhotoImage(file='Images/Quince.png')
def alphabet_Q():
    str1.set('Q is for Quince')
    Disp.create_image(85,62,image=imgQ)
    engine.say('Q is for Quince')
    engine.runAndWait()

imgR = PhotoImage(file='Images/RaspBerry.png')
def alphabet_R():
    str1.set('R is for RaspBerry')
    Disp.create_image(85,62,image=imgR)
    engine.say('R is for RaspBerry')
    engine.runAndWait()

imgS = PhotoImage(file='Images/StrawBerry.png')
def alphabet_S():
    str1.set('S is for StrawBerry')
    Disp.create_image(85,62,image=imgS)
    engine.say('S is for StrawBerry')
    engine.runAndWait()

imgT = PhotoImage(file='Images/Tamarind.png')
def alphabet_T():
    str1.set('T is for Tamarind')
    Disp.create_image(85,62,image=imgT)
    engine.say('T is for Tamarind')
    engine.runAndWait()

imgU = PhotoImage(file='Images/Ugli.png')
def alphabet_U():
    str1.set('U is for Ugli')
    Disp.create_image(85,62,image=imgU)
    engine.say('U is for Ugli')
    engine.runAndWait()

imgV = PhotoImage(file='Images/Vanilla.png')
def alphabet_V():
    str1.set('V is for Vanilla')
    Disp.create_image(85,62,image=imgV)
    engine.say('V is for Vanilla')
    engine.runAndWait()

imgW = PhotoImage(file='Images/Watermelon.png')
def alphabet_W():
    str1.set('W is for Watermelon')
    Disp.create_image(85,62,image=imgW)
    engine.say('W is for Watermelon')
    engine.runAndWait()

imgX = PhotoImage(file='Images/Xigua.png')
def alphabet_X():
    str1.set('X is for Xigua')
    Disp.create_image(85,62,image=imgX)
    engine.say('X is for Xigua')
    engine.runAndWait()

imgY = PhotoImage(file='Images/Yuzu.png')
def alphabet_Y():
    str1.set('Y is for Yuzu')
    Disp.create_image(85,62,image=imgY)
    engine.say('Y is for Yuzu')
    engine.runAndWait()

imgZ = PhotoImage(file='Images/Zucchini.png')
def alphabet_Z():
    str1.set('Z is for Zucchini')
    Disp.create_image(85,62,image=imgZ)
    engine.say('Z is for Zucchini')
    engine.runAndWait()


#=================== Main Screen ===================#
Display = Entry(frame1, textvariable=str1, font=('arial',44,'bold'), bg='blue', fg='white', bd=34, width=39, justify=CENTER)
Display.grid(row=0, column=0, columnspan=7, pady=1)

#=================== Row 1 ===================#
btnA = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_A, width=10, height=3, text='A', bg='orange', fg='white')\
    .grid(row=1, column=0)
btnB = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_B, width=10, height=3, text='B', bg='orange', fg='white').grid(row=1, column=1)
btnC = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_C, width=10, height=3, text='C', bg='orange', fg='white').grid(row=1, column=2)
btnD = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_D, width=10, height=3, text='D', bg='orange', fg='white').grid(row=1, column=4)
btnE = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_E, width=10, height=3, text='E', bg='orange', fg='white').grid(row=1, column=5)
btnF = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_F, width=10, height=3, text='F', bg='orange', fg='white').grid(row=1, column=6)

#=================== Row 2 ===================#
btnG = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_G, width=10, height=3, text='G', bg='orange', fg='white')\
    .grid(row=2, column=0)
btnH = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_H, width=10, height=3, text='H', bg='blue', fg='white').grid(row=2, column=1)
btnI = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_I, width=10, height=3, text='I', bg='blue', fg='white').grid(row=2, column=2)
btnJ = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_J, width=10, height=3, text='J', bg='blue', fg='white').grid(row=2, column=3)
btnK = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_K, width=10, height=3, text='K', bg='blue', fg='white').grid(row=2, column=4)
btnL = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_L, width=10, height=3, text='L', bg='blue', fg='white').grid(row=2, column=5)
btnM = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_M, width=10, height=3, text='M', bg='orange', fg='white').grid(row=2, column=6)

#=================== Row 3 ===================#
btnN = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_N, width=10, height=3, text='N', bg='orange', fg='white')\
    .grid(row=3, column=0)
btnO = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_O, width=10, height=3, text='O', bg='blue', fg='white').grid(row=3, column=1)
btnP = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_P, width=10, height=3, text='P', bg='blue', fg='white').grid(row=3, column=2)
btnQ = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_Q, width=10, height=3, text='Q', bg='blue', fg='white').grid(row=3, column=3)
btnR = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_R, width=10, height=3, text='R', bg='blue', fg='white').grid(row=3, column=4)
btnS = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_S, width=10, height=3, text='S', bg='blue', fg='white').grid(row=3, column=5)
btnT = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_T, width=10, height=3, text='T', bg='orange', fg='white').grid(row=3, column=6)

#=================== Row 4 ===================#
btnU = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_U, width=10, height=3, text='U', bg='orange', fg='white')\
    .grid(row=4, column=0)
btnV = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_V, width=10, height=3, text='V', bg='orange', fg='white').grid(row=4, column=1)
btnW = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_W, width=10, height=3, text='W', bg='orange', fg='white').grid(row=4, column=2)
btnReset = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=reset, width=10, height=3, text='Reset', bg='green', fg='white').grid(row=4, column=3)
btnX = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_X, width=10, height=3, text='X', bg='orange', fg='white').grid(row=4, column=4)
btnY = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_Y, width=10, height=3, text='Y', bg='orange', fg='white').grid(row=4, column=5)
btnZ = Button(frame1, pady=1, bd=1, font=('arial',21,'bold'),command=alphabet_Z, width=10, height=3, text='Z', bg='orange', fg='white').grid(row=4, column=6)


root.mainloop()
