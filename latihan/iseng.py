import random

welcome_messages = "Welcome To My Games!"
cuypy_position = random.randint(1, 8)


print("********************")
print(f"{welcome_messages}")
print("********************")

nama_user = input("Masukan nama kamu: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa di bawah ini
|_| |_| |_| |_| |_| |_| |_| |_|
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1/ 2/ 3 /4 5/ 6/ 7/ 8]:"))

Konfirmasi = input("Apakah kamu sudah yakin dengan pilihanmu? [yes/ no?]")

if Konfirmasi == "yes":
    print()
else:
    print("kamu keluar dari games! PAYAH SEKALI KAMU!!!")
    exit()

    
if pilihan_user == cuypy_position:
    print(f"Selamat {nama_user} kamu menang! posisi CUYPY berada di goa {cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
else:
    print(f"Kamu kalah! CUYPY bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.")