#developer: UTH
# crear las librerias
from Tkinter import * #libreria de grafico nos permite manipular cajas de texto
import ttk #libreria de objetos especiales
import os #libreria de ejecutar comandos
import time #libreria para manejar tiempo y pausa
import tkFont #libreria para configurar tipo de fuente
import tkMessageBox
import subprocess

# Crear ventana
v0=Tk()
v0.title("Control I/O (INPUT/OUTPUT)")
v0.geometry("500x400+0+0")
img_on = PhotoImage(file="~/Documentos/proyecto_pi/encender.png")
img_off = PhotoImage(file="~/Documentos/proyecto_pi/apagar.png")


# zona de tipo de fuentes
text1=tkFont.Font(family="Arial", size=20)

# zona de etiquetas
label1=Label(v0,text="CONTROL I/O",font=text1).place(x=145,y=10)
label_on=Label(v0,text="GPIO17 ",font=text1).place(x=30,y=100)
label_on=Label(v0,text="GPIO21 ",font=text1).place(x=170,y=100)
label_on=Label(v0,text="GPIO27 ",font=text1).place(x=300,y=100)

def update():
             pf=open("~/Documentos/proyecto_pi/gpio17.txt","r")
             for line in pf:
                campo=line.split("\n")
                campof=campo[0]

                if (campof == "1"):
                                btn_on=Button(v0,image=img_on).place(x=40,y=150)
                                v0.after(1000,update)
                if (campof == "0"):
                                
                                btn_off=Button(v0,image=img_off).place(x=40,y=150)
                                v0.after(1000,update)
update()

def update2():
             pf=open("~/Documentos/proyecto_pi/gpio21.txt","r")
             for line in pf:
                campo=line.split("\n")
                campof=campo[0]

                if (campof == "1"):
                                btn_on=Button(v0,image=img_on).place(x=180,y=150)
                                v0.after(1000,update2)
                if (campof == "0"):
                                btn_on=Button(v0,image=img_off).place(x=180,y=150)
                                v0.after(1000,update2)

update2()

def update3():
             pf=open("~/Documentos/proyecto_pi/gpio27.txt","r")
             for line in pf:
                campo=line.split("\n")
                campof=campo[0]

                if (campof == "1"):
                                btn_on=Button(v0,image=img_on).place(x=310,y=150)
                                v0.after(1000,update3)
                if (campof == "0"):
                                btn_off=Button(v0,image=img_off).place(x=310,y=150)
                                v0.after(1000,update3)
update3()

    

#Definicion de funciones e imprimir texto
#Se debe ser ordenado y respetar los margenes tal cual para que no de error
def on17():
        print "ENCENDIDO"
        os.system("~/Documentos/proyecto_pi/encender17.sh")
def off17():
        print "APAGADO"
        os.system("~/Documentos/proyecto_pi/apagar17.sh")
        
def on21():
        print "ENCENDIDO"
        os.system("~/Documentos/proyecto_pi/encender21.sh") 
def off21():
        print "APAGADO"
        os.system("~/Documentos/proyecto_pi/apagar21.sh")
        
def on27():
        print "ENCENDIDO"
        os.system("~/Documentos/proyecto_pi/encender27.sh")
def off27():
        print "APAGADO"
        os.system("~/Documentos/proyecto_pi/apagar27.sh")        

    
# zona de Botones
btn_on=Button(v0,text="ON",command=on17).place(x=30,y=250)
btn_off=Button(v0,text="OFF",command=off17).place(x=80,y=250)

btn_on=Button(v0,text="ON",command=on21).place(x=170,y=250)
btn_off=Button(v0,text="OFF",command=off21).place(x=220,y=250)

btn_on=Button(v0,text="ON",command=on27).place(x=300,y=250)
btn_off=Button(v0,text="OFF",command=off27).place(x=350,y=250)


v0.mainloop()

