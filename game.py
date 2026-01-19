secret_number = 777
guess_number = int(input("Masukkan Tebak Angka: "))

while guess_number != secret_number:
    print("Tebakan salah, silahkan coba lagi")
    guess_number = int(input("Masukkan Tebak Angka: "))

print("Selamat!! Tebakan anda benar")
print("Kode ini saya buat di codespace")
