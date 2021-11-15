a = int(input("Masukkan angka pertama :"))
b = int(input("Masukkan angka kedua :"))
c = int(input("Masukkan angka ketiga :"))

if a >= b >= c or a >= c >= b:
     print("Bilangan terbesar yaitu :",a)
if b >= a >= c or b >= c >= a:
     print("Bilangan terbesar yaitu :",b)
if c >= a >= b or c >= b >= a:
     print("Bilangan terbesar yaitu :",c)