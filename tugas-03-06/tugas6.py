import numpy as np
import pandas as pd
import os

np.random.seed(42)


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["nilai"] >= threshold).mean() * 100
        return round(lulus, 2)

    def save_summary(self, path: str):
        jumlah_lulus = (self.df["status"] == "LULUS").sum()
        jumlah_tidak_lulus = (self.df["status"] == "TIDAK LULUS").sum()

        with open(path, "a", encoding="utf-8") as file:
            file.write("\n=== RINGKASAN GRADEBOOK ===\n")
            file.write(f"Jumlah data      : {len(self.df)}\n")
            file.write(f"Rata-rata nilai  : {self.average()}\n")
            file.write(f"Persentase lulus : {self.pass_rate()}%\n")
            file.write(f"Jumlah lulus     : {jumlah_lulus}\n")
            file.write(f"Jumlah tidak lulus : {jumlah_tidak_lulus}\n")

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"


if __name__ == "__main__":
    print("=== NUMPY ===")
    nilai_ujian = np.array([78, 85, 90, 66, 72, 88, 95, 60, 74, 81])

    rata2 = np.mean(nilai_ujian)
    median = np.median(nilai_ujian)
    std_dev = np.std(nilai_ujian)
    nilai_min = np.min(nilai_ujian)
    nilai_max = np.max(nilai_ujian)

    print("Array nilai:", nilai_ujian)
    print("Rata-rata:", round(rata2, 2))
    print("Median:", round(median, 2))
    print("Standar deviasi:", round(std_dev, 2))
    print("Nilai minimum:", nilai_min)
    print("Nilai maksimum:", nilai_max)

    print("\n=== PANDAS ===")
    data = {
        "nama": ["Andi", "Budi", "Citra", "Dina", "Eko"],
        "nim": ["A101", "A102", "A103", "A104", "A105"],
        "nilai": nilai_ujian[:5]
    }

    df = pd.DataFrame(data)
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

    print(df.head())

    jumlah_lulus = (df["status"] == "LULUS").sum()
    jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum()

    ringkasan_path = "ringkasan_tugas6.txt"
    with open(ringkasan_path, "w", encoding="utf-8") as file:
        file.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        file.write(f"Rata-rata        : {round(rata2, 2)}\n")
        file.write(f"Median           : {round(median, 2)}\n")
        file.write(f"Standar deviasi  : {round(std_dev, 2)}\n")
        file.write(f"Nilai minimum    : {nilai_min}\n")
        file.write(f"Nilai maksimum   : {nilai_max}\n")
        file.write("\n=== RINGKASAN DATAFRAME ===\n")
        file.write(f"Jumlah baris     : {len(df)}\n")
        file.write(f"Jumlah lulus     : {jumlah_lulus}\n")
        file.write(f"Jumlah tidak lulus : {jumlah_tidak_lulus}\n")

    print("\n=== OOP: GRADEBOOK ===")
    gradebook = GradeBook(df)
    print(gradebook)
    print("Average:", gradebook.average())
    print("Pass rate:", gradebook.pass_rate(), "%")
    gradebook.save_summary(ringkasan_path)

    print(f"\nRingkasan berhasil disimpan di: {os.path.abspath(ringkasan_path)}")