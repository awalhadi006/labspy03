num = []
while num!=0:
    a = int(input("Masukkan bilangan : "))
    num.append(a)
    if a == 0:
        break
print("Nilai Terbesar adalah : ",max(num))