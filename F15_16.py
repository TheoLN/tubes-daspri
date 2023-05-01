from F13_14 import save

def exit_program (dataBahan,dataCandi,dataUser) :
    choice = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"))
    if choice == 'y' or choice =='Y' :
        save(dataBahan,dataCandi,dataUser)
        exit()
    elif choice =='N' or choice=='n' :
        exit()
    else :
        exit_program(dataBahan,dataCandi,dataUser)



def help(username) :
    print("=========== HELP ===========") 
    print("1. exit")
    print("   Untuk keluar dari program dan kembali ke terminal")
    print("2. save")
    print("   Untuk menyimpan progress dalam bentuk csv di folder baru")
    if username[1] == "bandung_bondowoso":
        print("3. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("4. summonjin")
        print("   Untuk memanggil jin")
        print("5. hilangkanjin")
        print("   Untuk menghapus nama jin dari permainan")
        print("6. ubahjin")
        print("   Untuk mengubah role jin")
        print("7. batchkumpul")
        print("   Untuk mengerahkan semua jin pengumpul mengumpulkan bahan")
        print("8. batchbangun")
        print("   Untuk mengerahkan semua jin pembangun membangun candi")
        print("9. laporanjin")
        print("   Untuk menampilkan laporan data jin")
        print("10.laporancandi")
        print("   Untuk menampilkan laporan data candi")
        
    elif username[1] == "roro_jonggrang" :
        print("3. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("4. hancurkancandi")
        print("   Untuk menghancurkan candi yang telah dibangun")
        print("5. ayamberkokok")
        print("   Untuk menyelesaikan permainan")
    elif username[1]=="jin_pembangun" :
        print("3. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("4. bangun")
        print("   Untuk membangun 1 candi")

    elif username[1]=="jin_pengumpul" :
        print("3. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("4. kumpul")
        print("   Untuk mengumpulkan bahan membangun candi")

    else :
        print("3. login")
        print("   Untuk masuk menggunakan akun sesuai file user")

            

