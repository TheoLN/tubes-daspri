import os
import time


def load(folder) :
# Kamus lokal
## lokasi_file : path yang merujuk pada folder utama
## loaded_folder : path yang merujuk pada folder yang diload

#algoritma
    lokasi_file = os.path.dirname(os.path.realpath(__file__))
    loaded_folder = os.path.join(lokasi_file, folder)
    print(loaded_folder)

    if not os.path.exists(loaded_folder) :
    ##Jika folder tidak ada 
        print("Folder \""+folder+"\" tidak ditemukan." )
        exit()

    elif folder == "Save" :
    ##jika input hanya folder save
        folder_in_save = str(input("Masukkan nama folder yang ada di dalam folder \"Save\" :"))
        print ("Selamat datang di program \"Membangun Candi\"")
        print ("Silahkan masukkan username anda")
        return(os.path.join(loaded_folder,folder_in_save))
    else :
    ##jika input yang dimasukkan lengkap pathnya (contoh : Save/16-3-2023) atau inputnya adalah initial
        print ("Selamat datang di program \"Membangun Candi\"")
        print ("Silahkan masukkan username anda")
        return(loaded_folder)
        
def create_file (path):
    
    with open (os.path.join(path,"bahan_bangunan.csv"),'w') as f:
        f.writelines("hellor")
    with open (os.path.join(path,"candi.csv"),'w') as f:
        f.writelines("hellor")
    with open (os.path.join(path,"user.csv"),'w') as f:
        f.writelines("hellor")


def cek_file(path) :
    a = os.path.join(path,"user.csv")
    b = os.path.join(path,"candi.csv")
    c = os.path.join(path,"bahan_bangunan.csv")
    if os.path.isfile(a) and os.path.isfile(b) and os.path.isfile(c):
        return False
    else :
        return True

    
def save() :
    lokasi_file = os.path.dirname(os.path.realpath(__file__))
    folder_save = os.path.join(lokasi_file, "Save")
    save_folder = str(input("Masukkan nama folder :"))
    folder = os.path.join(folder_save,save_folder)
    if not os.path.isdir(folder):
        print("saving .  .  .")
        os.mkdir(folder)
        create_file(folder)
        print("Berhasil menyimpan data di Save/"+save_folder)
    elif  os.path.isdir(folder) and cek_file(folder):
        print("saving .  .  .")
        create_file(folder)
        print("Berhasil menyimpan data di Save/"+save_folder)
    elif not cek_file(folder) :
        print("saving .  .  .")
        create_file(folder) 
        


     
