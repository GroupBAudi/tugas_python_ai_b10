# Deklarasi variabel dan tipe data
nama_program = "Infinite Learning"
umur = 20
sedang_belajar = True
hobi = ["coding", "rally", "musik", "game"]

# Manipulasi string
nama_depan = "Nick"
nama_belakang = "Candra"

print("=== Manipulasi String ===")
print("Nama lengkap:", nama_depan + " " + nama_belakang)
print("Panjang nama depan:", len(nama_depan))
print("Huruf besar:", nama_depan.upper())
print("Huruf kecil:", nama_belakang.lower())

# Operasi matematika sederhana
angka1 = 15
angka2 = 4

print("\n=== Operasi Matematika ===")
print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pembagian bulat:", angka1 // angka2)
print("Sisa bagi:", angka1 % angka2)

# List dan akses elemen
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("\n=== List ===")
print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen ketiga:", buah[2])

buah.append("semangka")
print("Setelah append:", buah)

buah.remove("jeruk")
print("Setelah remove:", buah)

buah.pop()
print("Setelah pop:", buah)

# Input dari user
print("\n=== Input User ===")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun.")