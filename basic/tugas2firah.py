"""
tugas 2:

saya punya sederet angka dari 1 - 30

- tolong dicetak angka tersebut satu persatu
- tiap kelipatan 3, ganti angka jadi tulisan "dang"
- tiap kelipatan 5, ganti angka jadi "dut"
- tiap kelipatan 3 dan 5, ganti angka jadi "dangdut"

"""

a = 0
b = 1


while b < 31:
   
    if b%3 == 0:
         print("dang")
         
    elif b%5 == 0:
         print("dut")
         
    else:
          print(b)
    
    
    if b%3 == 0 and b%5 == 0:
        print("dangdut")    
    b += 1


