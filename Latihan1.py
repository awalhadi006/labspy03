import random

num = int(input("Masukkan nilai N : "))
for i in range(num):
    x = random.uniform(0, 0.5)
    print("data ke: {0} => {1}".format(i+1, x))
print("Selesai")
