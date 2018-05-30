# wuerfel.py

# 100 mal würfel simulieren
#anzahl von 1 2 3 4 5 6 ausgeben

# Eingabe
eingabe = int(input("Wie oft soll gewürfelt werden "))
anz = input
# Variablen
eins = 0
zwei = 0
drei = 0
vier = 0
fuenf = 0
sechs = 0

# Zufallszahl
from random import *

# Schleifen
for i in range(0, eingabe):
  
    wuerfel = randint(1,6)
    if(wuerfel == 1):
        eins+=1
    if(wuerfel == 2):
        zwei+=1
    if(wuerfel == 3):
        drei+=1
    if(wuerfel == 4):
        vier+=1
    if(wuerfel == 5):
        fuenf+=1
    if(wuerfel == 6):
        sechs+=1

# Ausgabe
print(" ")
print("Eins" , eins ,"Zwei" , zwei , "Drei" , drei , "Vier" , vier , "Fünf" , fuenf , "Sechs",sechs)