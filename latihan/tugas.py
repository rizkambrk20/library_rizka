print("******** Data Inputan ******** ")
brt  =int(input("Berat:"))
hrg  =int(input("Harga:"))
ongkos =int(input("Ongkos:"))
uang =int(input("Uang:"))

print("******** HAsil Inputan ********")
print("Sisa :"+str(uang-ongkos*2-hrg*brt))