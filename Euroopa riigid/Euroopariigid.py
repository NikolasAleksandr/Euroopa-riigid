﻿from random import *

def failist_to_dict(f:str):
    riik_pealinn={}#sõnastik {"Riik":"Pealinn"}
    pealinn_riik={}#sõnastik {"Pealinn":"Riik"}
    riigid=[] #järjend, kus talletakse riigide nimetused
    file=open(f,'r',encoding="utf-8-sig")
    
    for line in file:
        k,v=line.strip().split('-') #k-võti, v-väärtus
        riik_pealinn[k]=v #täidame riik_pealinn
        pealinn_riik[v]=k #täidame pealinn_riik
        riigid.append(k)
    file.close()
    
    return riik_pealinn,pealinn_riik,riigid

#käivitame loodud funktsioon
riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")

def lisa_sõnastikku(sõnastik, võti, väärtus):
    sõnastik[võti] = väärtus
    return f"{võti} on lisatud sõnastikku. Nüüd on tema väärtus {väärtus}."

def muuda_sõnastikku(sõnastik, võti, väärtus):
    sõnastik[võti] = väärtus
    return f"{võti} on muudetud. Nüüd on tema väärtus {väärtus}."

def kuva_pealinna_või_riik(sõnastik, sisend_tekst):
    sisend_tekst = sisend_tekst.capitalize()

    if sisend_tekst in sõnastik:
        return f"{sisend_tekst} pealinn: {sõnastik[sisend_tekst]}"
    
    for riik, pealinn in sõnastik.items():
        if pealinn == sisend_tekst:
            return f"Riik pealinnaga {sisend_tekst}: {riik}"

    lisa_valik = input(f"{sisend_tekst} puudub sõnastikust. Kas soovite lisada? (Jah/Ei): ")
    if lisa_valik.lower() == "jah":
        uus_väärtus = input(f"Sisestage {sisend_tekst} pealinn või riik: ")
        return lisa_sõnastikku(sõnastik, sisend_tekst, uus_väärtus)
    else:
        muuda_valik = input(f"{sisend_tekst} puudub sõnastikust. Kas soovite seda muuta? (Jah/Ei): ")
        if muuda_valik.lower() == "jah":
            uus_väärtus = input(f"Sisestage uus väärtus {sisend_tekst} pealinnale või riigile: ")
            return muuda_sõnastikku(sõnastik, sisend_tekst, uus_väärtus)
        else:
            return "Tegevus tühistatud."
        

def õige_vastus(antud_vastus, oodatav_vastus):
    return antud_vastus.lower() == oodatav_vastus.lower()

def testi_teadmised(sõnastik):
    õiged_vastused = 0
    küsimused = 0
    
    for _ in range(6):  
        suvaline_sõna = choice(list(sõnastik.keys()))
        õige_väärtus = sõnastik[suvaline_sõna]
        küsimus = input(f"Mis on pealinn riigile '{suvaline_sõna}'? ")

        if õige_vastus(küsimus, õige_väärtus):
            print("Õige!")
            õiged_vastused += 1
        else:
            print("Vale!")
        küsimused += 1
    
    protsent = õiged_vastused / küsimused * 100
    return protsent

kasutaja_sisend = input("Sisestage riigi või pealinna nimi: ")
tulemus = kuva_pealinna_või_riik(riik_pealinn, kasutaja_sisend)
print(tulemus)

soov_testida = input("Kas soovite kontrollida oma teadmisi? (Jah/Ei): ")
if soov_testida.lower() == "jah":
    tulemus_protsent = testi_teadmised(riik_pealinn)
    print(f"Teie tulemus: {tulemus_protsent}% õigetest vastustest.")



