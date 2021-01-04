from mysql.connector import errorcode
import mysql.connector
from tkinter import messagebox as msg


class BBDD:


    def conexionbbdd(self):
        # Conexion a la BBDD al principio de la funcion para conocer si hay internet
        try:
            self.cnx = mysql.connector.connect(
                host='sql3.freemysqlhosting.net',
                username='sql3384063',
                password='dxRKvLXzJT',
                database='sql3384063',
                port='3306')
            self.conexion = self.cnx.cursor()
            #print('exito')
            self.cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                msg.showerror('Error','Por favor verique su conexion a internet')
        else:
            self.cnx.close()
        


    def createuser(self,data=""):
        # Funcion de crear usuarios
        try:
            sql = 'INSERT INTO user VALUES(null,%s,%s,null)'
            self.cnx = mysql.connector.connect(
                host='sql3.freemysqlhosting.net',
                username='sql3384063',
                password='dxRKvLXzJT',
                database='sql3384063',
                port='3306')
            self.conexion = self.cnx.cursor()
            self.conexion.execute(sql,data)
            self.cnx.commit()
            return [self.conexion.rowcount]
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                msg.showerror(f'Error','El usuario esta registrado en el sistema')      


    def loginusuario(self,data=""):
        sql = ("SELECT * FROM user WHERE username = %s AND password = %s")
        self.cnx = mysql.connector.connect(
            host='sql3.freemysqlhosting.net',
            username='sql3384063',
            password='dxRKvLXzJT',
            database='sql3384063',
            port='3306')
        self.conexion = self.cnx.cursor()
        self.conexion.execute(sql,data)
        result = self.conexion.fetchone()
        return result      
  

    def promoinfo(self):
        # Metodo para establecer desde la BBDD mensajes y promociones e info
        sql = ("SELECT * FROM info")
        self.cnx = mysql.connector.connect(
            host='sql3.freemysqlhosting.net',
            username='sql3384063',
            password='dxRKvLXzJT',
            database='sql3384063',
            port='3306')
        self.conexion = self.cnx.cursor()
        self.conexion.execute(sql)
        promo = self.conexion.fetchall()
        #print(promo)
        if len(promo) >= 1:
            for x in promo:
                if x[1] == 1:
                    msg.showinfo('Informacion',x[2])
                if x[1] == 2:
                    msg.showwarning('Informacion',x[2])    
        else:
            return False

    def checkcredits(self,data):
        ### Checkear  creditos
        sql = ("SELECT * FROM user WHERE username = %s")
        self.cnx = mysql.connector.connect(
            host='sql3.freemysqlhosting.net',
            username='sql3384063',
            password='dxRKvLXzJT',
            database='sql3384063',
            port='3306')
        self.conexion = self.cnx.cursor()
        self.conexion.execute(sql,data)
        credit = self.conexion.fetchone()
        return credit 