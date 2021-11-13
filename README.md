 # Latihan membuat conditional dan loop python   

* Nama          : Hizbullah Ridwan
* NIM           : 312110055
* Kelas         : TI.21.C.1
* Mata Kuliah   : Bahasa Pemrograman
----------------------------------
Dalam latihan membuat conditional dan loop [python](https://www.python.org/) ini, saya menggunakan [visual studio code](https://code.visualstudio.com/) sebagai teks editornya.     

1. **Conditional**     
   * [Membuat program menentukan nilai akhir](https://github.com/Ridwanwildan/Conditional-Loop-Python#mebuaed)         
   * [Membuat program menampilkan status gaji karyawan](https://code.visualstudio.com/)    
   * [Penggunaan kondisi OR](https://code.visualstudio.com/)      
   * [Tugas praktikum 2](https://code.visualstudio.com/)      
   * [Tugas 1: Menentukan dua bilangan terbesar](https://code.visualstudio.com/)      
   * [Tugas 2: Mengurutkan data dari data terkecil](https://code.visualstudio.com/)       
   * [Tugas 3: Program nested](https://code.visualstudio.com/)              

2. **Loop**
   * [Tugas 1: Menampilkan n bilangan acak yang lebih kecil dari 0.5](https://code.visualstudio.com/)       
   * [Tugas 2: Menampilkan bilangan terbesar dari n data yang diinput](https://code.visualstudio.com/)    
   * [Tugas 3: Menghitung laba](https://code.visualstudio.com/)      
  
## Membuat program menentukan nilai akhir   

```bash
nama = input("Masukkan nama:")
uts = input("Masukkan nilai UTS:")
uas = input("Masukkan nilai UAS:")
tugas = input("Masukkan nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
if akhir > 80:
 huruf = "A"
elif akhir > 70:
 huruf = "B"
elif akhir > 50:
 huruf = "C"
elif akhir > 40:
 huruf = "D"
else:
 huruf = "E"
print("\nNama :",nama)
print("Nilai UTS :",uts)
print("Nilai UAS :",uas)
print("Nilai Tugas :",tugas)
print("Nilai Akhir :",akhir)
print("\nNilai Huruf :",huruf)
print("Keterangan :",keterangan)
```    