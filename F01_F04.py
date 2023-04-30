import Utilities as u

#F01 -- LogIn

def logIn(dataUser : list, loggedIn : list):

    i = 0
    if loggedIn == [None,None]:
        
        usn = input("Masukkan Username: ")
        pw = input("Masukkan password: ")
        
        while i < u.my_length(dataUser):
            if dataUser[i][0] == usn: #ngecek dataUser
                if dataUser[i][1] == pw:
                    print("Selamat datang,"+usn+ "!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    loggedIn[0] = usn
                    loggedIn[1] = dataUser[i][2]

                    return loggedIn
                else:
                    print("Password salah!")
                    return loggedIn
            else: 
                i += 1
        print("Username tidak terdaftar!")
        return loggedIn
    else: 
        print("Login gagal!")
        print("Anda telah login dengan username ",loggedIn[0],"silahkan lakukan “logout” sebelum melakukan login kembali.")
        return loggedIn
    
#F02 -- LogOut
        
def logout(loggedIn):
    if loggedIn != [None,None]:
        loggedIn = [None, None]
        print("Logout Berhasil!")
        return loggedIn
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return loggedIn

#F03 -- SummonJin

def summonJin(dataJin):

    if u.my_length(dataJin) > 102:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return dataJin
    else:
        print("Jenis jin yang dapat dipanggil: ")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        while True:
            Jenis = str(input("Masukkan nomor jenis jin yang dipanggil: "))

            if Jenis == "1":
                print("Memilih jin “Pengumpul”.")
                Jenis = "jin_pengumpul"
                break
            elif Jenis == "2":
                print("Memilih jin “Pembangun”.")
                Jenis = "jin_pembangun"
                break
            else: 
                print(f"Tidak ada jenis jin bernomor “{Jenis}”!")
    
        i = 0
        while True:
            Jusn = str(input("Masukkan username jin: "))
            
            bool = False
            for i in range (u.my_length(dataJin)):
                if Jusn == dataJin[i][0]:
                    bool = True
            
            if not bool:
                while True:
                    Jpw = str(input("Masukkan password jin: ")) 
                    temp = Jpw + u.MARK
                    i = 0
                    k = temp[i]
                    while k != "\\"  :
                        i += 1
                        k = temp[i]
                    if i >= 5 and i <= 25:
                        u.attach(dataJin, [Jusn, Jpw, Jenis])
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print("")
                        print("Jin",Jusn,"berhasil dipanggil!")

                        return dataJin
                    
                    else: 
                        print("Password panjangnya harus 5-25 karakter!")
            else:
                print(f"Username “{Jusn}” sudah diambil!")


#F04 -- HilangkanJin

def hilangkanJin(dataJin,datacandi):
    hapus = input("Masukkan username jin : ")
    for i in range (u.my_length(dataJin)):
        if dataJin[i][0] == hapus:
            ans = str(input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? "))
            if ans  == "Y" or ans == "y":
                print("Jin telah berhasil dihapus dari alam gaib. ")
                
                j = 0
                while datacandi[j] != u.MARK:
                    if datacandi[j][1] == hapus:
                        datacandi = u.my_delArray(datacandi, datacandi[j])
                    else:
                        j += 1
              
                return (u.my_delArray(dataJin, dataJin[i]),datacandi)
              
              
            else:
                print("Tidak ada jin yang terhapus. ")
                return dataJin
    print("Tidak ada jin dengan username tersebut.")
    return dataJin



                






