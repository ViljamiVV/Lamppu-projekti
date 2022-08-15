#! /usr/bin/python3
# -*- coding: utf-8 -*-

from serial import *
from datetime import *
import json
import time
import os 

JSON = "data.json"
def Tapahtuma(data):
    
    if len(data) == 2: 
        try:
            with open (JSON) as tiedosto:
                jsonSisalto = json.load(tiedosto)
                
        except json.decoder.JSONDecodeError:
            jsonSisalto = {}
            
        # jos tiedostoa ei ole, tee tyhjä tietokanta   
        except FileNotFoundError:
            jsonSisalto = {}
            open(JSON, "a").close()
            
            # oikeuksien vaihto jotta sitä pystytään lukemaan
            os.chmod(JSON, 0o755) 
           
        # jsonSisalto avain saa aikaleiman arvoksi 
        jsonSisalto["REF"] = int(time.time()) 
    
    
        lippu = 0
        for avain, arvo in jsonSisalto.items():
            # jos tällä avaimella löytyy tietue
            if avain == data: 
                jsonSisalto[avain] = jsonSisalto["REF"]
                lippu = 1 
        if lippu == 0:
            jsonSisalto[data] = jsonSisalto["REF"]
             
        try:
            with open (JSON, "w") as tiedosto:
                json.dump(jsonSisalto, tiedosto)
                
        except Exception:
            print("Virhe, tiedostoon ei voida kirjoittaa")
    
def sarjaportinKuuntelija():

    # luodaan sarjaporttisoketti ja varaudutaan virhetilanteeseen 
    try:
    # USB-sarjaportin tiedot on haettu minicom ohjelman tiedoista 
        microbitti = Serial(port = '/dev/ttyACM0', baudrate=115200, timeout = 2)
        
    except Exception:
        print("Tarkasta portti")
     
    while True:
        
        try:
        # välitetään luetut kaksi tavua ("aa"/"bb") Tapahtuma-funktiolle
            Tapahtuma(microbitti.read(2).decode())    
        except KeyboardInterrupt:
             print("Virhe, ohjelma keskeytetään")
             sys.exit()
             
if __name__ == "__main__":

    sarjaportinKuuntelija()

