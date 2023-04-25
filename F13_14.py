import os
import time
from Utilities import *

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
        path_for_folder_in_save = (os.path.join(loaded_folder,folder_in_save))
        if not os.path.exist(path_for_folder_in_save) :
            print("Folder \""+folder_in_save+"\" tidak ditemukan." )
            exit()
        else :
            print ("Selamat datang di program \"Membangun Candi\"")
            print ("Silahkan masukkan username anda")
            return(loaded_folder)

    else :
    ##jika input yang dimasukkan lengkap pathnya (contoh : Save/16-3-2023) atau inputnya adalah initial
        print ("Selamat datang di program \"Membangun Candi\"")
        print ("Silahkan masukkan username anda")
        return(loaded_folder)

dataBahan =[]
dataUser=[]
dataCandi = []


def create_file (path):
    
    with open (os.path.join(path,"bahan_bangunan.csv"),'w') as f:
        f.write("nama;deskripsi;jumlah\n")
        for i in range (3) :
            for j in range(3):
                if j != 2 :
                    f.write(str(dataBahan[i][j])+";")
                else :
                    f.write(str(dataBahan[i][j]))
            f.write("\n") 
            
    with open (os.path.join(path,"candi.csv"),'w') as f:
        f.write("id;pembuat;pasir;batu;air\n")
        for i in range (100):
            if not Marked(dataCandi[i][0]) :
                for j in range(5) :
                    if j != 4 :
                        f.write(str(dataCandi[i][j]),";")
                    else :
                        f.write(str(dataCandi[i][j]))
                f.write("\n")
            else :
                i= 100-1
            
    with open (os.path.join(path,"user.csv"),'w') as f:
        f.write("username;password;role\n")
        for i in range (100):
            if not Marked(dataUser[i][0]) :
                for j in range(3) :
                    if j != 4 :
                        f.write(str(dataUser[i][j]),";")
                    else :
                        f.write(str(dataUser[i][j]))
                f.write("\n")
            else :
                i= 100-1

    


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
        

save()
