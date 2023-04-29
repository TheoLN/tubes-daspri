import Utilities as u
# F06 - Jin pembangun
def bangun(Jusn:str, bahan_bangunan:list, candi:list):
    banyak_candi=0
    for i in range (u.my_length(candi)):
        if candi[i][0]!= None :
            banyak_candi +=1
    
    pasir = u.rng()
    batu = u.rng()
    air = u.rng()
    amount_pasir = int(bahan_bangunan[0][2])
    amount_batu = int(bahan_bangunan[1][2])
    amount_air = int(bahan_bangunan[2][2])

    bahan_cukup = False 
    if amount_pasir >= pasir and amount_batu >= batu and amount_air >= air:
        bahan_cukup = True

    if banyak_candi < 100:
        if bahan_cukup:
            print("Candi berhasil dibangun.")
            banyak_candi += 1
            sisa_candi = 100 - banyak_candi
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
            
            
            count = 0
            for i in range(2+u.my_length(candi)):   
                
                temp_array=[i,Jusn,pasir,batu,air]
                if count == 0 and candi[i][0] == None :
                    count+=1
                    
                u.attach(candi,temp_array)
                
            
                    
            pasir_awal = int(bahan_bangunan[0][2])
            batu_awal =int(bahan_bangunan[1][2])
            air_awal = int( bahan_bangunan[2][2])


            bahan_bangunan[0][2] = str(pasir_awal-pasir)
            bahan_bangunan[1][2] = str(batu_awal-batu)
            bahan_bangunan[2][2] = str(air_awal-air)
            
            
            return bahan_bangunan,candi
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        return bahan_bangunan, candi
    else:
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: 0.")
        return bahan_bangunan, candi


# F07 - Jin Pengumpul
def kumpul(bahan_bangunan: list):
    pasir = u.rng()
    batu = u.rng()
    air = u.rng()

    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    pasir_awal= int(bahan_bangunan[0][2])
    batu_awal =int(bahan_bangunan[1][2])
    air_awal = int(bahan_bangunan[2][2])
    pasir_akhir =pasir_awal + pasir
    batu_akhir = batu_awal + batu
    air_akhir = air_awal +air

    (bahan_bangunan[0][2]) = str(pasir_akhir)
    (bahan_bangunan[1][2]) = str(batu_akhir)
    (bahan_bangunan[2][2]) = str(air_akhir)
    
    return bahan_bangunan

