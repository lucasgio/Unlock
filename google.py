#!/usr/bin/python3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as msg
from tkinter.ttk import Progressbar
from adbutils import adb
from bbdd import *
from msj import *
import os
import time
import sys
import os.path
import webbrowser
import adbutils





class Principal:

    def __init__(self):
        self.google = Tk() 
        self.titulo = 'GSM TOOL'
        self.icono = os.path.abspath('.\\imagenes\\phone.ico')
        self.fondo1 = ImageTk.PhotoImage(file= '.\\imagenes\\home.jpg')
        #self.usbimg = ImageTk.PhotoImage(file= '.\\imagenes\\usb.png')
        self.user = StringVar()
        self.password = StringVar()
        self.loginmenu = Menu()
        self.framederecho = Frame()
        self.codenames = ('Sailfish','Marlin','Walleye','Taimen','Blueline','Crosshatch','Sargo','Bonito','Flame','Coral','Sunfish','Bramble','Redfin')
        self.unlock = ImageTk.PhotoImage(file= '.\\imagenes\\pixel.jpg')
        self.color = '#B0A8B9'
        self.menu = None
        self.usb = None
        self.bypass = None
        self.log = None
        self.select = None
        self.detalles =None
        self.ope = None
        self.log1 = None
        self.logmarca = None
        self.logmodelo = None
        self.size = '720x680'
        self.color = '#B0A8B9'
        self.bbdd = BBDD() 
        self.msj = Mensajes()
    

        
    ### START LOGIC
    def loginusuarios(self):
         # Vericamos si la tupla del parametro viene vacia
        try:
            datos = (self.user.get(),self.password.get())
            consulta  = self.bbdd.loginusuario(datos)
            self.mainmenu(consulta[3])
            self.user = consulta[0]
            try:
                if datos[0] == consulta[1] and datos[1] == consulta[2]:
                    msg.showinfo('Success','Your user are successfully logged')
                    self.validacionsaldo(consulta[3])
                    self.login.destroy()            
            except Exception:
                msg.showerror('Error','User: '+ datos[0] + ' not exits in the system')
        except Exception:
            msg.showerror("Error","""
               1.The user and password fields can't empty
               2.Check Internet
            """)

    ##  BLOQUE Form para crear usuarios y login de usuario
    def crearusuario(self):
        datos = (self.user.get(),self.password.get())
        consulta = self.bbdd.createuser(datos)
        if consulta:
           msg.showinfo('Information','The account is successfully complete') 
           self.registre.destroy()
    
     ## BLOQUE UNLOCK GOOGLE PIXEL
    def scangoogle(self):
        # Intrucciones para el desbloqueo
        # Buscamos dispositvos y sacamos Information
        # Llamamos a la funcion UNLOCKTRUTH() si cumple la condicion con los datos obtenidos
        for d in adb.devices():
            self.progress['value'] += 10
            self.google.update_idletasks()
            time.sleep(1.5)
            log = d.serial
            self.ope = Label(self.framederecho,text='Searching any Google Pixel ...')
            self.ope.config(bg='white')
            self.ope.pack(anchor=W,pady=10,padx=10)
            time.sleep(2.0)
            self.progress['value'] += 15
            self.google.update_idletasks()
            self.log1 = Label(self.framederecho,text=f'No serial: {log}')
            self.log1.config(bg='white')
            self.log1.pack(anchor=W,pady=5,padx=10)
            time.sleep(2.5)
            self.progress['value'] += 20
            self.google.update_idletasks()
            d = adb.device()
            marca = d.prop.name
            modelo = d.prop.model
            time.sleep(3.0)
            self.progress['value'] += 25
            self.google.update_idletasks()
            self.logmarca = Label(self.framederecho,text=f'Brand: {marca}')
            self.logmarca.config(bg='white')
            self.logmarca.pack(anchor=W,pady=5,padx=10) 
            time.sleep(3.5)
            self.progress['value'] += 30
            self.google.update_idletasks()
            self.logmodelo = Label(self.framederecho,text=f'Model: {modelo}')
            self.logmodelo.config(bg='white')
            self.logmodelo.pack(anchor=W,pady=5,padx=10)
            if not self.logmarca in self.codenames:
                msg.showinfo("Information","The devices connected isn't a Google Pixel,please recheck")
                self.progress['value'] = 0
                self.borrarlog()
                return False
            self.unlocktruth()

    def borrarlog(self):
        # Borramos el frame derecho que contiene los LOG del debloqueo
        self.ope.pack_forget()
        self.log1.pack_forget()
        self.logmarca.pack_forget()
        self.logmodelo.pack_forget()

    def unlocktruth(self):
        # Ejecutamos la segunda funcion del proceso de unlock llamada desde la funcion SCANGOOGLE()
        d = adb.device()
        self.progress['value'] = 0
        log3 = Label(self.framederecho, text='Trying to Unlock .... ')
        log3.pack(anchor=W,pady=5,padx=10)
        self.google.update_idletasks()
        time.sleep(2.0)
        d.shell('pm uninstall -k --user 0 com.google.android.apps.work.oobconfig')
        self.progress['value'] += 30
        self.google.update_idletasks()
        log4 = Label(self.google,text='Sending data to server ... ')
        log4.pack(anchor=W,pady=5,padx=10)
        self.progress['value'] += 50
        self.google.update_idletasks()    
        time.sleep(2.2)
        log5 = Label(self.google,text='Receiving data from server ...')
        log5.pack(anchor=W,pady=5,padx=10)
        self.progress['value'] += 50
        self.google.update_idletasks() 
        time.sleep(1.2)
        if adb == 0:
            self.msj.infosucces()
            return False
        elif adb == 1:
            self.msj.infoerror()
            return False
         
    ## END   


    ## INIT

    def setup(self):
        # Configuracion de lo aplicacion
        self.google.geometry(self.size)
        self.google.iconbitmap(self.icono)    
        self.google.title(self.titulo)
        self.google.resizable(0,0)
        self.google.config(bg=self.color)


    ### START DISEÑO      
        
    def loginmain(self):
        # Diseño del form login
        self.loginmenu = Frame(self.google,width=350,height=550)
        self.loginmenu.config(bg=self.color)
        self.loginmenu.pack(side=TOP,pady=5)
        img = Label(self.loginmenu,image=self.fondo1)
        img.pack(side=TOP)
        label1 = Label(self.loginmenu,text='GSM TOOL - IOSVANY ALVAREZ 2020')
        label1.config(bg=self.color)
        label1.pack(side=BOTTOM,pady=10)


    def mainmenu(self,saldo=""):
        # Menu
        self.menu = Menu(self.google)
        self.google.config(menu = self.menu)

        # Submenu Operaciones
        operaciones = Menu(self.menu,tearoff=0)
        operaciones.add_command(label='Unlock Permanent Google Pixel',command=self.unlockgoogle)
        #Menu
        self.menu.add_cascade(label='Operations',menu=operaciones)
        self.menu.add_command(label='Exit',command=self.google.quit)

    def unlockgoogle(self):
        #Diseño de widget Unlock Google Pixel
        self.loginmenu.pack_forget() 
        self.usb = Frame(self.google,width=400,height=680)
        self.usb.config(bg="green")
        self.usb.pack(side=LEFT)
        # Imagen
        img = Label(self.usb,image=self.unlock)
        img.pack(side=LEFT)
        # Detalles
        self.detalles = Frame(self.google,width=320,height=480)
        self.detalles.config(bg=self.color)
        self.detalles.pack()
        titulo = Label(self.detalles,text="Instruccionts")
        titulo.config(bg=self.color)
        titulo.pack(anchor=W,pady=10)
        # Instrucciones
        instrucciones1 = Label(self.detalles,text='1. Hard reset via RECOVERY without SIM')
        instrucciones2 = Label(self.detalles,text='2. Start Initial Configuration (WITHOUT INTERNET)')
        instrucciones3 = Label(self.detalles,text='3. Enable USB debugging')
        instrucciones4 = Label(self.detalles,text='4. Connect Google Pixel to PC')
        instrucciones6 = Label(self.detalles,text='6. Click UNLOCK')
        instrucciones1.pack(anchor=W)
        instrucciones1.config(bg=self.color)
        instrucciones2.pack(anchor=W)
        instrucciones2.config(bg=self.color)
        instrucciones3.pack(anchor=W)
        instrucciones3.config(bg=self.color)
        instrucciones4.pack(anchor=W)
        instrucciones4.config(bg=self.color)
        instrucciones6.pack(anchor=W)
        instrucciones6.config(bg=self.color)
        # Botones
        unlock = Button(self.detalles,text='Unlock',command=self.scangoogle)
        unlock.config(padx=30)
        unlock.pack(anchor=W,pady=50)
        self.progress = Progressbar(self.detalles, orient=HORIZONTAL,length=300, mode="determinate")
        self.progress.pack(anchor=W,pady=50)
        detalles = Label(self.detalles,text='LOG')  
        detalles.config(bg=self.color) 
        detalles.pack(anchor=S,pady=20) 
        # Log
        self.framederecho = Frame(self.google, width=350, height=200)
        self.framederecho.config(bg='white',relief=RIDGE)
        self.framederecho.pack(side=RIGHT, anchor=S)
        self.framederecho.pack_propagate(False)         
    ### END DISEÑO
   
    ### START WIDGET
    def usercenter(self):
        self.login = Tk()
        self.login.title(self.titulo)
        self.login.geometry('350x200')
        self.login.iconbitmap(self.icono)
        self.login.resizable(0,0)
        self.login.config(bg=self.color)
        # Form Login
        user = Label(self.login,text='Usuario')
        user.config(bg=self.color)
        user.grid(row=0,column=2,padx=20,pady=30)
        self.user = Entry(self.login)
        self.user.grid(row=0,column=3,padx=20)
        password = Label(self.login,text='Password')
        password.config(bg=self.color)
        password.grid(row=1,column=2,padx=20,pady=20)
        self.password = Entry(self.login)
        self.password.grid(row=1,column=3,padx=10)
        # Boton
        loginbutton = Button(self.login,text='Login',command=self.loginusuarios)
        loginbutton.config(padx=20)
        loginbutton.grid(row=2,column=3,padx=20)

    def registercenter(self):
        self.registre = Tk()
        self.registre.title(self.titulo)
        self.registre.geometry('350x200')
        self.registre.iconbitmap(self.icono)
        self.registre.resizable(0,0)
        self.registre.config(bg=self.color)
        # Form registre
        user = Label(self.registre,text='Usuario')
        user.config(bg=self.color)
        user.grid(row=0,column=2,padx=20,pady=30)
        self.user = Entry(self.registre)
        self.user.grid(row=0,column=3,padx=20)
        password = Label(self.registre,text='Password')
        password.config(bg=self.color)
        password.grid(row=1,column=2,padx=20,pady=20)
        self.password = Entry(self.registre)
        self.password.grid(row=1,column=3,padx=10)
        # Boton
        registrebutton = Button(self.registre,text='Registre',command=self.crearusuario)
        registrebutton.config(padx=20)
        registrebutton.grid(row=2,column=3,padx=20)

    ### END WIDGET



    def run(self):
        self.google.mainloop()





if __name__ == '__main__':
    newgoogle = Principal()
    newgoogle.setup()
    newgoogle.mainmenu()
    newgoogle.loginmain()
    newgoogle.run()



        