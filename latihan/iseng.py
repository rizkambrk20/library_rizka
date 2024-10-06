import random

welcome_messages = "Welcome To My Games!"
cuypy_position = random.randint(1, 8)


print("********************")
print(f"{welcome_messages}")
print("********************")

nama_user = input("Masukan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa]*8
goa = goa_kosong.copy()

goa[cuypy_position -1] = "|0_0|"
joined_array_goa_kosong=''.join(goa_kosong)
joined_array_goa = ''.join(goa)

print(f'''
Halo {nama_user}! Coba perhatikan goa di bawah ini
{joined_array_goa_kosong}
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1/ 2/ 3 /4 5/ 6/ 7/ 8]:"))

Konfirmasi = input(f"Apakah kamu sudah yakin jawabannya adalah {pilihan_user} [yes/ no?]")

if Konfirmasi == "yes":
    if pilihan_user == cuypy_position:
        print(f"{joined_array_goa} \n Selamat {nama_user} kamu menang! posisi CUYPY berada di goa {cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
    else:
        print(f"Kamu kalah! \n {joined_array_goa} \n CUYPY bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.")
elif Konfirmasi == "no":
    print("kamu keluar dari games! PAYAH SEKALI KAMU!!!")
    exit()
else:
    print("Silahkan Ulangi Gamesnya!!!")
