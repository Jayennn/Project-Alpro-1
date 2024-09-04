# Program untuk menghitung gaji pegawai dalam satu minggu

# Meminta input dari pengguna untuk upah per jam dan mengonversinya ke tipe data integer
upah_per_jam = int(input("Masukkan upah per jam: "))

# KONSTANTA
SATU_HARI_KERJA = 8  # Jumlah jam kerja dalam satu hari
HARI_KERJA_PER_MINGGU = 5  # Jumlah hari kerja dalam satu minggu

# Menghitung total jam kerja dalam satu minggu
total_jam_kerja = SATU_HARI_KERJA * HARI_KERJA_PER_MINGGU

# Menghitung total gaji pegawai dalam satu minggu
total_upah = upah_per_jam * total_jam_kerja

# Menampilkan hasil perhitungan total gaji pegawai dalam satu minggu
print(f"Total gaji pegawai dalam satu minggu: Rp. {total_upah:,.2f}")
