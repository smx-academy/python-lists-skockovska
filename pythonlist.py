#1.Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, da se dodadat vo list i da se soberat site broevi vo listata

"""listanabroevi = []
zbirnabroevi = 0
for i in range (10):
    broj = int (input("Vnesete broj:  "))
    listanabroevi.append(broj)
    zbirnabroevi+=broj
print("Listata na vneseni broevi e: {} " .format(listanabroevi) )
print("Zbirot na vnesenite broevi iznesuva {} " .format(zbirnabroevi))


#2.Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, da se dodadt vo lista i da se najde najgolemiot broj

listanabroevi = []
x= int (input ("Vnesete kolku broevi ke vnesete: "))
for i in range (x):
    a= int (input ("Vnesete go brojot "))
    listanabroevi.append(a)

print ("Listata na vneseni broevi e: " , listanabroevi)    
listanabroevi.sort(reverse=True) 
print ("Najgolemiot broj od listata e " ,listanabroevi [0])


#3. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, 
# da se ispecati listata i korisnikot da moze da izbere kolku elementi i koi elementi ke gi izbrise

listanabroevi = []
x= int (input ("Vnesete kolku broevi ke vnesete: "))
for i in range (x):
    a= int (input ("Vnesete go brojot "))
    listanabroevi.append(a)

print ("Listata na vneseni broevi e: " , listanabroevi) 
brisenje= int (input ("Koj element sakate da go izbrisete: "))
for i in range (brisenje):
    listanabroevi.remove (brisenje)

print ("Listata na broevi po izbrisanite podatoci e: " , listanabroevi) 


#4. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, da se dodadat vo lista, i da se najde najdolgoto ime

listanaiminja = []
x= int (input ("Vnesete kolku iminja ke vnesete: "))
for i in range (x):
    ime= input ("Vnesete go imeto ")
    listanaiminja.append(ime)
    

res = max(listanaiminja, key = len)
print ("Listata na vneseni iminja e: " , listanaiminja) 
print("Najdolgoto ime e : " + res) # ne mi dava tocni vrednosti, ja pecati prvata najdena vrednost od listata so najdolg string

 

#5. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi, da se dodadat vo lista i da se najde vtoriot najgolem broj

listanabroevi = []
x= int (input ("Vnesete kolku broevi ke vnesete: "))
for i in range (x):
    a= int (input ("Vnesete go brojot "))
    listanabroevi.append(a)

print ("Listata na vneseni broevi e: " , listanabroevi) 
listanabroevi.sort()
print ("Vtoriot najgolem element od listata e: " , listanabroevi[-2]) 
"""
#6. Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. Korisnikot da moze da vnesuva produkti se dodeka ne izbere deka saka da plati. 
# Produktitte da se dodavaat vo edna lista, cenite vo druga lista. Koga ke izbere deka saka da plati da mu se ispecatat produktite i cenite vo nalik na "fiskalna smetka".
#Da ima moznost korisnikot da plati i da se presmeta dali i kolku treba da mu se vrati kusur

produkti = []
smetka= []
zbir_produkti = 0
zbir_smetka = 0
while True:
    produkt = input("Vnesete produkt: ")
    cena = int (input ("Vnesete cena: "))
    produkti.append(produkt)
    smetka.append(cena)
    zbir_smetka+=cena
    zbir_produkti+=1
    plakanje = input ("Dali sakate da platite: ")
    if plakanje.lower () == "da":
        break
    else:
        pass

print ("Produktite vo vasata kosnicka se: ", produkti)
print ("Smetkata iznesuva: ", zbir_smetka)

plateno = int (input ("Vnesete kolku plakate: ")) 
kusur = plateno - zbir_smetka

if kusur > 0:
    print("Vi blagodarime na uplatata. Vasiot kusur iznesuva {} ".format(kusur))
else:
    print("Vasata suma {} ne e dovolna da ja platite smetkata".format(plateno))