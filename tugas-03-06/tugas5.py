def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai():.2f}, status={self.status()})"


if __name__ == "__main__":
# --- DEMO FUNCTIONS ---
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")

    # --- DEMO CLASS ---
    print("\n=== CLASS STUDENT ===")
    
    # Mahasiswa 1
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80.0)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(82.5)
    
    # Mahasiswa 2
    mhs2 = Student("Siti", "A124")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)

    # Cetak sesuai instruksi
    print(mhs1)
    print(f"Rata-rata: {mhs1.rata_nilai()} | Status: {mhs1.status()}")
    
    print(mhs2)
    print(f"Rata-rata: {mhs2.rata_nilai()} | Status: {mhs2.status()}")