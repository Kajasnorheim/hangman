#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:30:41 2019

Navn på gruppemedlemmer: 
Michelle Paulsen Kårbø, Marte Marheim, Kaja Sofie Norheim

@author: kaja
"""

import random #random

def start(): #starte programmet
    navn = input("Hva heter du? ") #skrive inn navnet
    print("Velkommen til Hangman, ", navn) #printe ut velkommen, pluss navnet som er typet inn
    hangman()#starte hangman
    print()

def hangman(): #starte hangman
    ord = random.choice(["løve", "vindu", "datamaskin", "katt", "sitron"]) #velg et random ord fra listen "ord"
    
    gyldigeBokstaver = "abcdefghijklmnopqrstuvwxyzæøå" #bokstavene man kan bruke
    
    sjanser = 10 #10 sjanser til å gjette bokstav, hvis ikke avsluttes programmet
    ordLagret = '' #bokstaven som er gjettet fylles inn her
    
    while len(ord) > 0:  #mens lengden av ordet er større enn 0. så er riktig bokstav tom. 
        riktigBokstav = '' #er ingenting
        
        
        for bokstav in ord:
            if bokstav in ordLagret: #hvis bokstaven er i ordLagret
                riktigBokstav = riktigBokstav + bokstav #ingenting = ingenting + den riktige bokstaven du gjettet
            else:
                riktigBokstav = riktigBokstav + "_" + " " #ingenting = ingenting +  stripket linje
               
                
        if riktigBokstav == ord: #hvis bokstaven du gjettet er lik et av ordene i lista.
            print(riktigBokstav) #skriv ut bokstaven som er typet inn
            print("Du gjettet riktig! Ordet var: ",ord) #det var riktig ord til slutt. 
            break
        
        print("Hvilket ord er dette:", riktigBokstav)  #hvilket ord er dette: det som er typet inn
        gjett = input("Gjett en bokstav: ") #gjette bokstavene
        
        if gjett in gyldigeBokstaver: #hvis bokstaven du setter inn i gjett er blandt de gyldige bokstavene
            ordLagret = ordLagret + gjett # bokstaven som er gjettet = bokstaven som er gjettet + bokstaven som er skrevet inn. input
        else:
            print("Du kan bare taste inn en bokstav: ") #Hvis du taster inn flere eller variabel som ikke er riktig. print dette
            
            gjett = input() #input skrive inn tallet. 
            
        if gjett not in ord: #hvis bokstaevn som er skrevet inn ikke er i ordene på listen
            if gjett not in ord:
                sjanser = sjanser - 1 #antall gjett = antall gjett -1. 
                if sjanser == 0: #hvis sjansen er lik 0 har du brukt opp alle sjansene
                    print("Du klarte ikke å gjette ordet:", ord)
                    break

start() #slutte "start"programmet