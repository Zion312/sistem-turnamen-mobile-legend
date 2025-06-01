import random

# list utama untuk menyimpan tim
daftar_tim = []

# menambahkan tim
def tambah_tim():
    nama = input("Masukkan nama tim: ")
    daftar_tim.append(nama)
    print(f"Tim '{nama}' berhasil ditambahkan.\n")

# menyisipkan tim di posisi tertentu
def sisip_tim():
    nama = input("Masukkan nama tim: ")
    try:
        posisi = int(input("Masukkan posisi penyisipan: "))
        daftar_tim.insert(posisi, nama)
        print(f"Tim '{nama}' disisipkan di posisi {posisi + 1}.\n")
    except ValueError:
        print("Posisi harus berupa angka!\n")

# menghapus tim
def hapus_tim():
    nama = input("Masukkan nama tim yang ingin dihapus: ")
    if nama in daftar_tim:
        daftar_tim.remove(nama)
        print(f"Tim '{nama}' berhasil dihapus.\n")
    else:
        print(f"Tim '{nama}' tidak ditemukan.\n")

# menampilkan semua tim
def tampil_tim():
    if not daftar_tim:
        print("Belum ada tim yang terdaftar.\n")
    else:
        print("Daftar Tim:")
        for i, tim in enumerate(daftar_tim, 1):
            print(f"{i}. {tim}")
        print()

# membuat dan menampilkan jadwal pertandingan
def buat_jadwal():
    if len(daftar_tim) < 2:
        print("Minimal harus ada 2 tim untuk membuat jadwal.\n")
        return [], []

    acak = daftar_tim.copy()
    random.shuffle(acak)
    jadwal = []
    while len(acak) >= 2:
        tim1 = acak.pop()
        tim2 = acak.pop()
        jadwal.append((tim1, tim2))

    if acak:
        print(f"Tim '{acak[0]}' otomatis lolos karena jumlah tim ganjil.")

    print("\nJadwal Pertandingan:")
    for match in jadwal:
        print(f"{match[0]} vs {match[1]}")
    print()

    return jadwal, acak

# menampilkan hasil pertandingan
def hasil_pertandingan(jadwal):
    hasil = []
    print("Hasil Pertandingan:")
    for match in jadwal:
        pemenang = random.choice(match)
        hasil.append(pemenang)
        print(f"{match[0]} vs {match[1]} => Pemenang: {pemenang}")
    return hasil

# menampilkan peringkat akhir
def tampilkan_peringkat(pemenang_list, lolos=[]):
    ranking = list(set(pemenang_list + lolos))
    ranking.sort()
    print("\n=== PERINGKAT AKHIR ===")
    for i, tim in enumerate(ranking, 1):
        print(f"{i}. {tim}")
    print()

# menu utama
def menu():
    while True:
        print("=== SISTEM TURNAMEN MOBILE LEGEND ===")
        print("1. Tambah Tim")
        print("2. Sisip Tim")
        print("3. Hapus Tim")
        print("4. Lihat Daftar Tim")
        print("5. Buat Jadwal & Tandingkan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '1':
            tambah_tim()
        elif pilihan == '2':
            sisip_tim()
        elif pilihan == '3':
            hapus_tim()
        elif pilihan == '4':
            tampil_tim()
        elif pilihan == '5':
            jadwal, lolos = buat_jadwal()
            if jadwal:
                hasil = hasil_pertandingan(jadwal)
                tampilkan_peringkat(hasil, lolos)
        elif pilihan == '0':
            print("Terima kasih telah menggunakan sistem turnamen!")
            break
        else:
            print("Pilihan tidak valid.\n")

# menjalankan aplikasi
menu()
