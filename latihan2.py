gaji = int(input("Masukkan gaji:"))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]

if gaji > 3000000:
     print ("Gaji sudah diatas UMR")
     if berkeluarga:
          print ("Waji ikutan asuransi dan menabung untuk pensiun")
     else:
          print("Tidak perlu asuransi")
     if punya_rumah:
          print ("wajib bayar pajak rumah")
     else:
          print("tidak wajib bayar pajak rumah")

else:
     print("Gaji belum UMR")

