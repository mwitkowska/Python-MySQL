#-*-coding:utf-8-*-
import pymysql.cursors  

class Hotel:
    def __init__ (self):
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',                             
                             db='hotel')
        self.cur=self.db.cursor()
        
        while(True):
            status=input("Czy chcesz się zalogować jako administrator czy jako użytkownik? \nNaciśnij A lub U. \nŻeby wyjść, naciśnij Q: \n")
            if(status.upper()=="A"):
                print(self.admin())
            elif(status.upper()=="U"):  
                print(self.user())
            elif(status.upper()=="Q"):
                print("Do widzenia")
                self.db.close()
                break
            else:
                print("Podałeś nieprawidłową literę")
                
    
    def admin(self):
        logA=str(input("Podaj login: "))
        passA=str(input("Podaj hasło: "))
        self.cur.execute('select count(*) from logowanie_admin where login_admin="%s" and haslo_admin="%s";' %(logA, passA))      
        dbuser = self.cur.fetchall()
        if dbuser[0][0]:
            print("Zalogowano jako admin")
        else:
            print("Logowanie nie powiodło się")
            #admin(self) jak zrobić, żeby wróciło do logowania admina?
            
                                    
    def user(self):
        logU=str(input("Podaj login: "))
        passU=str(input("Podaj hasło: "))
        self.cur.execute('select count(*) from logowanie_goscia where login_goscia="%s" and haslo_goscia="%s";' %(logU, passU))      
        dbuser = self.cur.fetchall()
        if dbuser[0][0]:
            return "Zalogowano jako user"
        else:
            return "Logowanie nie powiodło się"

                                                 
hotel=Hotel()
                                


   

