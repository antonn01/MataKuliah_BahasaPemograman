def jualan():
    a = "capucino"
    b = "teh"
    c = "cincau"
    d = "kukubima"
    e = "thai tea"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3.", c)
    print ("4.", d)
    print ("5.", e)
    print ("6. Exit")

def capucino():
    capucino = "CAPUCINO"
    print(capucino)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    total = capucino*ppn
    print(total)

def teh():
    teh = "TEH MANIS"
    print(teh)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    total = teh*ppn
    print(total)

def cincau():
    cincau = "CINCAU"
    print(cincau)
    cincau = int(input("masukkan harga : "))
    ppn = 10/100
    total = cincau*ppn
    print(total)

def kukubima():
    kukubima = "KUKUBIMA"
    print(kukubima)
    kukubima = int(input("masukkan harga : "))
    ppn = 10/100
    total = kukubima*ppn
    print(total)

def thaitea():
    thaitea = "THAITEA"
    print(thaitea)
    thaitea = int(input("masukkan harga : "))
    ppn = 10/100
    total = thaitea*ppn
    print(total)

def welcome():
    nim = 1234567
    nama = "QWERTY"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        cincau()
    elif pil == 4:
        kukubima()
    elif pil == 5:
        thaitea()
        break
    else:
        print ("pilihan salah")