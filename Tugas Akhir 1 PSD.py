barang = ["Buku", "Mainan", "Sepatu", "Kartu", "Krayon", "Pensil"]
kotak = []

def Lihat_Barang():
    print("Daftar barang:")
    for i, b in enumerate(barang, start=1):
        print(f"{i}. {b}")

def masuk_dalam_kotak():
    Lihat_Barang()
    try:
        index = int(input("Masukkan No. barang: ")) - 1
        if 0 <= index < len(barang):
            kotak.append(barang[index])
            print("barang dimasukkan kedalam kotak.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus angka.")

def buang_dari_kotak():
    if not kotak:
        print("Kotak kosong.")
        return
    
    print("\nIsi Kotak:")
    for i, b in enumerate(kotak, start=1):
        print(f"{i}. {b}")
    
    try:
        index = int(input("Nomor yang ingin dihapus: ")) - 1
        if 0 <= index < len(kotak):
            removed = kotak.pop(index)
            print(f"{removed} dibuang dari kotak.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus angka.")

def Lihat_Kotak():
    if not kotak:
        print("Kotak kosong.")
    else:
        print("Isi Kotak:")
        for i, b in enumerate(kotak, start=1):
            print(f"{i}. {b}")

def menu():
    while True:
        print(" MENU :")
        print("1. Periksa Barang")
        print("2. masuk ke kotak")
        print("3. buang dari kotak")
        print("4. Periksa Kotak")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            Lihat_Barang()
        elif pilihan == "2":
            masuk_dalam_kotak()
        elif pilihan == "3":
            buang_dari_kotak()
        elif pilihan == "4":
            Lihat_Kotak()
        elif pilihan == "5":
            print("Semoga Bermanfaat")
            break
        else:
            print("Menu tidak valid.")

menu()