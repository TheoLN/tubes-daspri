def jumlahTakNone (x) :
    # Spek : fungsi untuk menghitung dalam suatu baris matrix, berapa jumlah yang tidak None

    # Kamus 
    # count = integer

    # Algoritma
    count = 0
    for i in range (100) :  # Loop sebanyak berapa jumlah baris pada matrix
        if x[i][0] != None : # Kondisi ketika elemen tidak sama dengan nol, jumlah akan bertambah satu
            count += 1
    return count

def cek (x,temp) :
    # Spek : fungsi untuk mengecek apakah ada elemen yang sama pada array dengan suatu variabel yang ditentukan
    # input berupa array dan variabel yang ingin dicari.

    # Kamus 
    # count = integer

    # Algoritma
    count = 0
    for i in range(100) : # Loop sebanyak berapa jumlah baris pada matrix
          if temp == x[i][0] : # Kondisi ketika ada elemen yang sama dengan variabel yang ditetapkan maka jumlah akan bertambah satu
               count += 1
    if count == 0 : # Jika tidak ada yang sama yang diindikasikan dengan jumlah nol maka return True. sebaliknya return False
        return True
    else :
         return False
      
def laporanjin(user,bahan,candi):
    # Spek 
    # merupakan fungsi yang menerima input matrix dari tiga file csv yang ada. Fungsi ini akan mengembalikan nilai dari total jin, total jin pengumpul
    # Total jin pembangun yang datanya diambil dari user.csv, mengembalikan jin yang terajin dan termalas yang datanya diambil dari candi.csv, serta jumlah pasir,
    # batu, air yang datanya diambil bahan_bangunan.csv. Untuk mencari total jin, jin pengumpul dan jin pembangun, kita melakukan loop pada matrix user kolom role.
    # Ketika menemukan kesamaan antara data pada matrix dengan str yang diinginkan, maka variable yang menyimpan nilai total dari semua jin dan total masing-masing jin 
    # bertambah satu. Untuk mencari jin terajin dan termalas idenya yaitu kita membuat 100 x 2 dengan kolom nama jin dan jumlah candi yang ia bangun dengan elemen pada
    # matrix tersebut unik / hanya ada satu nama jin beserta jumlahnya. Ketika ditemukan kesamaan nama jin pada matrix candi awal, maka yang bertambah adalah jumlahnya
    # Idenya kita melakukan nested loop dengan loop pertama merupakan loop membaca file csv dan loop kedua loop pada baris matrix yang 
    # kita buat. Dari setiap elemen pada data file csv yang tidak none kita melakukan pengecekan pada setiap elemen matrix bentukan. Ketika ada yang sama, lakukan break lalu 
    # tambah jumlahnya pada kolom jumlah candi bersesuaian dengan jenis jin yang sama tersebut di matrix. Ketika tidak ditemukan elemen yang sama dari array bentukan,
    # cek apakah elemen tersebut sudah ada di matrix bentukan. Jika belum ubah baris baru dengan jenis jin tersebut dan berikan jumlahya satu. Ketika sudah selesai melakukan
    # loop, cari jin yang terajin dengan membandingkan jumlah candi terbanyak yang dibangun lalu diambil nama jinnya. Ketika ada yang sama bandingkan leksikografis yang terendah.
    # Sebaliknya untuk mencari jin termalas dengan membandingkan jumlah candi paling sedikit yang dibangun lalu diambil nama jinnya. Ketika ada yang sama bandingkan leksikografis 
    # yang terbesar. Selain itu, untuk mencari jumlah pasir, batu, dan air hanya perlu mengambil data dari matrix bahan_bangunan sesuai dengan baris dan kolom
    # yang sesuai.

    # Kamus 
    # totJinkumpul, totJinBangun, terbesar, terkecil, nomor = integer
    # terajin, termalas = string
    # pembuat = matrix
    # user, candi, bahan = matrix dari file csv

    # Algoritma
    totJinkumpul,totJinBangun=0,0
    nomor = 0
    terajin = ''
    termalas = ''
    pembuat = [[None for j in range (2)] for i in range(100)] # deklarasi matrix nama jin dan jumlah candi yang ia buat
    for i in range(102):
        # Loop sebanyak jumlah baris pada matrix. Ketika ditemukan elemen yang sesuai dengan yang diinginkan dalam hal ini 
        # jin_pengumpul dan jin_pembangun pada matrix, variabel yang merupakan jumlah string tersebut bertambah satu
        if user[i]!=None:
            if user[i][2]=="jin_pengumpul" :
                totJinkumpul+=1
            elif user[i][2]=="jin_pembangun":
                totJinBangun+=1
    print(f"> Total Jin: {totJinBangun+totJinkumpul}") # mencetak hasil dari jumlah total jin kumpul dan bangun
    print(f"> Total Jin Pengumpul: {totJinkumpul}") # mencetak hasil dari jumlah total jin kumpul dan bangun
    print(f"> Total Jin Pembangun: {totJinBangun}") # mencetak hasil dari jumlah total jin kumpul dan bangun

    for i in range(1,101) : # Loop pada matrix candi
        for j in range(jumlahTakNone(pembuat)+1) : # Loop pada matrix pembuat dengan batas elemen yang tidak None tambah satu
            if candi[i][1] != None and candi[i][1] == pembuat[j][0] and candi[i][0] != '\\':
                # Ketika elemen pada matrix candi tidak None dan tidak merupakan mark, ketika elemen pada candi sama dengan elemen yang ada pada matrox, maka jumlah pada
                # matrix pembuat dalam hal ini pada kolom satu akan bertambah satu
                pembuat[j][1] += 1
                break
            if candi[i][1] != None and candi[i][1] != pembuat[j][0] and candi[i][0] != '\\' :
                # Ketika elemen pada matrix candi tidak None dan tidak merupakan mark, ketika elemen pada candi tidak ada yang sama dengan elemen yang ada pada matrix, 
                # maka lakukan pengecekan apakah nama jin tersebut sudah ada di matrix pembuat atau tidak, jika belum ada, buat baris baru untuk nama jin tersebut, dan 
                # beri jumlah satu.
                if cek(pembuat,candi[i][1]) == True :
                    pembuat[nomor][0] = candi[i][1]
                    pembuat[nomor][1] = 1
                    nomor += 1
                    break 
    terkecil = 999999 # Dipilih terkecil nilai tersebut dengan asumsi tidak ada yang lebih besar dari nilai tersebut
    terbesar = -999999 # Dipilih terbesar nilai tersebut dengan asumsi tidak ada yang lebih kecil dari nilai tersebut
    for i in range (jumlahTakNone(pembuat)) :
        # Loop untuk mencari nilai terbesar pada matrix dengan cara membandingkan dengan variabel terbesar dengan jumlah masing-masing elemen dari
        # nama setiap jin yang ada pada matrix.
        if pembuat[i][1] > terbesar and pembuat[i][1] != None :
            # Ketika ada elemen yang lebih besar dari variabel terbesar, ubah variabel tersebut sesuai elemen pada jumlah candi yang lebh besar dan ambil data dari
            # matrix tersebut nama jinnya
            terbesar =  pembuat[i][1]
            terajin = pembuat[i][0]
        elif pembuat[i][1] == terbesar and  pembuat[i][0] < terajin :
            # Ketika ada elemen yang sama dengan variabel terbesar, bandingkan leksikografis terendah dari kedua jin tersebut
            terajin = pembuat[i][0]
            terbesar = pembuat[i][1]
    for i in range (jumlahTakNone(pembuat)) :
        if pembuat[i][0] != None and pembuat[i][1] < terkecil:
            # Ketika ada elemen yang lebih kecil dari variabel terkcil, ubah variabel tersebut sesuai elemen pada jumlah candi yang lebih kecil dan ambil data dari
            # matrix tersebut nama jinnya
            terkecil =  pembuat[i][1]
            termalas = pembuat[i][0]
        elif pembuat[i][1] == terkecil and  pembuat[i][0] > termalas :
            # Ketika ada elemen yang sama dengan variabel terkecil, bandingkan leksikografis terbesar dari kedua jin tersebut
            termalas = pembuat[i][0]
            terkecil = pembuat[i][1]
    if terbesar != -999999 and terkecil != 999999 : # Jika ada perubahan nilai pada variabel atau ketika elemen pada matrix tidak nol maka cetak nilai var terajin dan termalas
        print(f"> Jin Terajin: ", terajin)
        print(f"> Jin Termalas: ", termalas)
    else: # Ketika tidak ada perubahan pada variabel terbesar dan terkecil
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")

    print(f"> Jumlah Pasir: {bahan[0][2]} unit") # mencetak jumlah pasir dengan mengambil data pada lokasi yang bersesuaian pada matrix bahan
    print(f"> Jumlah Batu: {bahan[1][2]} unit") # mencetak jumlah air dengan mengambil data pada lokasi yang bersesuaian pada matrix bahan
    print(f"> Jumlah Air: {bahan[2][2]} unit") # mencetak jumlah batu dengan mengambil data pada lokasi yang bersesuaian pada matrix bahan
    return
