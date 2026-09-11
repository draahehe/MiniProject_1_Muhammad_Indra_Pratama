jual_akun = []

def tampilkan_menu():
    print("\nWelcome Guis :v")
    print("\nSilahkan memilih opsi menu yang tersedia:")
    print("1. Tambah Akun")
    print("2. View Semua Akun")
    print("3. Update Data Akun")
    print("4. Delete Akun")
    print("5. Keluar")

def tambah_akun():
    print("\nTambah Akun")
    id_akun = input("Masukkan ID Akun Yang Ingin Ditambahkan: ")
    nama_game = input("Masukkan Nama Game: ")

    while True:
        harga = input("Masukkan Harga Jual (Rp): ")
        if harga.isdigit():
            harga = int(harga)
            break
        else:
            print("Harga hanya boleh berisi angka tanpa huruf atau simbol!")

    while True:
        status = input("Masukkan Status Akun(Tersedia/Terjual): ").capitalize()
        if status in ["Tersedia", "Terjual"]:
            break
        else:
            print("Status hanya boleh 'Tersedia' atau 'Terjual' Tidak ada pilihan lain.")

    jual_akun.append((id_akun, nama_game, harga, status))
    print("Akun berhasil ditambahkan.")

def lihat_akun():
    print("\nDaftar Akun Game Yang Tersedia:")
    if len(jual_akun) == 0:
        print("Tidak ada data akun.")
    else:
        for i, akun in enumerate(jual_akun):
            print(f"{i+1}. ID: {akun[0]} | Game: {akun[1]} | Harga: Rp{akun[2]} | Status: {akun[3]}")

def ubah_akun():
    print("\nUpdate Data Akun")
    if len(jual_akun) == 0:
        print("Tidak ada data akun.")
        return

    if len(jual_akun) == 1:
        index = 0
    else:
        lihat_akun()
        try:
            index = int(input("Silahkan input nomor akun yang ingin diubah: ")) - 1
            if not (0 <= index < len(jual_akun)):
                print("Nomor akun tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka, tidak boleh huruf atau simbol.")
            return

    id_baru = input("Masukkan ID Akun yang Baru: ")
    nama_baru = input("Masukkan Nama Game baru: ")

    while True:
        harga_baru = input("Masukkan Harga baru (Rp): ")
        if harga_baru.isdigit():
            harga_baru = int(harga_baru)
            break
        else:
            print("Harga hanya boleh berisi angka tanpa huruf atau simbol.")

    while True:
        status_baru = input("Masukkan Status baru (Tersedia/Terjual): ").capitalize()
        if status_baru in ["Tersedia", "Terjual"]:
            break
        else:
            print("Status hanya boleh 'Tersedia' atau 'Terjual' Tidak ada pilihan lain.")

    jual_akun[index] = (id_baru, nama_baru, harga_baru, status_baru)
    print("Data akun telah diupdate")

def hapus_akun():
    print("\nHapus Akun")
    if len(jual_akun) == 0:
        print("Tidak ada data akun.")
        return

    if len(jual_akun) == 1:
        jual_akun.pop(0)
        print("Hanya ada satu akun, Akun akan langsung dihapus.")
    else:
        lihat_akun()
        try:
            index = int(input("Silahkan input nomor akun yang ingin dihapus: ")) - 1
            if 0 <= index < len(jual_akun):
                jual_akun.pop(index)
                print("Akun Telah Terhapus.")
            else:
                print("Nomor akun tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")

while True:
    tampilkan_menu()
    pilihan = input("Silahkan memilih menu (1-5): ")

    if pilihan == "1":
        tambah_akun()
    elif pilihan == "2":
        lihat_akun()
    elif pilihan == "3":
        ubah_akun()
    elif pilihan == "4":
        hapus_akun()
    elif pilihan == "5":
        print("\nTerima kasih telah menjual akun di tempat kami")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")