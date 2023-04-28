def jumlahTakNone (x) :
    count = 0
    for i in range (100) :
        if x[i][0] != None :
            count += 1
    return count
def cek (x,temp) :
    count = 0
    for i in range(100) :
          if temp == x[i][0] :
               count += 1
    if count == 0 :
        return True
    else :
         return False
def laporanjin(user,bahan,candi):
    totJinkumpul,totJinBangun=0,0
    nomor = 0
    terajin = ''
    termalas = ''
    pembuat = [[None for j in range (2)] for i in range(100)]
    for i in range(102):
        if user[i]!=None:
            if user[i][2]=="jin_pengumpul" :
                totJinkumpul+=1
            elif user[i][2]=="jin_pembangun":
                totJinBangun+=1
    print(f"> Total Jin: {totJinBangun+totJinkumpul}")
    print(f"> Total Jin Pengumpul: {totJinkumpul}")
    print(f"> Total Jin Pembangun: {totJinBangun}")

    for i in range(100) :
        for j in range(jumlahTakNone(pembuat)+1) :
            if candi[i][1] != None and candi[i][1] == pembuat[j][0] :
                pembuat[j][1] += 1
                break
            if candi[i][1] != None and candi[i][1] != pembuat[j][0] :
                if cek(pembuat,candi[i][1]) == True :
                    pembuat[nomor][0] = candi[i][1]
                    pembuat[nomor][1] = 1
                    nomor += 1
                    break      
    terkecil = 999999
    terbesar = -999999
    for i in range (jumlahTakNone(pembuat)) :
        if pembuat[i][1] > terbesar and pembuat[i][1] != None :
            terbesar =  pembuat[i][1]
            terajin = pembuat[i][0]
        elif pembuat[i][1] == terbesar and  pembuat[i][0] < terajin :
            terajin = pembuat[i][0]
            terbesar = pembuat[i][1]
    for i in range (jumlahTakNone(pembuat)) :
        if pembuat[i][0] != None and pembuat[i][1] < terkecil:
            terkecil =  pembuat[i][1]
            termalas = pembuat[i][0]
        elif pembuat[i][1] == terkecil and  pembuat[i][0] > termalas :
            termalas = pembuat[i][0]
            terkecil = pembuat[i][1]
    if terbesar != -999999 and terkecil != 999999 :
        print(f"> Jin Terajin: ", terajin)
        print(f"> Jin Termalas: ", termalas)
    else:
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")
    print(f"> Jumlah Pasir: {bahan[3][2]} unit")
    print(f"> Jumlah Air: {bahan[1][2]} unit")
    print(f"> Jumlah Batu: {bahan[2][2]} unit")
    return