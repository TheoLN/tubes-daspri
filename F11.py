from csvparser import *
from Utilities import *


def HancurkanCandi (data_candi) :
    # Spek 
    # Fungsi ini merupakan fungsi untuk menghancurkan candi atau menghapus data candi yang ingin dihapus dari matrix candi. Idenya adalah dengan mengubah data id candi
    # pada matrix candi yang ingin dihancurkan(id,pembuat,pasi,batu,air) menjadi None. Setelah itu, buat matrix baru yang berisi None dan matrix ini akan 
    # akan mengambil data tak None dari matrix candi. Ubah data pada matrixx candi dengan matrix baru tersebut.
    

    # Kamus 
    # id, count, j = integer
    # jawab = string
    # data_candi_temp = matrix
    # data_candi = matrix dari file csv

    # Algoritma
    id = int(input("Masukkan ID candi : ")) # Input nilai candi yang ingin dihancurkan
    count = 0
    data_candi_temp = [[None for i in range (5)] for j in range(101)] # Matriks sebagai pengubah dari matrix candi
    for i in range (my_length(data_candi)):
        # Loop untuk mencari id candi yang ingin dihancurkan
        if data_candi[i][0]!=None and int(data_candi[i][0]) == id : # Kondisi ketika matrix candi tak None dan elemen pada matrix candi sama dengan id
            jawab = input("Apakah anda yakin ingin menghancurkan candi ID(Y/N): ") # Meminta input user berupa string untuk memastikan
            count = 1 # Sebagai penanda jika id ditemukan
            if jawab == 'Y' or jawab == 'y' : # Kondisi jika user menjawab sesuai, ubah setiap elemen id candi yang ingin dihancurkan menjadi None
                data_candi[i][0] = None
                data_candi[i][1] = None
                data_candi[i][2] = None
                data_candi[i][3] = None
                data_candi[i][4] = None
                print("")
                print("Candi berhasil dihancurkan")
                
    if count == 0 : # Jika count = 0 maka pada loop tidak ditemukan id yang sesuai
        print("")
        print("Tidak ada candi dengan  ID tersebut.")
        print("")
        return
    j = 0
    
    for i in range(100) : 
        # Perulangan untuk memeberi nilai pada matrix data candi baru yang diberi nilai dari elemen-elemen pada matrix data candi jika elemennya tidak None
        if data_candi[i][0] != None  :
            data_candi_temp[j][0] = data_candi[i][0]
            data_candi_temp[j][1] = data_candi[i][1]
            data_candi_temp[j][2] = data_candi[i][2]
            data_candi_temp[j][3] = data_candi[i][3]
            data_candi_temp[j][4] = data_candi[i][4]
            j += 1

    return data_candi_temp

#HancurkanCandi()
#print(data_candi)

