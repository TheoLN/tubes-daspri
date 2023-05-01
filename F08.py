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
        return(bahan_bangunan)
    
def batchBangun(dataJin, bahan_bangunan,candi):
    banyak_candi = u.my_length(candi)
    jumlah_pembangun = 0
    for i in range(u.my_length(dataJin)):
        if dataJin[i][2] == "jin_pembangun":
            jumlah_pembangun+=1
    cond=True
    if jumlah_pembangun!=0:
        bahan = [0 for i in range(4)]

        ## array_bahan untuk menyimpan data bahan yang diperlukan untuk masing masing candi yang berbeda
        array_bahan =[None for i in range(u.NMAX)]
        array_bahan[0] = u.MARK

        bahan_bangunan_request = [[0 for i in range(3)]for j in range(3)]
        for i in range(jumlah_pembangun):
            for j in range(3):  
                bahan[j] = u.rng()
                
                if j == 0:
                    bahan_bangunan_request[j][2]+=bahan[j]
                if j == 1:
                    bahan_bangunan_request[j][2]+=bahan[j]
                if j == 2:
                    bahan_bangunan_request[j][2]+=bahan[j]
            u.attach(array_bahan, [str(bahan[0]),str(bahan[1]),str(bahan[2])])
        

                
        for i in range(3):
            if int(bahan_bangunan[i][2]) < bahan_bangunan_request[i][2]:
                cond = False       
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
        return(bahan_bangunan,candi)
    if cond:        ## bahan yang dimiliki cukup
        candi_terbangun = 0
        if banyak_candi + jumlah_pembangun>100:
            candi_terbangun = 100 - banyak_candi
            banyak_candi += candi_terbangun
            
        else:
            candi_terbangun = jumlah_pembangun
        print(f'Mengerahkan {candi_terbangun} jin untuk membangun candi dengan total {bahan_bangunan_request[0][2]} pasir, {bahan_bangunan_request[1][2]} batu, dan {bahan_bangunan_request[2][2]} air.')
        print(f'Jin berhasil membangun total {candi_terbangun} candi.')

    ## membangun candi sebanyak candi_terbangun
        jin=0  ## variabel untuk menentukan nama jin yang membangun
        count =0
        if u.my_length(candi) == 0 : ##kondisi jika program masih initial dan belum ada candi yang terbangun
            for i in range(u.my_length(dataJin)) :
                if dataJin[i][2] == "jin_pembangun" and count ==0 :
                    u.attach(candi,["1",dataJin[i][0],array_bahan[0][0],array_bahan[0][1],array_bahan[0][2]])
                    count+=1
                    jin = i+1
        
        for i in range(count, candi_terbangun) :  #loop sebanyak candi terbangun 
            count = 0 ## mereset count tiap loop
            for j in range(u.my_length(candi)): ## untuk mengecek id candi
                id = j
                for k in range(jin,u.my_length(dataJin)) :  ## untuk mengecek username jin
                    if dataJin[k][2] == "jin_pembangun": ##jika jin merupakan jin pembangun
                        if candi[j+1] != u.MARK : ## kalau index bukan index yang terakhir
                            
                            if candi[0][0] != "1" and count ==0 :  ## jika id candi yang pertama bukan satu 
                                u.attach(candi,["1",dataJin[k][0],array_bahan[i][0],array_bahan[i][1],array_bahan[i][2]])
                                count+=1
                                jin = k+1 ## agar loop selanjutnya dilanjut dari jin setelah jin ini

                            elif int(candi[j+1][0]) - int(candi[j][0]) != 1 and count ==0:  ##jika selisih antar 2 id candi yang berdampingan lebih dari satu 
                                j = int(candi[j][0])+1
                                u.attach(candi,[str(j),dataJin[k][0],array_bahan[i][0],array_bahan[i][1],array_bahan[i][2]]) 
                                count +=1
                                jin = k+1
                        
                        elif count == 0 :  ## kondisi dimana semua id candi sudah urut dan benar
                            u.attach(candi,[str(id+2),dataJin[k][0],array_bahan[i][0],array_bahan[i][1],array_bahan[i][2]])
                            jin=k+1
            u.sort_id(candi)        ## Untuk mengsort id candi tiap selesai membangun 1 candi

        ## Mengurangi banyak bahan bangunan
        for i in range(3) :
            bahan_bangunan[i][2] = str (int(bahan_bangunan[i][2])-bahan_bangunan_request[i][2])

        
        return(bahan_bangunan,candi)
    else: ##bahan yang dimiliki tidak cukup
        print(f'Bangun gagal. Kurang {Selisih(bahan_bangunan_request[0][2],int(bahan_bangunan[0][2]))} pasir, {Selisih(bahan_bangunan_request[1][2],int(bahan_bangunan[1][2]))} batu, dan {Selisih(bahan_bangunan_request[2][2],int(bahan_bangunan[2][2]))} air.')
        return (bahan_bangunan,candi)