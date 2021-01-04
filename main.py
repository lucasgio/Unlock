#!/usr/bin/python3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as msg
from adbutils import adb
from bbdd import *
import os
import time
import sys
import os.path
import webbrowser
import adbutils




class Google:

    def __init__(self):

        self.google = Tk() 
        self.titulo = 'GSM TOOL'
        self.icono = os.path.abspath('.\\imagenes\\phone.ico')
        self.fondo1 = ImageTk.PhotoImage(file= '.\\imagenes\\home.jpg')
        self.unlock = ImageTk.PhotoImage(file= '.\\imagenes\\pixel.jpg')
        #self.usbimg = ImageTk.PhotoImage(file= '.\\imagenes\\usb.png')
        self.user = StringVar()
        self.password = StringVar()
        self.device = StringVar()
        self.devices= ['Dispositivos Conectados']
        self.device.set(self.devices)
        self.loginmenu = None
        self.menu = None
        self.usb = None
        self.bypass = None
        self.log = None
        self.select = None
        self.detalles =None
        self.size = '720x680'
        self.color = '#B0A8B9'
        self.bbdd = BBDD() 

        
    #### Start  Logica 
    def loginusuarios(self):
         # Vericamos si la tupla del parametro viene vacia
        try:
            datos = (self.user.get(),self.password.get())
            consulta  = self.bbdd.loginusuario(datos)
            self.mainmenu(consulta[3])
            self.user = consulta[0]
            try:
                if datos[0] == consulta[1] and datos[1] == consulta[2]:
                    msg.showinfo('Exito','Se ha logueado correctamente')
                    self.validacionsaldo(consulta[3])
                    self.login.destroy()
                    
                    
            except Exception:
                msg.showerror('Error','El usuario: '+ datos[0] + ' no existe en el sistema')
        except Exception:
            msg.showerror("Error","""
               1.Los campos de usuarios y contraseñas estan vacios
               2.Verifique su conexion a internet 
            """)

    def crearusuario(self):
        datos = (self.user.get(),self.password.get())
        consulta = self.bbdd.createuser(datos)
        if consulta:
           msg.showinfo('Informacion','Se ha creado la cuenta exitosamente') 
           self.registre.destroy()
    
    def add(self):
        self.info()
        webbrowser.open_new_tab('https://paypal.com')

    def validacionsaldo(self,saldo):
        if saldo in range(1,3) :
            msg.showwarning('Atencion',"Creditos Insuficientes en su cuenta")
        elif saldo <= 0:
             msg.showwarning('Atencion',"""
              Su cuenta no cuenta con saldo,
              Solo puede utilizar operaciones gratuitas
             """)

    def scan(self):
        
        adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
        #print(len(adb.devices()))
        if len(adb.devices()) == 0:
            msg.showwarning('Atencion','Habilite la Depuracion USB del telefono')
            adb.server_kill()
            return False
        for d in adb.track_devices():
            add = (d.serial)
            print(add)
            self.devices.append(add)
            self.check.pack_forget()
            time.sleep(3.0)
            self.select = OptionMenu(self.detalles,self.device,*self.devices)
            self.select.config(padx=20)
            self.select.pack(anchor=W,pady=20,padx=10)
            return False
        


      











   ### End Logica






    def setup(self):
        self.google.geometry(self.size)
        self.google.iconbitmap(self.icono)    
        self.google.title(self.titulo)
        self.google.resizable(0,0)
        self.google.config(bg=self.color)
        
    def loginmain(self):
        self.loginmenu = Frame(self.google,width=350,height=550)
        self.loginmenu.config(bg=self.color)
        self.loginmenu.pack(side=TOP,pady=5)
        img = Label(self.loginmenu,image=self.fondo1)
        img.pack(side=TOP)
        label1 = Label(self.loginmenu,text='GSM TOOL - IOSVANY ALVAREZ 2020')
        label1.config(bg=self.color)
        label1.pack(side=BOTTOM,pady=10)


    def mainmenu(self,saldo=""):
        self.menu = Menu(self.google)
        self.google.config(menu = self.menu)

        # Submenu Usuario
        usuariomenu = Menu(self.menu,tearoff = 0)
        usuariomenu.add_command(label='Login Usuario',command=self.usercenter)
        usuariomenu.add_separator()
        usuariomenu.add_command(label='Crear Usuario',command=self.registercenter)

        # Submenu Credito
        credito = Menu(self.menu,tearoff=0)
        credito.add_command(label=f'Saldo: {saldo}')
        credito.add_command(label='Add Creditos',command=self.add)
        

        # Submenu Operaciones
        operaciones = Menu(self.menu,tearoff=0)
        operaciones.add_command(label='Bypass MDM Google Pixel')
        operaciones.add_separator()
        operaciones.add_command(label='Unlock Permanent Google Pixel',command=self.unlockgoogle)
        operaciones.add_separator()
        operaciones.add_command(label='Huawei Fix Apn Cubacel')
        operaciones.add_separator()
        operaciones.add_command(label='Fix APN SIM CUBACEL (SOON)')

        #Menu
        self.menu.add_cascade(label='Usuario',menu=usuariomenu)
        self.menu.add_cascade(label='Creditos',menu=credito)
        self.menu.add_cascade(label='Operaciones',menu=operaciones)
        self.menu.add_cascade(label='Flasheo SO')
        self.menu.add_cascade(label='Backup & Restore')
        self.menu.add_command(label='Salir',command=self.google.quit)


    def unlockgoogle(self):
        self.loginmenu.pack_forget()
        self.usb = Frame(self.google,width=400,height=680)
        self.usb.config(bg="green")
        self.usb.pack(side=LEFT)
        # Imagen
        img = Label(self.usb,image=self.unlock)
        img.pack(side=LEFT)
        # LOG
        self.log = LabelFrame(self.google,width=320,height=340)
        self.log.config(bg='white')
        self.log.pack(side=BOTTOM)
        # Detalles
        self.detalles = Frame(self.google,width=320,height=340)
        self.detalles.config(bg=self.color)
        self.detalles.pack(side=TOP)
        titulo = Label(self.detalles,text="Instrucciones")
        titulo.config(bg=self.color)
        titulo.pack(anchor=W,pady=10)
        # Instrucciones
        instrucciones1 = Label(self.detalles,text='1. Hard Reset via RECOVERY without SIM')
        instrucciones2 = Label(self.detalles,text='2. Start Initial Configuration (WITHOUT INTERNET)')
        instrucciones3 = Label(self.detalles,text='3. Enable USB debugging')
        instrucciones4 = Label(self.detalles,text='4. Click boton SCAN DEVICES')
        instrucciones6 = Label(self.detalles,text='6. Click UNLOCK buttom before choosen you phone')
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
        self.check = Button(self.detalles,text='Scan Devices',command=self.scan)
        self.check.config(padx=10)
        self.check.pack(side=LEFT ,padx=10,pady=10)
        unlock = Button(self.detalles,text='Unlock')
        unlock.config(padx=20)
        unlock.pack(side=LEFT,padx=10)
        # Select
        




    def step2(self):
        self.usb.pack_forget()
        self.bypass = Frame(self.google,width=350,height=550)
        self.bypass.config(bg='green')
        self.bypass.pack(pady=20)


    # Form de Login y Registre

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


    def info(self):
        msg.askquestion('Informacion de Pago',"""
        Si desea realizar algun pago,debe?
         1. Escribir al siguiente numero por whatsapp 
            o telegram +5355112180
         2. El pago seria a travez de paypal a esta direccion:
            giounlocker91@gmail.com
         3. Despues de realizado el pago debe enviar el recibo 
            de la tranferencia
         4. Una vez hecho la transferencia sabiendo que 
            (1 crd = 2 USD) sera incrementado 
            automaticamente su credito en su cuenta

            Si esta de acuerdo, se procedera a redirigirle hacia 
            paypal.com       
        """)    



    def run(self):
        self.google.mainloop()





if __name__ == '__main__':
    newgoogle = Google()
    newgoogle.setup()
    newgoogle.mainmenu()
    newgoogle.loginmain()
    #newgoogle.step1()
    newgoogle.run()



        