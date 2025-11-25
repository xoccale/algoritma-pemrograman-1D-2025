contacts = {} 
 
while True:
    print("\n=============================")
    print("===== MENU CONTACT BOOK =====")
    print("1. Lihat semua kontak (Read)")
    print("2. Cari kontak")
    print("3. Tambah kontak (Create)")
    print("4. Update email (Update)")
    print("5. Hapus kontak (Delete)")
    print("6. EXIT")

    pilihan = input("Pilih menu 1-6 (jangan sampe salah input): ")

    if pilihan == "1": 
        kosong = True
        for nama in contacts:
            kosong = False
            break

        if kosong:
            print("\nKontak masih kosong, tambahin kontak dulu.")
        else:
            print("\n====== List Kontak ======")
            for nama in contacts:
                nomor = contacts[nama][0]
                email = contacts[nama][1]
                print(f"Nama: {nama} | Nomor: {nomor} | Email: {email}")   

    elif pilihan == "2":
        nama_cari = input("|| 2. Cari Kontak. ||Masukkan nama kontak: ")

        if nama_cari in contacts:
            print("\nKontak ditemukan!")
            print("Nama :", nama_cari)
            print("Nomor:", contacts[nama_cari][0])
            print("Email:", contacts[nama_cari][1])
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == "3":
        nama = input("||3. Tambah Kontak. ||Masukkan nama: ")

        while True:
            nomor = input("Masukkan nomor: ")
            if not (nomor.isdigit() and 3 <= len(nomor) <= 15):
                print("Nomormu tidak valid karna harus angka saja dan minimal 3 angka, max 15 angka!")
                continue

            nomor_sama = any(info[0] == nomor for info in contacts.values())
            if nomor_sama:
                print("Nomor ini udah dipake kontak lain. Masukkan nomor lain.")
                continue

            break
        
        while True:
            email = input("Masukkan email: ")
            if "@" not in email or "." not in email:
                print("Email tidak valid. Harus mengandung '@' dan '.'.")
                continue

            email_sama = any(info[1] == email for info in contacts.values())
            if email_sama:
                print("Email ini udah dipakai kontak lain. Masukkan email lain.")
                continue

            break

        contacts[nama] = [nomor, email]
        print("\nKontak baru sudah masuk!")

    elif pilihan == "4":
        if not contacts:
            print("Belom ada kontak.")
        else:
            print("\n================== List Kontak ==================")
            for nama in contacts:
                nomor = contacts[nama][0]
                email = contacts[nama][1]
                print(f"Nama: {nama} | Nomor: {nomor} | Email: {email}")
            print("================================================")

            nama_up = input("|| 4. Update email. ||Masukkan nama kontak yang ingin di-update: ")

            if nama_up in contacts:
                while True:
                    email_baru = input("Masukkan email baru: ")
                    if "@" in email_baru and "." in email_baru:
                        break
                    print("Email tidak valid. Harus mengandung misalnya '@gmail.com' atau 'ac.id'. Coba lagi.")

                contacts[nama_up][1] = email_baru
                print("Email syudah berhasil diperbarui!")
            else:
                print("Yakin udah ada kontaknya? Kontak tdak ditemukan.")

    elif pilihan == "5":
        if not contacts:
            print("Belom ada kontak.")
        else:
            print("\n================== List Kontak ==================")
            for nama in contacts:
                nomor = contacts[nama][0]
                email = contacts[nama][1]
                print(f"Nama: {nama} | Nomor: {nomor} | Email: {email}")
            print("================================================")

        nama_hapus = input("|| 5. Hapus kontak. ||Masukkan nama kontak yang ingin dihapus: ")
            
        if nama_hapus in contacts:
            del contacts[nama_hapus]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == "6":
        print("Okey, program ditutup.")
        break

    else:
        print("Pilihan tidak valid, silahkan pilih angka menu.")