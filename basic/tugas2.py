'''
tugas 2:

saya punya sederet angka dari 1 - 30

- tolong dicetak angka tersebut satu persatu
- tiap kelipatan 3, ganti angka jadi tulisan "dang"
- tiap kelipatan 5, ganti angka jadi "dut"
- tiap kelipatan 3 dan 5, ganti angka jadi "dangdut"

output:
1
2
dang
4
dut
dang
7
8
dang
dut
.
.
.
.
30
'''

for i in range(1,31):

    if i%3 == 0 and i%5 == 0:
        print("exo")
    elif i%3 == 0:
        print("cbx")
    elif i%5 == 0:
        print("sc")
    else:
        print(i)
        

#kalo diatas udah memenuhi syarat, maka kondisi selanjutnya akan dilupakan