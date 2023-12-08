prima = int(input("masukan bilangan: "))

if prima > 1:
    #cek bilangan prima
    for i in range(2,prima):
        if (prima % i) == 0:
            print(prima,"bukan bilangan prima")
            print(i, "times", prima//i, "is", prima)
            break
    else:
        print(prima, "adalah bilangan prima")
else:
    print(prima, "bukan bilangan prima")