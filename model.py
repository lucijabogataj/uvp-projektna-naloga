import random
import time
import os

PLUS, MINUS, KRAT = 'plus', 'minus', 'krat'
NASLOV = 'VESELO RAČUNANJE'
NAPAKA = 'Odgovor {} pa ni pravilen. Poskusi znova!'
ZAKLJUCEK = 'Čestitam! Rešil si vseh {} računov v {} sekundah.'

STEVILO_RACUNOV = 10

class Racun:

    def __init__(self, operacija):
        self.operacija = operacija

    def razpon_a(self):
        if self.operacija == PLUS:
            return (0, 100)
        elif self.operacija == MINUS:
            return (1, 100)
        elif self.operacija == KRAT:
            return (0, 11)

    def razpon_b(self):
        if self.operacija == PLUS:
            return (0, 100 - self.a)
        elif self.operacija == MINUS:
            return (1, self.a)
        elif self.operacija == KRAT:
            return (0, 11)

    def znak(self):
        if self.operacija == PLUS:
            return '+'
        elif self.operacija == MINUS:
            return '-'
        elif self.operacija == KRAT:
            return '*'

    def izberi_a(self):
        self.a = random.randrange(*self.razpon_a())

    def izberi_b(self):
        self.b = random.randrange(*self.razpon_b())

    def kompozitum(self):
        if self.operacija == PLUS:
            return self.a + self.b
        elif self.operacija == MINUS:
            return self.a - self.b
        elif self.operacija == KRAT:
            return self.a * self.b

class Naloga:

    def __init__(self):
        self.porabljen_cas = 0

    def odstej_zacetni_cas(self):
        self.porabljen_cas -= time.time()

    def pristej_koncni_cas(self):
        self.porabljen_cas += time.time()

    def ustvari_racun(self, operacija):
        self.racun = Racun(operacija)
        self.racun.izberi_a()
        self.racun.izberi_b()
        a = self.racun.a
        b = self.racun.b
        self.izpis = str(a) + ' ' + self.racun.znak() + ' ' + str(b) + ' = '

    def obdelaj_rezultat(self):
        self.rezultat = round(self.porabljen_cas)
        if self.racun.operacija == PLUS:
            stevilka_vrstice = 0
        elif self.racun.operacija == MINUS:
            stevilka_vrstice = 1
        elif self.racun.operacija == KRAT:
            stevilka_vrstice = 2
        self.seznam = preberi_datoteko()
        if self.seznam[stevilka_vrstice] == '0' or \
           int(self.seznam[stevilka_vrstice]) > self.rezultat:
            self.seznam[stevilka_vrstice] = self.rezultat
        with open('rezultatki.txt', 'w') as datoteka:
            for x in self.seznam:
                print(x, file=datoteka)

def preberi_datoteko():
    seznam = []
    with open('rezultatki.txt') as datoteka:
        for stevilo in datoteka:
            seznam.append(stevilo[:-1])
        return(seznam)

def naredi_datoteko():
    if os.path.isfile('./rezultatki.txt') == False:
        with open('rezultatki.txt', 'w') as datoteka:
            print('0', file=datoteka)
            print('0', file=datoteka)
            print('0', file=datoteka)
