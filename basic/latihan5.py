# LOOPS

#===== while loop =====#

x = 0

while x < 5:
    print(x) #akan terus melooping sampai satu kondisi terpenuhi
    x += 1 # untuk memotong looping menjadi sebanyak yg diinginkan while

## infinite loop

i = 1
# while i < 5: atau pake :
while True:
    print("EXO CONCERT 2025")


#===== for loop =====#

exo_cbx = ['chen', 'baekhyun', 'xiumin']
for exo in exo_cbx:
    print(f"We are One {exo} saranghaja!")

# iterasi string pake for loop
namaku = "firah"
for eja in namaku:
    print(eja)

# # for range
# for i in range(5):
#     print(i)

c = 0

while c < 100:
  print(c)
  c = c + 3