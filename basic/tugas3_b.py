a = 1
prime = int(input("masukan bilangan prima : "))
flag = False

while a < prime:
    
    if prime == 1:
        print(prime, "bukan bilangan prima")
    elif prime > 1:
        #cek faktor
        for i in range(2, prime):
            if (prime % i) == 0:
            #kalo faktor ketemu, set flag = True
                flag = True
                break
        
        #cek kalo flag = True
        if flag:
            print(prime, "bukan bilangan prima")
        else:
            print(prime, "adalah bilangan prima")
        a += 1