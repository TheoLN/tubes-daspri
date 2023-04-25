from F13_14 import save

def exit_program () :
    choice = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"))
    if choice == 'y' or choice =='Y' :
        save()
        exit()
    elif choice =='N' or choice=='n' :
        exit()
    else :
        exit_program()



def help(username) :
    print("=========== HELP ===========")
    if username ==[None,None] :
        print("1. login")
        print("     Untuk masuk menggunakan akun")
        print("2. exit")
        print("     Untuk keluar dari program dan kembali ke terminal")
    else :
        if username[1] == "bandung_bondowoso":
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("   Untuk memanggil jin")
        elif username[1] == "roro_jonggrang" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("")
            print("")
        elif username[1]=="jin_pembangun" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
        else :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")

            

