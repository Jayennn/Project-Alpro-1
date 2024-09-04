# Program untuk mengonversi suhu dari Celsius ke Fahrenheit

# Meminta input suhu dalam Celsius dari pengguna dan mengonversinya ke tipe data float
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Menghitung suhu dalam Fahrenheit menggunakan rumus (C × 9/5) + 32
fahrenheit = (celcius * 9/5) + 32

# Menampilkan hasil konversi suhu dengan 2 angka di belakang koma
print(f"Hasil konversi Celcius ke Fahrenheit: {fahrenheit:.2f}")
