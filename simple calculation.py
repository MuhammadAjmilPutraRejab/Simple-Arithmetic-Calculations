def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa dibagi dengan nol!"

print("Operasi Aritmatika Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")


pilihan = int(input("Pilih operasi (1/2/3/4): "))


angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))


if pilihan == 1:
    print("Hasil Penjumlahan:", tambah(angka1, angka2))
elif pilihan == 2:
    print("Hasil Pengurangan:", kurang(angka1, angka2))
elif pilihan == 3:
    print("Hasil Perkalian:", kali(angka1, angka2))
elif pilihan == 4:
    print("Hasil Pembagian:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid!")
