import random
from ascii import *
import os
import sys

def main():
    print "sveiki atvyke i hangman'a!"

    file_obj = open("zodziu_sarasas.txt", "r")

    praeitas_ilgis = 0
    for zodis in file_obj.readlines():
        ilgiausias_zodis = len(zodis[:-1])
        if praeitas_ilgis < ilgiausias_zodis:
            praeitas_ilgis = ilgiausias_zodis

    lygis = 0
    while not int(lygis) in range(2, praeitas_ilgis+1): #kol lygis nera mums tinkamas - leidziami while loopa
        try:
            lygis = int(raw_input("ivesk lygi 2-{}   ".format(praeitas_ilgis)))
        except ValueError as e:
            print "ivesk skaiciu"

    gyvybes = 0
    while not int(gyvybes) in range(3, 7): #kol gyvybes nera mums tinkamos - leidziami while loopa
        gyvybes = input("pasirink kiek turesi gyvybiu: 3-6 ")  # choose a shift

    pak_img = 6 - gyvybes

    file_obj = open("zodziu_sarasas.txt", "r")  # galima kursoriu grazint i pradzia - google
    zodziu_sarasas = []

    for zodis in file_obj.readlines():
        zodzio_ilgis = len(zodis[:-1])
        if zodzio_ilgis <= lygis and zodzio_ilgis >= 2:
            zodziu_sarasas.append(zodis[:-1])  # pridedame zodi i sarasa

    zodis_atspek = random.choice(zodziu_sarasas).lower()
    pasleptas_zodis = "_" * (len(zodis_atspek))

    zodis_neatspetas = True

    while zodis_neatspetas: # while ciklas kuris spelioja ir atidengia raides

        print pasleptas_zodis
        print zodis_atspek

        if pasleptas_zodis == zodis_atspek: # patikrinti ar speta raide yra zodyje
            print "zodis atspetas! :)"
            break

        if gyvybes == 0:
            print "tave pakore :("
            break

        spejimas = raw_input("spek raide: ").lower()

        if spejimas in zodis_atspek:
            raides = list(zodis_atspek)
            for indexas, value in enumerate(raides):     # rasti spetos raides padeti
                if value == spejimas:
                    pasleptas_zodis_list = list(pasleptas_zodis)
                    pasleptas_zodis_list[indexas] = spejimas
                    pasleptas_zodis = "".join(pasleptas_zodis_list)     # atidengti raide
                    print "atspejai raide! :)"
                    print pasleptas_zodis

        else:
            print "neteisingai :( bandyk dar kart..."
            gyvybes -= 1
            pak_img += 1
            print ("gyvybes: " + str(gyvybes))
            print HANGMANPICS[pak_img]


    while True:
        answer = raw_input('kartoti? (y/n): ').lower()
        if answer in ('y', 'n'):
            if answer == 'y':
                main()

            else:
                print 'ate'
            break

main()
