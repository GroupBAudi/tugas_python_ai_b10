print("=== LIST - AKSES & MANIPULASI ===")
data_list = ["Nick", 21, 3.14, "Python", 2026, "Batam"]
print("List awal:", data_list)
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])
print("Slicing [1:5:2]:", data_list[1:5:2])

print("\nSebelum append:", data_list)
data_list.append("AI")
print("Sesudah append:", data_list)

print("\nSebelum insert:", data_list)
data_list.insert(2, "Ruby")
print("Sesudah insert:", data_list)

print("\nSebelum extend:", data_list)
data_list.extend(["HTML", "CSS"])
print("Sesudah extend:", data_list)

print("\nSebelum pop:", data_list)
item_pop = data_list.pop()
print("Item yang dipop:", item_pop)
print("Sesudah pop:", data_list)

print("\nSebelum remove:", data_list)
data_list.remove("Python")
print("Sesudah remove:", data_list)

print("\n=== TUPLE - IMMUTABILITY & UNPACKING ===")
data_tuple = ("Nick", "Batam", 2026, "Python", True, "AI")
print("Tuple:", data_tuple)
print("Panjang tuple:", len(data_tuple))
print("Indeks ke-2:", data_tuple[2])

nama, kota, tahun, *rest = data_tuple
print("Hasil unpacking:")
print("nama =", nama)
print("kota =", kota)
print("tahun =", tahun)
print("rest =", rest)

print("\n=== SET - KEUNIKAN & OPERASI HIMPUNAN ===")
set_a = {"python", "ruby", "html", "css", "javascript", "python"}
set_b = {"python", "css", "tensorflow", "pytorch", "javascript"}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A - B:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

set_duplikat = {"AI", "AI", "Python", "Python", "Ruby"}
print("Set dengan duplikat otomatis jadi unik:", set_duplikat)

print("\n=== DICTIONARY - KEY/VALUE DASAR ===")
mahasiswa = {
    "nama": "Nick",
    "nim": "2331182",
    "angkatan": 2023,
    "kota": "Batam"
}

print("Dict awal:", mahasiswa)

mahasiswa["jurusan"] = "Sistem Informasi"
print("Setelah tambah key jurusan:", mahasiswa)

mahasiswa["kota"] = "Batam, Indonesia"
print("Setelah ubah nilai kota:", mahasiswa)

del mahasiswa["angkatan"]
print("Setelah hapus key angkatan:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

print("\n=== NESTED STRUCTURES ===")
buku = [
    {"judul": "Python Basics", "penulis": "Andi", "tahun": 2020},
    {"judul": "Belajar Ruby", "penulis": "Budi", "tahun": 2018},
    {"judul": "AI for Beginners", "penulis": "Citra", "tahun": 2023},
    {"judul": "Web Dasar", "penulis": "Dina", "tahun": 2021}
]

print("Semua judul buku:")
for item in buku:
    print("-", item["judul"])

tahun_batas = 2021
buku_baru = [item for item in buku if item["tahun"] >= tahun_batas]
print(f"Buku terbit >= {tahun_batas}:", buku_baru)

print("\n=== COMPREHENSION & UTILITAS ===")
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]
status_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}

kalimat = "Python Data Structures with Nick"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}

print("Angka 1-20:", angka)
print("List genap:", genap)
print("List kuadrat:", kuadrat)
print("Dict genap/ganjil:", status_angka)
print("Set huruf unik:", huruf_unik)

print("\n=== KEANGGOTAAN & PENCARIAN SEDERHANA ===")
cari_list = "Nick"
if cari_list in data_list:
    print(f"'{cari_list}' ada di list pada indeks", data_list.index(cari_list))
else:
    print(f"'{cari_list}' tidak ada di list")

cari_set = "python"
if cari_set in set_a:
    print(f"'{cari_set}' ada di set A")
else:
    print(f"'{cari_set}' tidak ada di set A")