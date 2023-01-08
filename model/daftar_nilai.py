import view

dt_mhs = {}

# Menambah Data
def tambah_data():
    global dt_mhs
    ulangi = "y"
    while ulangi == "y":
        print("\n" + "Masukan data mahasiswa")
        print("="*25)
        nama = view.in_nama()
        nim = view.in_nim()
        nilai_tugas = view.in_Ntugas()
        nilai_uts = view.in_Nuts()
        nilai_uas = view.in_Nuas()
        nilai_akhir = nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100
        dt_mhs[nim] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]
        ulangi = (input('Ingin tambah data lagi? (y/n) : '))

        if ulangi == 'n':
            print("\n" + "Data berhasil di tambahkan!")
            return dt_mhs


# Mengubah data
def ubah_data():
    nim = input("\n" + "Masukan NIM untuk mengubah data: ")

    if nim in dt_mhs.keys():
        while True:
            print("\n" + "Mau mengubah apa?")
            update_dt = input("(Semua), (Nama), (Tugas), (UTS), (UAS) : ")
            if update_dt.lower() == "semua":
                print("\n")
                print(f"Ubah semua data dari NIM '{nim}'")
                print("="*40)
                dt_mhs[nim][0] = view.upd_nama()
                dt_mhs[nim][2] = view.upd_Ntugas()
                dt_mhs[nim][3] = view.upd_Nuts()
                dt_mhs[nim][4] = view.upd_Nuas()
                dt_mhs[nim][5] = dt_mhs[nim][2]*30/100 + dt_mhs[nim][3]*35/100 + dt_mhs[nim][4] *35/100
                print("\n" + "Data berhasil diubah!")
                break

            elif update_dt.lower() == "nama":
                print("\n")
                print(f"Ubah data 'Nama' dari NIM '{nim}'")
                print("="*40)
                dt_mhs[nim][0] = view.upd_nama()
                print("\n" + "Data <nama> berhasil diubah!")
                break

            elif update_dt.lower() == "tugas":
                print("\n")
                print(f"Ubah 'Nilai Tugas' dari NIM '{nim}'")
                print("="*40)
                dt_mhs[nim][2] = view.upd_Ntugas()
                dt_mhs[nim][5] = dt_mhs[nim][2] *30/100 + dt_mhs[nim][3]*35/100 + dt_mhs[nim][4] *35/100
                print("\n" + "Data <nilai tugas> berhasil diubah!")
                break

            elif update_dt.lower() == "uts":
                print("\n")
                print(f"Ubah 'Nilai UTS' dari NIM '{nim}'")
                print("="*40)
                dt_mhs[nim][3] = view.upd_Nuts()
                dt_mhs[nim][5] = dt_mhs[nim][2] *30/100 + dt_mhs[nim][3]*35/100 + dt_mhs[nim][4] *35/100
                print("\n" "Data <nilai UTS> berhasil diubah!")
                break

            elif update_dt.lower() == "uas":
                print("\n")
                print(f"Ubah 'Nilai UAS' dari NIM '{nim}'")
                print("="*40)
                dt_mhs[nim][4] = view.upd_Nuas()
                dt_mhs[nim][5] = dt_mhs[nim][2] *30/100 + dt_mhs[nim][3]*35/100 + dt_mhs[nim][4] *35/100
                print("\n" + "Data <nilai UAS> berhasil diubah!")
                break

            else:
                print("\n" + f"<Menu '{update_dt}' tidak ditemukan!>")

    else:
        print(f"NIM '{nim}' Tidak ditemukan!")


# Menghapus data
def hapus_data():
    print("Menghapus data...")
    print("="*40)
    nim = input("Masukan NIM untuk menghapus data : ")
    if nim in dt_mhs.keys():
        del dt_mhs[nim]
        print("\n" + f"Data NIM '{nim}' berhasil dihapus!")
    else:
        print("\n" + f"NIM '{nim}' Tidak ditemukan!")


# Mencari data
def cari_data():
    print("Mencari data...")
    print("="*40)
    view.mencari_data()