
from Utilities import *
from csvparser import *

def laporanjin(user,bahan,candi):
    totJinkumpul,totJinBangun=0,0
    nomor = 0
    terbesar = 0
    terkecil = 0
    terajin = ''
    termalas = ''
    totalcandi = [[0 for j in range (2)] for i in range(100)]
    for i in range(102):
        if user[i]!=None:
            if user[i][2]=="jin_pengumpul" :
                totJinkumpul+=1
            elif user[i][2]=="jin_pembangun":
                totJinBangun+=1
    print(f"> Total Jin: {totJinBangun+totJinkumpul}")
    print(f"> Total Jin Pengumpul: {totJinkumpul}")
    print(f"> Total Jin Pembangun: {totJinBangun}")
    for i in range (1, 102):
        for j in range(100):
            if candi[i][1] is not None :
                if candi[i][1] == totalcandi[j][0] :
                    totalcandi[j][1] += 1
                    break
        else :
            totalcandi[nomor][0] = candi[i][1]
            totalcandi[nomor][1] += 1
            nomor += 1
    terkecil = totalcandi[i][1]
    termalas = totalcandi[i][0]
    for i in range (100) :
        if totalcandi[i][1] > terbesar :
            terbesar =  totalcandi[i][1]
            terajin = totalcandi[i][0]
        elif totalcandi[i][1] == terbesar and  totalcandi[i][0] > terajin :
            terajin = totalcandi[i][0]
            terbesar = totalcandi[i][1]
    for i in range (100) :
        if totalcandi[i][1] < terbesar :
            terkecil =  totalcandi[i][1]
            termalas = totalcandi[i][0]
        elif totalcandi[i][1] == terkecil and  totalcandi[i][0] < terajin :
            termalas = totalcandi[i][0]
            terkecil = totalcandi[i][1]
    # terkecil = totalcandi[0][1]
    # for i in range (jumlahjin) :
    #     if totalcandi[i][1] < terkecil :
    #         terkecil =  totalcandi[i][1]
    if terbesar != 0 and terkecil != 0 :
        print(f"> Jin Terajin: ", terajin)
        print(f"> Jin Termalas: ", termalas)
    else:
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")
    print(f"> Jumlah Pasir: {bahan[1][2]} unit")
    print(f"> Jumlah Air: {bahan[3][2]} unit")
    print(f"> Jumlah Batu: {bahan[2][2]} unit")
    return

#laporanjin(data_user, bahan_bangunan, data_candi)