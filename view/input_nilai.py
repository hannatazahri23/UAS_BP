# Inputan Tambah Data
def in_nama() ->str:
    nama = input(f"{'Nama':<12}:")
    return nama

def in_nim() ->str:
    nim = input(f"{'NIM':<12}:")
    return nim

def in_Ntugas() ->int:
    nilai_tugas = int(input(f"{'Nilai Tugas':<12}:"))
    return nilai_tugas

def in_Nuts() ->int:
    nilai_uts = int(input(f"{'Nilai UTS':<12}:"))
    return nilai_uts

def in_Nuas() ->int:
    nilai_uas = int(input(f"{'Nilai UAS':<12}:"))
    return nilai_uas


# Inputan Ubah Data
def upd_nama() ->str:
    u_nama = input(f"{'Ubah Nama':<18}:")
    return u_nama

def upd_Ntugas() ->int:
    u_Ntugas = int(input(f"{'Ubah Nilai Tugas':18}:"))
    return u_Ntugas

def upd_Nuts() ->int:
    u_Nuts = int(input(f"{'Ubah Nilai UTS':18}:"))
    return u_Nuts

def upd_Nuas() ->int:
    u_Nuas = int(input(f"{'Ubah Nilai UAS':18}:"))
    return u_Nuas