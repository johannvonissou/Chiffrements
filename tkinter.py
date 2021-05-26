#!/bin/python3

import tkinter
from vigenere import Vigenere
from rsa import RSA
from cesar import Cesar

root = tkinter.Tk()
root.title("RSA-César-Vigenère")
root.geometry("150x175")

def choix():
    globals()[lb.get(lb.curselection()).lower()]()

def vigenere():
    global texte
    global texte1
    texte = tkinter.Entry(root)
    texte.insert(0,"Texte")
    texte.pack()
    texte1 = tkinter.Entry(root)
    texte1.insert(0,"Cle")
    texte1.pack()
    buttonc = tkinter.Button(root, text = "chiffrer", command = vigenere_c)
    buttonc.pack()
    buttond = tkinter.Button(root, text = "déchiffrer", command = vigenere_d)
    buttond.pack()

def cesar():
    global texte
    global texte1
    texte = tkinter.Entry(root)
    texte.insert(0,"Texte")
    texte.pack()
    texte1 = tkinter.Entry(root)
    texte1.insert(0,"Cle")
    texte1.pack()
    buttonc = tkinter.Button(root, text = "chiffrer", command = cesar_c)
    buttonc.pack()
    buttond = tkinter.Button(root, text = "déchiffrer", command = cesar_d)
    buttond.pack()

def rsa():
    buttonc = tkinter.Button(root, text = "chiffrer", command = rsa_c)
    buttonc.pack()
    buttond = tkinter.Button(root, text = "déchiffrer", command = rsa_d)
    buttond.pack()

def vigenere_c():
    if texte1.get() != None:
        v = Vigenere(texte1.get())
        ct = v.chiffrer(texte.get())
        label = tkinter.Label(root, text = ct)
        label.pack()

def vigenere_d():
    if texte1.get() != None:
        v = Vigenere(texte1.get())
        t = v.dechiffrer(texte.get())
        label = tkinter.Label(root, text = t)
        label.pack()

def cesar_c():
    if texte.get() != None:
        c = Cesar(int(texte1.get()))
        t = c.chiffrer(texte.get())
        label = tkinter.Label(root, text = t)
        label.pack()

def cesar_d():
    if texte.get() != None:
        c = Cesar(int(texte1.get()))
        t = c.dechiffrer(texte.get())
        label = tkinter.Label(root, text = t)
        label.pack()

def rsa_c():
    global texte
    texte = tkinter.Entry(root)
    texte.insert(0,"Texte")
    texte.pack()
    button = tkinter.Button(root, text = "chiffrer", command = rsa_c_c)
    button.pack()


def rsa_c_c():
        c = RSA()
        c.get_clepri()
        c.get_clepub()
        t = c.chiffrer_chaine(texte.get())
        label = tkinter.Label(root, text = t)
        label.pack()

def rsa_d():
    global texte
    global texte1
    global texte2
    texte = tkinter.Entry(root)
    texte.insert(0,"Texte")
    texte.pack()
    texte1 = tkinter.Entry(root)
    texte1.insert(0,"Cle 1")
    texte1.pack()
    texte2 = tkinter.Entry(root)
    texte2.insert(0,"Cle 2")
    texte2.pack()
    button = tkinter.Button(root, text = "dechiffrer", command = rsa_d_d)
    button.pack()    

def rsa_d_d():
        r = RSA(keygen= False)
        r.set_clepri((int(texte1.get()),int(texte2.get())))
        t = r.dechiffrer_chaine(texte.get())
        label = tkinter.Label(root, text = t)
        label.pack()


lb = tkinter.Listbox(root, height=3, selectmode='SINGLE')
lb.insert(1,"Cesar")
lb.insert(2,"Vigenere")
lb.insert(3,"RSA")
lb.pack()

buttonchoix = tkinter.Button(root, text = "choisir", command = choix)
buttonchoix.pack()


root.mainloop()
