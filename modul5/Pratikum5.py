print('='*60)
print('PROGRAM INPUT DATA')
print('='*60)

dict = {}
while True:
    print('Pilih Menu Yang Tersedia')
    data = input('[L(ihat),T(ambah),U(bah),H(apus),C(ari),K(eluar) :')

    if data in ('l', 'L'):
        if dict.items():
            print("-"*75)
            print("|Daftar Nilai                                                            |") 
            print("-"*75)
            print("|No. |    Nama    |     NIM     |  UTS  |  UAS  |  Tugas  |  Akhir       |")
            print("-"*75)
            i = 0 
            for y in dict.items():
                i += 1
                print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7}      |".format
                (y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))        
        else:
           
            print("-"*75)
            print("|Daftar Nilai                              |") 
            print("-"*75)
            print("|No. |    Nama    |     NIM     |  UTS  |  UAS  |  Tugas  |  Akhir       |")
            print("-"*75)
            print("|                           TIDAK ADA DATA                               |") 
            print("-"*75)      
    elif data in ('t','T'):
        print("Tambah Data")
        nama = input("Masukan Nama      : ")
        nim = int(input("Masukan NIM    : "))
        tugas = int(input("Nilai Tugas  : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
        dict[nama] = nim, uts, uas, tugas, akhir
    elif data in ('u','U'):
        print("Ubah Data")
        nama = input("Masukan Nama                  : ")
        if nama in dict.keys():
            nim = int(input("Masukan NIM    : "))
            tugas = int(input("Nilai Tugas  : "))
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35                
            dict[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Nama {0} Tidak di Tentukan".format(nama))
    elif data in ('h','H'):
        print("Hapus Data")
        nama = input("Masukan Nama      : ")    
        if nama in dict.keys():
            del dict[nama]
        else:
            print("Nama {0} Tidak di Temukan".format(nama))
    elif data in ('c','C'):
        print("Cari Data")            
        nama = input("Masukan Nama      : ")
        if nama in dict.keys():
            print("-"*75)
            print("|Daftar Nilai                              |")  
            print("-"*75)
            print(nama, nim, uts, uas, tugas,akhir)
            print("-"*75)
        else:
            print("Nama {0} Tidak di Tentukan".format(nama))
    elif data in ('k','K'):
        print("Terima Kasih")
        break
    else:
        print("Pilih Menu Yang Tersedia")