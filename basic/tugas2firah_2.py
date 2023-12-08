"""
tugas 2:

saya punya sederet angka dari 1 - 30

- tolong dicetak angka tersebut satu persatu
- tiap kelipatan 3, ganti angka jadi tulisan "dang"
- tiap kelipatan 5, ganti angka jadi "dut"
- tiap kelipatan 3 dan 5, ganti angka jadi "dangdut"

"""


b = 1


while b < 31:
    cetak = ""
     #ngecek kelipatan 3,5
    if b%3 == 0:
        cetak = "dang"
    elif b%5 == 0:
        cetak = "dut"
    else:
        cetak = b

    #ngecek kelipatan 3 dan 5
    if b%3 == 0 and b%5 == 0:
        cetak = "dangdut"
    print(cetak)
    b += 1
