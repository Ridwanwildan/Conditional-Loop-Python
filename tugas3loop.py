modal = 100000000
for i in range(9):
 if (i>=1 and i<=2):
     print(f"Laba bulan ke-{i} sebesar :",modal*0)
 elif (i>=3 and i<=4):
     print(f"Laba bulan ke-{i} sebesar :",modal*0.1)
 elif (i>=5 and i<=7):
     print(f"Laba bulan ke-{i} sebesar :",modal*0.5)
 elif (i==8):
     print(f"Laba bulan ke-{i} sebesar :",modal*0.2)
total = (((modal*0)*2)+((modal*0.1)*2)+((modal*0.5)*3)+((modal*0.2)*1))
print("Total laba adalah :", total)
