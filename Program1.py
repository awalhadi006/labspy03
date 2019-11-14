modal = 100000000
sum = 0
y = 0
laba = [int(0), int(0), int(modal)*.1, int(modal)*.1, int(modal)*.5, int(modal)*.5, int(modal)*.5, int(modal)*.2]
for i in laba:
    sum = sum+i
    y+=1
    print("Laba Bulan Ke-",y, "sebesar", i)
print("Total Laba adalah: ",sum)