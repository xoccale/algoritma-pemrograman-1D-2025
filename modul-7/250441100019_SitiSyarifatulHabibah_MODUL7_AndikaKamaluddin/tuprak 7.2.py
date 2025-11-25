inventaris = {}  

while True:
    print("\n======== SISTEM INVENTARIS ========")
    print("1. Lihat semua barang (Read)")
    print("2. Cari barang")
    print("3. Tambah barang baru (Create)")
    print("4. Update stok (Update)")
    print("5. Hapus barang (Delete)")
    print("6. EXIT")

    pilihan = input("Pilihan menu: ")

    
    if pilihan == "1":
        kosong = True
        for id_b in inventaris:
            kosong = False
            break

        if kosong:
            print("Tidak ada item yang terdaftar.")
        else:
            print("\n====== DAFTAR BARANG ======")
            for id_b in inventaris:
                nama = inventaris[id_b][0]
                harga = inventaris[id_b][1]
                stok = inventaris[id_b][2]
                print(f"ID: {id_b} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

                
    
    elif pilihan == "2":
        id_cari = input("Masukkan ID barang: ")

        if id_cari in inventaris:
            print("\nBarang ditemukan!")
            print("ID   :", id_cari)
            print("Nama :", inventaris[id_cari][0])
            print("Harga:", inventaris[id_cari][1])
            print("Stok :", inventaris[id_cari][2])
        else:
            print("Barang tidak ditemukan.")

    
    elif pilihan == "3":
        id_baru = input("Masukkan ID barang: ")
        nama = input("Masukkan nama barang: ")
        while True:
            harga = input("Masukkan harga barang: ")
            valid = True
            for angka in harga:
                if angka not in "0123456789":
                    valid = False
                    break
                
            if valid:
                harga = int(harga)
                break
            print("Harga tidak valid! Harus angka.")

        while True:
            stok = input("Masukkan stok barang: ")
            valid = True
            for angka in stok:
                if angka not in "0123456789":
                    valid = False
                    break

            if valid:
                stok = int(stok)
                break
            print("Stok tidak valid! Harus angka.")

        inventaris[id_baru] = [nama, harga, stok]
        print("Barang udah ditambahkan.")

    
    elif pilihan == "4":
        if kosong:
            print("Tidak ada item yang terdaftar.")
        else:
            print("\n================ DAFTAR BARANG ================")
            for id_b in inventaris:
                nama = inventaris[id_b][0]
                harga = inventaris[id_b][1]
                stok = inventaris[id_b][2]
                print(f"ID: {id_b} | Nama: {nama} | Harga: {harga} | Stok: {stok}")
        id_up = input("\nMasukkan ID barang yang ingin di-update: ")

        if id_up in inventaris:
            stok_baru = int(input("Masukkan stok baru: "))

            if stok_baru < 0:
                print("Stok tidak boleh negatif!")
            else:
                inventaris[id_up][2] = stok_baru
                print("Stok berhasil diperbarui.")
        else:
            print("Ups, gagal menemukan barang.")

    
    elif pilihan == "5":
        id_del = input("Masukkan ID barang yang mau dihapus: ")

        if id_del in inventaris:
            del inventaris[id_del]
            print("Done, barang berhasil dihapus.")
        else:
            print("Ups, gagal menemukan barang.")

    
    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silahkan pilih angka menu")