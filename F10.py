from Utilities import *
from csvparser import *


def laporancandi (data_candi):
    # Spek 
    # Fungsi ini merupakan fungsi yang mengembalikan hasil dari laporan candi dengan mengembalikan nilai total candi, total pasir, batu, air yang digunakan, dan
    # id candi dan nilainya yang termurah dan termahal. Untuk mencari nilai total candi,dapat dilakukan dengan melakukan perulangan mencari ada berapa banyak
    # elemen tak none pada baris pembuat. Untuk mencari total pasir, batu, air yang digunakan dapat dilakukan dengan cara melakukan perulangan pada matrix candi bagian
    # pasir, batu, air untuk menjumlahkan nilai integer dari setiap elemen baris pasir, batu, air yang tak None. Untuk mendapatkan id candi beserta nilainya yang 
    # termahal dan termurah dapat dilakukan dengan melakukan penjumlahan berdarkan harga dari masing-masing pasir, batu, air untuk setiap candi lalu simpan setiap nilai
    # tersebut pada suatu matirx beserta dengan idnya. Untuk mencari yang termahal dan termurah lakukan perulangan pada baris harga dengan cara membandingkan nilainya 
    # dengan variabel bentukan dan setiap lebih besar atau lebih kecil ubah nilai variabel tersebut dengan nilai elemen pada matrixx tersebut.

    # Kamus 
    # totalCandi, TotalPasir, TotalBatu, TotalAir, candiTermahal, candiTermurah, HargaTerbesar, HargaTerkecil  = integer
    # terajin, termalas = string
    # harga_total = matrix
    # data_candi = matrix dari file csv

    # Algoritma

    totalCandi=0
    TotalPasir=0
    TotalBatu=0
    TotalAir=0
    candiTermahal = 0
    candiTermurah = 0
    HargaTerbesar = -999999
    HargaTerkecil = 999999
    harga_total = [[None for j in range (2)] for i in range(101)]
    
    for i in range (0,101): 
        # Melakukan perulangan untuk menentukan berapa banyak candi yang ada dengan mencari elemen yang tidak None serta menjumlah masing-masing elemen yang tidak None
        # pada baris pasir, batu, air dari matrix bahan bangunan.
        if data_candi[i][1]!=None and data_candi[i][0] != '\\': # Kondisi elemen tidak none dan tidak sama dengan mark
            totalCandi+=1
            TotalPasir+=int(data_candi[i][2]) # Penjumlahan elemen total pasir pada elemen yang sesuai
            TotalBatu+=int(data_candi[i][3]) # Penjumlahan elemen total batu pada elemen yang sesuai
            TotalAir+=int(data_candi[i][4]) # Penjumlahan elemen total air pada elemen yang sesuai
            harga_total[i][0] = int(data_candi[i][2])*10000 +int(data_candi[i][3])*15000 +int(data_candi[i][4])*7500 
            # Menjumlahkan dari setiap elemen berdasarkan harga yang ditetapan untuk pasir, batu, air
            harga_total[i][1] = data_candi[i][0]   #id dari candi yang dibangun 
    for i in range (101) :
        # Loop untuk mencari harga termahal dari matrix harga_total baris harga dengan membandingkan dengan suatu variable. Ketika elemen pada matrix tidak None
        # dan lebih dari atau sama dengan var HargaTerbesar, ubah nilai  var HargaTerbesar dengan elemen pada matrix tersebut, lalu ambil idnya.
        if harga_total[i][0]!= None and harga_total[i][0] >= HargaTerbesar : # Kondisi yang memenuhi
            HargaTerbesar = harga_total[i][0] 
            candiTermahal = data_candi[i][0]  # Mengambil id candi dari hargaterbesar
    for i in range (101) :
        # Loop untuk mencari harga termurah dari matrix harga_total baris harga dengan membandingkan dengan suatu variable. Ketika elemen pada matrix tidak None
        # dan kurang dari atau sama dengan var HargaTerkecil, ubah nilai var HargaTerkecil dengan elemen pada matrix tersebut, lalu ambil idnya.
        if harga_total[i][0] != None and harga_total[i][0] < HargaTerkecil : # Kondisi yang memenuhi
            HargaTerkecil = harga_total[i][0]
            candiTermurah = data_candi[i][0]   # Mengambil id candi dari hargaterbesar
    if totalCandi == 0 : # Jika candinya nol id candi termurah dan termahal tidak ada
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {TotalPasir}")
        print(f"> Total Batu yang digunakan: {TotalBatu}")
        print(f"> Total Air yang digunakan: {TotalAir}")
        print(f"ID Candi termahal: -")
        print(f"ID Candi termurah: -")
    else : # Jika candinya tidak nol id candi termurah dan termahal bernilai variabel tersebut
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {TotalPasir}")
        print(f"> Total Batu yang digunakan: {TotalBatu}")
        print(f"> Total Air yang digunakan: {TotalAir}")
        print(f"ID Candi termahal: {candiTermahal} ({HargaTerbesar})")
        print(f"ID Candi termurah: {candiTermurah} ({HargaTerkecil})")



