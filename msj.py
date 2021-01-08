from tkinter import messagebox as msg




class Mensajes:

        ### START MENSAJE
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

    # Inicio bloque de mensajes correspondiente a la funcion UNLOCK
    def infosucces(self):
        msg.showinfo('Success', """
            Has been successfully unlocked.""")
        msg.showinfo('Information', """
            Please insert a SIM from your operator.
            In case the unlock is not performed successfully,
            Make Hard Reset and retry the procedure
        """)

    def infoerror(self):
        msg.showerror('Error', """
        Review the following instructions:
            1. Phone is connected to PC
            2. USB debugging is active
            3. Hard Reset to the phone WITHOUT SIM via (Recovery)               
        """)  

    def infoelse(self):
        msg.showerror('Error', """
          Review the following instructions:
            1. Phone is connected to PC
            2. USB debugging is active
            3. Hard Reset to the phone WITHOUT SIM via (Recovery)            
        """)
    #### END  MENSAJE
