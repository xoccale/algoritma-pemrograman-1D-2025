print("\nPROGRAM VALIDASI KUPON DISKON SISTEM KASIR\n")

barang = {
    "01": ["Air Mineral 600ml", 5000],
    "02": ["Mi Instan", 3500],
    "03": ["Susu Cair UHT", 9000],
    "04": ["Telur Ayam (1 butir)", 2500],
    "05": ["Beras Premium 1kg", 14000],
    "06": ["Gula Pasir 1kg", 13500],
    "07": ["Tepung Terigu 1kg", 12000],
    "08": ["Minyak Goreng 1 Liter", 15000],
    "09": ["Roti Tawar", 12000],
    "10": ["Sabun Mandi Cair", 18000]
}

kupon = {
    "YOUVEGOTDISC10": 10,
    "YEAYY15": 15,
    "WOAHHDISC20NIH": 20,
    "DISC5BERSYUKURAJA": 5,
    "TABARAKALLAH50DONG": 30
}

kupon_digunakan = []

while True:
    print("MENU UTAMA SISTEM KASIR")
    print("1. Tampilkan Semua Kupon Tersedia")
    print("2. Proses Transaksi Menggunakan Kupon")
    print("3. Selesai, Keluar dari Program")

    pilihan = input("\nSilakan pilih menu (Hanya di Nomor 1-3): ")

    try:
        pilihan = int(pilihan)
        if pilihan < 1 or pilihan > 3:
            print("Input tidak valid! Silakan pilih menu nomor 1 hingga 3.\n")
            continue
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka, bukan huruf atau simbol.\nSilakan coba lagi.\n")
        continue

    if pilihan == 1:
        print("\nTAMPILKAN SEMUA KUPON TERSEDIA")
        if len(kupon) == 0:
            print("Belum ada kupon yang tersimpan.\n")
        else:
            for kode, diskon in kupon.items():
                print("Kode Kupon:", kode, "| Diskon:", diskon, "%")
            print()

    elif pilihan == 2:
        print("\nPROSES TRANSAKSI MENGGUNAKAN KUPON\n")
        keranjang = {}
        print("DAFTAR BARANG:")
        for kode, info in barang.items():
            print(kode, "-", info[0], "| Harga: Rp", info[1])
        print()

        while True:
            kode_barang = input("Masukkan kode barang (ENTER untuk selesai): ")

            if kode_barang == "":
                if len(keranjang) == 0:
                    print("Keranjang masih kosong! Masukkan minimal 1 barang.\n")
                    continue
                else:
                    break

            if kode_barang not in barang:
                print("Kode barang tidak valid! Silakan masukkan kode yang sesuai.\n")
                continue

            while True:
                jumlah = input("Masukkan jumlah barang: ")
                if jumlah == "":
                    print("Input tidak valid! Jumlah tidak boleh kosong.\n")
                    continue
                try:
                    jumlah = int(jumlah)
                    if jumlah <= 0:
                        print("Jumlah harus lebih dari 0.\n")
                        continue
                    break
                except:
                    print("Jumlah harus berupa angka! Silakan ulangi.\n")
                    continue

            if kode_barang in keranjang:
                keranjang[kode_barang] = keranjang[kode_barang] + jumlah
            else:
                keranjang[kode_barang] = jumlah

            print("Barang berhasil ditambahkan ke keranjang!\n")

        total_belanja = 0
        print("\nRINCIAN BELANJA:")
        for kode, jumlah in keranjang.items():
            nama = barang[kode][0]
            harga = barang[kode][1]
            subtotal = harga * jumlah
            total_belanja = total_belanja + subtotal
            print(nama, "x", jumlah, ":", "Rp", subtotal)

        print("\nTotal Belanja Awal :", "Rp", total_belanja)

        while True:
            punya_kupon = input("\nApakah Anda memiliki kode kupon? (Y/T): ").upper()
            if punya_kupon not in ["Y", "T"]:
                print("Input tidak valid! Masukkan 'Y' atau 'T'.\n")
                continue
            break

        if punya_kupon == "Y":
            while True:
                kode_input = input("Masukkan kode kupon: ").upper()

                if kode_input == "":
                    print("Input tidak valid! Kode kupon tidak boleh kosong.\n")
                    continue

                if kode_input in kupon:
                    diskon = kupon[kode_input]
                    total_bayar = total_belanja * (100 - diskon) // 100
                    print("\nKupon valid! Diskon", diskon, "% diterapkan.")
                    print("\nRincian Transaksi:")
                    print("Total Belanja Awal       : Rp", total_belanja)
                    print("Kode Kupon Digunakan     :", kode_input)
                    print("Persentase Diskon        :", str(diskon) + "%")
                    print("Diskon Diperoleh         : Rp", total_belanja * diskon // 100)
                    print("Total yang Harus Dibayar : Rp", total_bayar)

                    kupon_digunakan.append(kode_input)
                    del kupon[kode_input]
                    print("\nKupon telah digunakan dan dihapus dari daftar kupon.\n")
                    break

                else:
                    if kode_input in kupon_digunakan:
                        print("Kupon tidak valid! Kupon sudah digunakan.\n")
                    else:
                        print("Kupon tidak valid! Tidak ada dalam daftar kupon.\n")
                    continue

        else:
            total_bayar = total_belanja
            print("\nTransaksi tanpa kupon.")
            print("\nRincian Transaksi:")
            print("Total Belanja Awal       : Rp", total_belanja)
            print("Kode Kupon Digunakan     : -")
            print("Persentase Diskon        : 0%")
            print("Diskon Diperoleh         : Rp 0")
            print("Total yang Harus Dibayar : Rp", total_bayar)
            print("\nPembayaran selesai tanpa kupon.\n")

    elif pilihan == 3:
        print("\nSELESAI, KELUAR DARI PROGRAM")
        print("Terima kasih! Program Validasi Kupon Diskon telah selesai dijalankan.\n")
        break