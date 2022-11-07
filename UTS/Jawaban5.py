print ("NIM  : 1234567")
print ("NAMA : QWERTY")

def Capucino():
    cap ="memilih capucino"
    print(cap)
    capucino = int(input("masukan harga : "))
    ppn = capucino * 10/100
    total = capucino+ppn
    print("Jumlah yang harus di bayarkan",total)

def Teh():
    t ="memilih Teh"
    print(t)
    Teh = int(input("masukan harga : "))
    ppn = Teh * 10/100
    total = Teh+ppn
    print("Jumlah yang harus di bayarkan",total)

def pilihan():
    print ("NIM  : 20210801242")
    print ("NAMA : Anton Nurfendi") 
    print("1. capucino")
    print("2. teh")
    print("3. Exit")
  

while True:
    pilihan()
    pil=int(input("pilihan : "))
    if pil==1:
        Capucino()
    elif pil==2:
        Teh()
    else :
        break