'''
Nama : Aldil Bhaskoro Anggito Isdwihardjo
NIM  : 101012380051
Tugas Minggu 4 Pemograman Python
'''

'''
Soal No. 1
Buatlah program untuk menampilkan bilangan ganjil dan genap
mulai dari 1 sampai dengan 20 selanjutnya simpan dalam list.
'''
# Penyelesaiannya sebagai berikut
# Inisialisasi dua list kosong untuk bilangan ganjil dan genap yang berfungsi untuk menyimpan bilangan ganjil dan genap
bilangan_ganjil = []
bilangan_genap = []

# Melakukan loop dari 1 hingga 20 menggunakan "for" dari 1 sampai 20 (range 1, 21)
for i in range(1, 21):
    if i % 2 == 0:
        # Jika Bilangan genap, tambahkan kedalam list bilangan_genap
        bilangan_genap.append(i)
    else:
        # Jika Bilangan ganjil, tambahkan kedalam list bilangan_ganjil
        bilangan_ganjil.append(i)


# Perintah untuk menampilkan list dari bilangan genap pada terminal
print("List pada bilangan Genap:", bilangan_genap)

# Perintah untuk menampilkan list dari bilangan ganjil pada terminal
print("List pada bilangan Ganjil:", bilangan_ganjil)


'''
Soal No. 2
Buat dictionary dengan ketentuan sebagai berikut.
    "Key" : Value (****),

    "Thriller": 1982,
    "Back in Black": 1980,
    "The Dark Side of the Moon": 1973,
    "The Bodyguard": 1992,
    "Bat Out of Hell": 1977,
    "Their Greatest Hits (1971-1975)": 1976

a. Tampilkan setiap nilai yang ada pada dictionary tersebut
b. Tampilkan nilai untuk data "The Dark Side of the Moon"
c. Tambahkan data pada dictionary "Soulvaki" dengan nilai 1993
d. Hitung banyaknya value pada dictionary
e. Check 1992 terdapat pada dictionary kemudian print pesan "Data 1992 ditemukan"

'''
# Penyelesaiannya sebagai berikut

# Pertama, membuat dictionary data terlebih dahulu
data_dictionary = {
    "Thriller": 1982,
    "Back in Black": 1980,
    "The Dark Side of the Moon": 1973,
    "The Bodyguard": 1992,
    "Bat Out of Hell": 1977,
    "Their Greatest Hits (1971-1975)": 1976
}

# a. Menampilkan setiap nilai dictionary menggunakan "for" untuk menampilan setiap nilai pada dictionary melalui terminal
print("a. Masing - masing nilai dari dictionary adalah : ")
for value in data_dictionary.values():
    print(value)

# b. Menampilkan nilai dari data “The Dark Side of the Moon”
print("\nb. Nilai untuk data 'The Dark Side of the Moon' adalah ", data_dictionary["The Dark Side of the Moon"])

# c. Menambahkan data “Soulvaki” dengan nilai 1993 pada dictionary 
data_dictionary["Soulvaki"] = 1993
print("\nc. Data 'Soulvaki' dengan nilai 1993 telah ditambahkan kedalam dictionary")

# d. Menghitung total nilai pada dictionary menggunakan len (berfungsi untuk mengkalkulasikan jumlah keseluruhan nilai dalam dictionary)
num_values = len(data_dictionary)
print("\nd. Total keseluruhan nilai pada dictionary adalah ", num_values)

# e. Melakukan pemeriksaan terhadap nilai 1992 yang terdapat pada dictionary.
#    Apabila terdapat nilai tersebut akan muncul pesan “Data 1992 ditemukan” pada terminal
#    digunakan fungsi "in" untuk melakukan pemeriksaan terhadap nilai 1992 pada dictionary 
#    agar dapat mencetak pesan yang telah dimasukan
if 1992 in data_dictionary.values():
    print("\ne. Data 1992 ditemukan")
