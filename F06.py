import Utilities as u
# F06 - Jin pembangun
def bangun(Jusn:str, bahan_bangunan:list, candi:list):
    banyak_candi = u.my_length(candi)
    pasir = u.rng()
    batu = u.rng()
    air = u.rng()
    amount_pasir = bahan_bangunan[0][2]
    amount_batu = bahan_bangunan[1][2]
    amount_air = bahan_bangunan[2][2]

    bahan_cukup = False 
    if int(amount_pasir) >= pasir and int(amount_batu) >= batu and int(amount_air) >= air:
        bahan_cukup = True

    if banyak_candi < 100:
        if bahan_cukup:
            print("Candi berhasil dibangun.")
            banyak_candi += 1
            sisa_candi = 100 - banyak_candi
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")

            for i in range(100):
                if candi[i] == [None]:
                    u.attach(candi[i], [Jusn, pasir, batu, air])
                    continue
            pasir_awal = int(bahan_bangunan[0][2])
            batu_awal =int(bahan_bangunan[1][2])
            air_awal = int( bahan_bangunan[2][2])

            pasir_awal -= pasir
            batu_awal -= batu
            air_awal -= air

            bahan_bangunan[0][2] = str(pasir_awal)
            bahan_bangunan[1][2] = str(batu_awal)
            bahan_bangunan[2][2] = str(air_awal)
            
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

