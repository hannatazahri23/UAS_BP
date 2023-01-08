import os
import model
import view

os.system("cls")
view.template_op()

while True:
    print("\n")
    print("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar")
    menu = input("Pilih menu: ")
    print("\n")

    # Menu
    if menu.lower() == 't':
        os.system("cls")
        view.template_op()
        print("\n")
        model.tambah_data()

    elif menu.lower() == 'c':
        os.system("cls")
        view.template_op()
        print("\n")
        model.cari_data()

    elif menu.lower() == 'l':
        os.system("cls")
        view.template_op()
        print("\n")
        view.lihat_data()

    elif menu.lower() == 'u':
        os.system("cls")
        view.template_op()
        print("\n")
        model.ubah_data()

    elif menu.lower() == 'h':
        os.system("cls")
        view.template_op()
        print("\n")
        model.hapus_data()

    # Keluar
    elif menu.lower() == 'k':
        view.template_end()
        break

    # Kesalahan
    else:
        os.system("cls")
        view.template_op()
        print("\n")
        view.msg_salah()