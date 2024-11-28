"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tadeáš Bartoš
email: bartos.tadeas@live.com
github: TadeasBoomer
"""

import sys
import re
from collections import Counter
import string

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

uzivatel_jmeno = input("Zadej své jméno: ")
if uzivatel_jmeno not in uzivatele:
    print("Uživatel nenalezen, program se ukončí.")
    sys.exit()

uzivatel_heslo = input("Zadej své heslo: ")

if uzivatele[uzivatel_jmeno] == uzivatel_heslo:
    print("Přihlášení bylo úspěšné!")
else:
    print("Nesprávné heslo, program se ukončí.")
    sys.exit()

try:
    uzivatel_vstup = int(input("Jsou k dispozici 3 texty, jaký si přeješ analyzovat? (zadej číslo 1, 2 nebo 3): "))
    
    if uzivatel_vstup < 1 or uzivatel_vstup > 3:
        print("Zadané číslo není v rozsahu 1-3, program se ukončí.")
        sys.exit()

    vybrany_text = TEXTS[uzivatel_vstup - 1]

    slova = vybrany_text.split()

    slova_velke_pismeno = len([slovo for slovo in slova if slovo.istitle()])
    slova_velkymi = len([slovo for slovo in slova if slovo.isupper()])
    slova_malymi = len([slovo for slovo in slova if slovo.islower()])
    cisla = [int(cislo) for cislo in re.findall(r'\b\d+\b', vybrany_text)]

    print("V tebou vybraném textu je: ")
    print(len(vybrany_text.split()), "slov,")
    print("z toho ", slova_velke_pismeno, "začíná velkým písmenem,")
    print(slova_velkymi, "je psáno velkým písmem,")
    print(slova_malymi, "je psáno malým písmem,")
    print(len(cisla), "jsou čísla a jejich součet je: ", sum(cisla))

    #delky_slov = [len(slovo) for slovo in slova]
    delky_slov = [len(''.join(char for char in slovo if char.isalnum())) for slovo in slova]
    cetnost_delky = Counter(delky_slov)
    print("Četnost délek slov v textu:")
    for delka, cetnost in sorted(cetnost_delky.items()):
        print(f"{delka:2}| {'*' * cetnost} {cetnost}")

except ValueError:
    print("Nezadal jsi číslo, program se ukončí.")
    sys.exit()