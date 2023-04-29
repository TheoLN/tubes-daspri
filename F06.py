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
            
            for i in range(u.my_length(candi)):  
                index=i 
                if not u.Marked(candi[i+1]):
                    if int(candi[i+1][0]) - int(candi[i][0]) != 1 and count ==0:
                        i = int(candi[i][0])+1
                        u.attach(candi,[str(i),Jusn,pasir,batu,air])
                        count +=1

            if count == 0 :
                u.attach(candi,[str(index+2),Jusn,pasir,batu,air])
                
            candi = u.sort_id(candi)
            
                    
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

