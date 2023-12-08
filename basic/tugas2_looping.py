a = 1

while a < 31:
    cetak = ""
    if a%3 == 0:
        cetak = "dang"
    elif a%5 == 0:
        cetak = "dut"
    else:
        cetak = a
        
    if a%3 == 0 and a%5 == 0:
        cetak = "dut"
    print(a)
    a += 1