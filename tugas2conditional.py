a = int(input("Masukkan angka pertama :"))
b = int(input("Masukkan angka kedua :"))
c = int(input("Masukkan angka ketiga :"))

print("Program mengurutkan data")
print("Bilangan ke-1 :", a)
print("Bilangan ke-2 :", b)
print("Bilangan ke-3 :", c)

if a <= b <= c :
     print("Urutan bilangan :",a, b, c)
elif a <= c <= b :
     print("Urutan bilangan :",a, c, b)
elif b <= a <= c :
     print("Urutan bilangan :",b, a, c)
elif b <= c <= a :
     print("Urutan bilangan :",b, c, a)
elif c <= a <= b :
     print("Urutan bilangan :",c, a, b)
else :
     print("Urutan bilangan :",c, b, a)