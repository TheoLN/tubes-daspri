from Utilities import *
from csvparser import *


def laporancandi (data_candi):

    
    totalCandi=0
    TotalPasir=0
    TotalBatu=0
    TotalAir=0
    candiTermahal = 0
    candiTermurah = 0
    HargaTerbesar = -999999
    harga_total = [[None for j in range (2)] for i in range(101)]
    HargaTerkecil = 999999
    for i in range (1,101):
        print (data_candi[i])
        if data_candi[i][1]!=None:
            totalCandi+=1
            TotalPasir+=int(data_candi[i][2])
            TotalBatu+=int(data_candi[i][3])
            TotalAir+=int(data_candi[i][4])
            harga_total[i][0] = int(data_candi[i][2])*10000 +int(data_candi[i][3])*15000 +int(data_candi[i][4])*7500
            harga_total[i][1] = data_candi[i][0]   
    for i in range (101) :
        if harga_total[i][0]!= None and harga_total[i][0] >= HargaTerbesar :
            HargaTerbesar = harga_total[i][0]
            candiTermahal = data_candi[i][0]   
    for i in range (101) :
        if harga_total[i][0] != None and harga_total[i][0] < HargaTerkecil :
            HargaTerkecil = harga_total[i][0]
            candiTermurah = data_candi[i][0]   
    if totalCandi == 0 :
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {TotalPasir}")
        print(f"> Total Batu yang digunakan: {TotalBatu}")
        print(f"> Total Air yang digunakan: {TotalAir}")
        print(f"ID Candi termahal: -")
        print(f"ID Candi termurah: -")
    else :
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {TotalPasir}")
        print(f"> Total Batu yang digunakan: {TotalBatu}")
        print(f"> Total Air yang digunakan: {TotalAir}")
        print(f"ID Candi termahal: {candiTermahal} ({HargaTerbesar})")
        print(f"ID Candi termurah: {candiTermurah} ({HargaTerkecil})")

