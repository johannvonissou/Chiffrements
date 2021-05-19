#!/bin/python3

class Cesar:
    def __valide(self, texte):
        textev = texte.upper().replace(" ", "")
        for c in textev:
            if ord(c) < 65 or ord(c) > 90:
                raise ValueError("La donnée doit contenir seulement des caractères valides (A-Za-z)!")
        return textev

    def chiffrer(self, texte):
        textev = self.__valide(texte)
        ctexte = str()
        for c in textev:
            ctexte += chr(65+((ord(c)+self.__cle-65)%26))
        return ctexte

    def dechiffrer(self, ctexte):
        textev = self.__valide(ctexte)
        texte = str()
        for c in textev:
            texte += chr(65+((ord(c)-self.__cle-65)%26))
        return texte

    def __init__(self, cle):
        self.__cle = cle