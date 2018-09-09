import tkinter as tk
import model

class Igra:

    def __init__(self, okno):
        self.okno = okno
        model.naredi_datoteko()
        self.prikazi_meni()

    def prikazi_meni(self):
        self.zgoraj = tk.Frame(self.okno)
        self.spodaj = tk.Frame(self.okno)
        zgoraj = self.zgoraj
        spodaj = self.spodaj
        zgoraj.pack()
        spodaj.pack()
        tk.Label(zgoraj, text=model.NASLOV).pack()
        levo = tk.Frame(spodaj)
        self.desno = tk.Frame(spodaj)
        levo.grid(row=0, column=0)
        self.desno.grid(row=0, column=1)
        tk.Label(spodaj, text='Izberi igro:').grid(row=0, column=0)
        tk.Button(spodaj, text='Seštevanje', \
                  command=self.nastavi_plus).grid(row=1, column=0)
        tk.Button(spodaj, text='Odštevanje', \
                  command=self.nastavi_minus).grid(row=2, column=0)
        tk.Button(spodaj, text='Poštevanka', \
                  command=self.nastavi_krat).grid(row=3, column=0)
        tk.Label(spodaj, \
                 text='Najboljši dosežek do sedaj:').grid(row=0, column=1)
        self.izpisi_dosezke()

    def izpisi_dosezke(self):
        i = 1
        for x in model.preberi_datoteko():
            if x == '0':
                tk.Label(self.spodaj, text='/').grid(row=i, column=1)
            else:
                tk.Label(self.spodaj, \
                         text='{} s'.format(x)).grid(row=i, column=1)
            i += 1

    def nastavi_plus(self):
        self.operacija = model.PLUS
        self.zacni_igro()

    def nastavi_minus(self):
        self.operacija = model.MINUS
        self.zacni_igro()
        
    def nastavi_krat(self):
        self.operacija = model.KRAT
        self.zacni_igro()

    def zacni_igro(self):
        self.naloga = model.Naloga()
        self.i = 0
        self.naloga.odstej_zacetni_cas()
        self.preveri_stevilo_racunov()

    def preveri_stevilo_racunov(self):
        if self.i < model.STEVILO_RACUNOV:
            self.i += model.STEVILO_RACUNOV
            self.naredi_korak()
        else:
            self.naloga.pristej_koncni_cas()
            self.cestitaj()
            
    def naredi_korak(self):
        self.spodaj.pack_forget()
        self.spodaj1 = tk.Frame(self.okno)
        self.spodaj1.pack()
        self.naloga.ustvari_racun(self.operacija)
        self.navodilo = 'Izračunaj:'
        self.izpisi_nalogo(self.navodilo)

    def izpisi_nalogo(self, navodilo):
        self.vrstica_z_navodilom = tk.Label(self.spodaj1, text=navodilo)
        self.vrstica_z_navodilom.pack()
        izpisan_racun = tk.Label(self.spodaj1, text=self.naloga.izpis)
        self.spr = tk.StringVar(self.okno) 
        vnosno_polje = tk.Entry(self.spodaj1, textvariable=self.spr)
        izpisan_racun.pack()
        vnosno_polje.pack()
        vnosno_polje.focus_set()
        oddaj = tk.Button(self.spodaj1, text='Oddaj', command=self.preveri)
        oddaj.pack()
        #self.spodaj1.bind('<Return>', self.preveri)
        #Rada bi, da se self.preveri zgodi ob pritisku na tipko enter. 

    def preveri(self, event=None):
        self.preveri_vnos(self.spr.get())

    def preveri_vnos(self, vnos):
        if vnos != str(self.naloga.racun.kompozitum()):
            self.spodaj1.pack_forget()
            navodilo = model.NAPAKA.format(vnos)
            self.spodaj1 = tk.Frame(self.okno)
            self.spodaj1.pack()
            self.izpisi_nalogo(navodilo)
        else:
            self.spodaj1.pack_forget()
            self.i += 1
            self.i -= model.STEVILO_RACUNOV
            self.preveri_stevilo_racunov()
            
    def cestitaj(self):        
        self.spodaj1.pack_forget()
        self.spodaj = tk.Frame(okno)
        self.naloga.obdelaj_rezultat()
        self.spodaj.pack()
        tk.Label(self.spodaj, \
                 text=model.ZAKLJUCEK.format(model.STEVILO_RACUNOV, \
                                             self.naloga.rezultat)).pack()
        tk.Button(self.spodaj, \
                  text='Nova igra', command=self.spet_prikazi_meni).pack()

    def spet_prikazi_meni(self):
        self.zgoraj.pack_forget()
        self.spodaj.pack_forget()
        self.prikazi_meni()
        

okno = tk.Tk()
moj_program = Igra(okno)
okno.mainloop()
