#!/bin/python3

class Vigenere:
    def chiffrer(self, texte):
        textev = self.__valide(texte)
        ctexte = str()
        r = self.__rembourrage(textev)
        for i in range(len(textev)):
            ctexte += chr(((ord(textev[i])+ord(r[i])-65)%26)+65)
        return ctexte

    def dechiffrer(self, ctexte):
        textev = self.__valide(ctexte)
        texte = str()
        r = self.__rembourrage(textev)
        for i in range(len(textev)):
            texte += chr(((ord(textev[i])-ord(r[i])-65)%26)+65)
        return texte

    def __rembourrage(self, texte):
        return self.__cle*(len(texte)//len(self.__cle))+self.__cle[:len(texte)%len(self.__cle)]

    def __valide(self, texte):
        textev = texte.upper().replace(" ", "")
        for c in textev:
            if ord(c) < 65 or ord(c) > 90:
                raise ValueError("La donnée doit contenir seulement des caractères valides (A-Za-z)!")
        return textev

    def get_key(self):
        return self.__cle

    def __init__(self, cle):
        self.__cle = self.__valide(cle)
    