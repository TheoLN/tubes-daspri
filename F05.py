import Utilities as u

def ubahjin(dataJin):
    Jusn = str(input("Masukkan username jin: "))
    if Jusn == "Bondowoso" or Jusn =="Roro" :
        print("Tidak dapat diubah tipe")
        return(dataJin)
    
  
    Jenis = None
    index = None
    for i in range(u.my_length(dataJin)):
        if dataJin[i][0] == Jusn:
            Jenis = dataJin[i][2]
            index = i
            if Jenis == "jin_pengumpul":
                print("Jin ini bertipe pengumpul",end=" ")
                Jenis_baru = input("Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")

                if Jenis_baru == 'Y' or Jenis_baru =='y':
                    dataJin[index][2] = "jin_pembangun"
                    print("Jin telah berhasil diubah.")
                
                    return(dataJin)
                else:
                    return(dataJin)
            else:
                print("Jin ini bertipe pembangun",end=" ")
                Jenis_baru = input("Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                if Jenis_baru == 'Y' or Jenis_baru =='y':
                    dataJin[index][2] = "jin_pengumpul"
                    print("Jin telah berhasil diubah.")
                    return(dataJin)
                else:
                    return(dataJin)
    else:
        print("Tidak ada jin dengan username tersebut.")
        return(dataJin)
        




        