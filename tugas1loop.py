from random import random
import random

jumlah = int(input("Masukkan nilai N :"))
for i in range(jumlah):
 a = random.uniform(0.0, 0.5)
 print(f"Data ke-{i+1}", a)
print("Selesai")