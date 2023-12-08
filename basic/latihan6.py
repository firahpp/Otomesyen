"""
        FUNCTION
"""
#### FUNCTION WITH ARGUMENT ####
def hai(nama): #nama disini adalah jenis argumen
    print("Annyeong " + nama + ". Bangawo!")
    
#hai("firah") #pemanggilan fungsi

def neng(nama):
    print(f"Hai Neng Geulis {nama} mau kemana?")
#neng("Putri")

#### FUNCTION WITHOUT ARGUMENT ####
def exo():
    print("EXO WE ARE ONE ")
    print("Saranghaja")
#exo()

def ngitung(x,y): #position argument 
    z = x + y
    return z #return : mengembalikan nilai z hasil ngitung
hasil = ngitung(2,3)
#print(hasil)

# c = hasil + 20
# print(c)

def kenalan(nama, hobby):
    print(f"Halo nama aku {nama}, hobby aku adalah {hobby}")
    
# kenalan("firah","fangirling")

def tetangga(nama, *pekerjaan): # arbitary argument  # PEKERJAAN bentuknya tuple
   if pekerjaan == ():
       kerjaan = "tidak ada"
   elif pekerjaan != ():
        kerjaan = pekerjaan[0]
        print(f"Halo nama saya {nama}, dan pekerjaan saya {kerjaan}")

#tetangga("lastri")  

   # output : Halo nama saya lastri, dan pekerjaan saya tidak ada
    
def kenalan3(nama="lastri", pekerjaan="serabutan"):
    print(f"halo nama saya {nama}, pekerjaan saya {pekerjaan}")
    
# kenalan3("JAJANG", "OB") #output nya menggantikan hardcore 
# kenalan3(pekerjaan="pembantu")
