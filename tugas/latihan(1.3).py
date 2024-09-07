# Program untuk menghitung gaji pegawai dalam satu minggu

# Meminta input dari pengguna untuk upah per jam dan mengonversinya ke tipe data integer
hourly_wage = int(input("Masukkan upah per jam: "))

# Meminta input dari pengguna untuk jumlah hari kerja dan mengonversinya ke tipe data integer
work_days_per_week = int(input("Masukkan jumlah hari kerja: "))

# KONSTANTA
WORK_HOURS_PER_DAY = 8  # Jumlah jam kerja dalam satu hari

# Menghitung total jam kerja dalam satu minggu
total_work_hours = WORK_HOURS_PER_DAY * work_days_per_week

# Menghitung total gaji pegawai dalam satu minggu
total_salary = hourly_wage * total_work_hours

# Menampilkan hasil perhitungan total gaji pegawai dalam satu minggu
print(f"Total employee salary for one week: Rp. {total_salary}")