
import kivy
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

#Cryptography
from cryptography.fernet import Fernet
import os






key = b'vkL9L8qaC6dYExg4SlBrgoTzWCkTzsndvh2yONHlEak='




def Encrypt(file_name):
    lock = Fernet(key)
    with open(file_name , 'rb') as file:
        data = file.read()
    criptografar = lock.encrypt(data)
    with open(file_name , 'wb') as file:
        file.write(criptografar)

def Decrypt(file_name):
    unlock= Fernet(key)
    with open(file_name , 'rb') as file:
        data = file.read()
    decoded = unlock.decrypt(data)
    with open(file_name , 'wb') as file:
        file.write(decoded)




# teste






class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class MainApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"







    def encrypt(self):

        Ftext = open("texto35gjo85458968573.txt", 'a')
        ms = self.root.ids.Sc1Text.text
        Ftext.write(ms)
        Ftext.close()


        arquivos = os.listdir()
        Files=list()


        for File in arquivos:
            if File.endswith('.txt'):
                Files.append(File)


        function = Encrypt

        for File in Files:
            function(File)


        #text label print e copy text

        A = open("texto35gjo85458968573.txt",'r')
        for N in A:
             N = N.rstrip()


        self.root.ids.Sc1Label.text = N
        self.root.ids.Sc2Label.text = ""

        A.close()

        #text label print e copy text

        os.remove("texto35gjo85458968573.txt")




    #lembrar terminar
    def decrypt(self):

        Ftext1 = open("texto35gjo8545896cyrsiw8573.txt", 'a')
        ms1 = self.root.ids.Sc1Text1.text
        Ftext1.write(ms1)
        Ftext1.close()

        arquivos = os.listdir()
        Files=list()


        for File in arquivos:
            if File.endswith('.txt'):
                Files.append(File)


        function = Decrypt

        for File in Files:
            function(File)


        A1 = open("texto35gjo8545896cyrsiw8573.txt",'r')
        for N1 in A1:
            N1 = N1.rstrip()


        self.root.ids.Sc1Label1.text = N1
        self.root.ids.Sc2Label1.text = ""

        A1.close()

        os.remove("texto35gjo8545896cyrsiw8573.txt")







MainApp().run()
