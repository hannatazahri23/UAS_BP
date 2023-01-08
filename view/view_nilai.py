import model

# PROGRAM UTAMA
## cetak_daftar_nilai
def lihat_data():
    print("Daftar Nilai:")
    print("="*67)
    print(f"|{'No':^4}|{'Nama':^20}|{'NIM':^11}|{'Tugas':^7}|{'UTS':^5}|{'UAS':^5}|{'Akhir':^7}|")
    print("="*67)
    if model.dt_mhs.keys():
        no = 1
        for tabel in model.dt_mhs.values():
            print(f"| {no:<3}| {tabel[0]:<19}| {tabel[1]:<10}| {tabel[2]:<6}| {tabel[3]:<4}| {tabel[4]:<4}| {tabel[5]:<6}|")
            print("-"*67)
            no += 1
    else:
        print(f"|{'!! TIDAK ADA DATA !!':^65}|")
        print("="*67)

## cetak_hasil_pencarian
def mencari_data():
    nim = input("Masukan NIM untuk mencari data: ")
    print("\n" + f"Result ({nim})")
    print("="*67)
    print(f"|{'Nama':^22}|{'*NIM':^13}|{'Tugas':^7}|{'UTS':^5}|{'UAS':^5}|{'Akhir':^7} |")
    print("="*67)
    if nim in model.dt_mhs.keys():
        print(f"| {model.dt_mhs[nim][0]:<21}| {model.dt_mhs[nim][1]:<12}| {model.dt_mhs[nim][2]:<6}| {model.dt_mhs[nim][3]:<4}| {model.dt_mhs[nim][4]:<4}| {model.dt_mhs[nim][5]:<6} |")
        print("-"*67)
    else:
        print(f"NIM '{nim}' Tidak ditemukan!")


# FUNCTION TAMBAHAN (template)
def template_op():
    print("="*67)
    print(f"|{'| PROGRAM INPUT NILAI MAHASISWA |':_^65}|")
    print("="*67)

def msg_salah():
    char1 = f"{'='*55}".center(67)
    tx_salah ="| Kesalahan memasukan perintah, Silahkan cek kembali! |".center(67)
    char2 = f"{'='*55}".center(67)
    print(char1)
    print(tx_salah)
    print(char2)

def template_end():
    char1 = f"{'='*55}".center(67)
    tx_end1 = "|-------------------PROGRAM SELESAI-------------------|".center(67)
    tx_end2 = "|-----TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI-----|".center(67)
    char2 = f"{'='*55}".center(67)

    print(char1)
    print(tx_end1)
    print(tx_end2)
    print(char2)