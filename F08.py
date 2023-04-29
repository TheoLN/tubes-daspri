import Utilities as u 
from F06 import bangun

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
    
def batchBangun(dataJin, bahan_bangunan,candi):
    banyak_candi = u.my_length(candi)
    jumlah_pembangun = 0
    array_jin = [ "" for i in range(100)]
    index_jin =0
    for i in range(u.my_length(dataJin)):
        if dataJin[i][2] == "jin_pembangun":
            array_jin[index_jin]= dataJin[i][0]
            index_jin +=1
            jumlah_pembangun+=1
    cond=True

    if jumlah_pembangun!=0:
        bahan = [0 for i in range(3)]
        bahan_bangunan_request = [[0 for i in range(3)]for i in range (3)]
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
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
    if cond:
        candi_terbangun = 0
        if banyak_candi + jumlah_pembangun>100:
            candi_terbangun = 100 - banyak_candi
            banyak_candi += candi_terbangun
        else:
            candi_terbangun = jumlah_pembangun
        print(f'Mengerahkan {jumlah_pembangun} jin untuk membangun candi dengan total {bahan_bangunan_request[0][2]} pasir, {bahan_bangunan_request[1][2]} batu, dan {bahan_bangunan_request[2][2]} air.')
        print(f'Jin berhasil membangun total {candi_terbangun} candi.')

        for i in range(candi_terbangun):
            bahan_bangunan,candi = bangun(array_jin[i],bahan_bangunan,candi)
            
            

        
        return bahan_bangunan,candi
    else:
        print(f"Bangun gagal. Kurang {Selisih(bahan_bangunan_request[0][2],int(bahan_bangunan[0][2]))} pasir, {Selisih(bahan_bangunan_request[1][2],int(bahan_bangunan[1][2]))} batu, dan {Selisih(bahan_bangunan_request[2][2],int(bahan_bangunan[2][2]))} air.")
        return bahan_bangunan,candi