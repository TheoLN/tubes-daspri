import Utilities as u 

def Selisih(input1,input2): 
    if (input1-input2)<0:
        return 0
    else:
        return(input1-input2)

def batchKumpul(dataJin, bahan_bangunan):
    jumlah_pengumpul = 0
    for i in range(u.my_length(dataJin)):
        if dataJin[i][2] == "jin_pengumpul":
            jumlah_pengumpul+=1
    if jumlah_pengumpul!=0:
        count_pasir =0
        count_batu =0
        count_air = 0
        bahan = [0 for i in range (4)]
        for i in range(jumlah_pengumpul):
            for j in range(3):  
                bahan[j] = u.rng()
                if j == 0 :
                    pasir = int(bahan_bangunan[j][2])+bahan[j]
                    count_pasir +=bahan[j]
                    bahan_bangunan[j][2] = str(pasir)
                if j == 1:
                    batu = int(bahan_bangunan[j][2]) + bahan[j]
                    bahan_bangunan[j][2] = str(batu)
                    count_batu += bahan[j]
                if j == 2:
                    air = int(bahan_bangunan[j][2]) + bahan[j]
                    bahan_bangunan[j][2] = str(air)
                    count_air+= bahan[j]
        print(f'Mengerahkan {jumlah_pengumpul} jin untuk mengumpulkan bahan.')
        print(f'Jin menemukan total {count_pasir} pasir, {count_batu} batu, dan {count_air} air.')
        return(bahan_bangunan)
    else:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
    
def batchBangun(dataJin, bahan_bangunan,dataCandi):
    jumlah_pembangun = 0
    for i in range(u.my_length(dataJin)):
        if dataJin[i][2] == "jin_pembangun":
            jumlah_pembangun+=1
    cond=True
    if jumlah_pembangun!=0:
        bahan = [0 for i in range(4)]
        bahan_bangunan_request = [0]
        for i in range(jumlah_pembangun):
            for j in range(3):  
                bahan[j] = u.rng()
                if j == 0:
                    bahan_bangunan_request[j][2]+=bahan[j]
                if j == 1:
                    bahan_bangunan_request[j][2]+=bahan[j]
                if j == 2:
                    bahan_bangunan_request[j][2]+=bahan[j]
        for i in range(3):
            if int(bahan_bangunan[i][2]) < bahan_bangunan_request[i][2]:
                cond = False       
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terelbih dahulu.')
    if cond:
        print(f'Mengerahkan {jumlah_pembangun} jin untuk membangun candi dengan total {bahan_bangunan_request[0][2]} pasir, {bahan_bangunan_request[1][2]} batu, dan {bahan_bangunan_request[2][2]} air.')
        print(f'Jin berhasil membangun total {jumlah_pembangun} candi.')
    else:
        print(f'Bangun gagal. Kurang {Selisih(bahan_bangunan_request[0][2],bahan_bangunan[0][2])} pasir, {Selisih(bahan_bangunan_request[1][2],bahan_bangunan[1][2])} batu, dan {Selisih(bahan_bangunan_request[2][2],bahan_bangunan[2][2])} air.')