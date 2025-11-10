#array
# Program array dua dimensi: data nilai siswa

# Membuat array 2D (list di dalam list)
nilai_siswa = [
    ["lia", 91, 75, 88],
    ["amel", 95, 88, 72],
    ["nur", 80, 85, 75],
    ["hikma", 83, 82, 77]
]

# Menampilkan semua data
print("=== Data Nilai Siswa ===")
for data in nilai_siswa:
    print(f"Nama: {data[0]}, Nilai 1: {data[1]}, Nilai 2: {data[2]}, Nilai 3: {data[3]}")

# Menghitung rata-rata tiap siswa
print("\n=== Rata-Rata Nilai ===")
for data in nilai_siswa:
    nama = data[0]
    rata = (data[1] + data[2] + data[3]) / 3
    print(f"{nama}: {rata:.2f}")





# Membuat dictionary
my_dict = {'nama': 'nurhikma', 'usia': 18, 'kota': 'enrekang'}

# Mengakses value berdasarkan key
print(my_dict['nama'])  # Output: nurhikma

# Menambah pasangan key-value
my_dict['pekerjaan'] = 'mahasiswa'
print(my_dict)  # Output: {'nama': 'nurhikma', 'usia': 18, 'kota': 'enrekang', 'pekerjaan': 'mahasiswa'
# Mengubah value
my_dict['usia'] = 19
print(my_dict)  # Output: {'nama': 'nurhikma', 'usia': '18, 'kota': 'enrekang, 'pekerjaan': 'mahasiswa'}

# Menghapus pasangan
del my_dict['kota']
print(my_dict)  # Output: {'nama': 'nurhikma', 'usia': 19, 'pekerjaan': 'mahasiswa'}

# Iterasi
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# nama: nurhikma
# usia: 18
# pekerjaan: mahasiswa
