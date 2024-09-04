# Program untuk menghitung luas permukaan tabung

# Meminta input dari pengguna untuk jari-jari tabung dan mengonversinya ke tipe data float
radius = float(input("Masukkan jari-jari tabung: "))

# Meminta input dari pengguna untuk tinggi tabung dan mengonversinya ke tipe data float
height = float(input("Masukkan tinggi tabung: "))

# Menghitung luas permukaan tabung dengan rumus 2πr(r + t)
surface = 2 * 3.14 * radius * (radius + height)

# Menampilkan hasil perhitungan luas permukaan tabung dengan 2 angka di belakang koma
print(f"Luas permukaan tabung adalah: {surface:.2f}")
