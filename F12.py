
from Utilities import *
from csvparser import *

def AyamBerkokok(data_candi) :
    # Spek 
    # Fungsi ini merupakan fungsi untuk menghitung jumlah candi yang dibangun dan menentukan pemenang berdasarkan kondisi berikut. Jika candi yang dibagun kurang dari 100,
    # Roro Jongrang yang memenangkan permainan. Jika candi yang dibangun lebih dari 100, Bandung Bondowoso yang memenangkan permainan. 
    

    # Kamus 
    # count = jumlah dari candi yang dibangun = integer
    # data_candi = matrix dari file csv

    # Algoritma
    print("Kukuruyuk.. Kukuruyuk..")
    print("")
    count = 0
    for i in range (100) :
        # Loop untuk mencari jumlah elemen pada kolom id yang tidak None dan tidak sama dengan mark
        if data_candi[i][0]!= None and data_candi[i] != "\\mark": # Jika kondisi memenuhi count yang merupakan jumlah dari candi akan bertambah satu
            count += 1 
    print("Jumlah Candi: ", count)
    print("")
    if count >= 100 : # Jika count / candi yang dibangun lebih dari 100, Bandung Bondowoso yang memenangkan permainan,
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    elif count >= 0 and count < 100 : # Kondisi jika Rorojongrang memenangkan permainan
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
#AyamBerkokok()
