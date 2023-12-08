#  ##### OPERATOR LOGIKA #####

# # a = 5
# # #AND
# # print(a<5 and a<10)

# # #OR
# # print(a<5 or a<10)

# # #NOT
# # print(not(a<5 and a<10)) 
# # print(not(a<5 or a<10))


#  ##### Condition/IF statement #####

a = 40
b = 30

if b > a:
    print("b lebih besar dari a")
elif a==b:
    print("a dan b sama")
else:
    print("a lebih besar dari b")

namaku = input("Masukan nama: ")

if namaku == "firah":
    print(f"Selamat Datang {namaku}") 
elif namaku == "kyungsoo":
    print(f"Hai abang {namaku}")
elif namaku != "firah":
    print(f"Kamu bukan {namaku}")
else:
    print("Nama tidak dikenal. Silahkan coba lagi")

### PYTHON TIPE SENSITIF. besar kecil huruf itu DIPERHITUNGKAN ###

## CONDITION BERSARANG (didalam if ada if)
nama = input("Masukan nama: ")
pekerjaan = input("Masukan pekerjaan: ")

if nama == "Firah":
    if pekerjaan == "QA":
        print(f"Selamat datang kembali {nama} di QA Team")
else:
    print("Nama tidak dikenal. Kamu bukan tim kami")
