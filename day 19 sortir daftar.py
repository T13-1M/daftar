import os

os.system("cls")

data = []
def tambah_data():
    berapa = int(input("Ada berapa data? "))

    for tambah in range(berapa):
        tambah = str(input("Masukkan data: "))

        with open("30 day python challenge/day 19.txt", "a", encoding="utf-8") as f:
            f.write(f"{tambah}\n")

        print("Data berhasil di tambahkan.\n")

def lihat_data():
    with open("30 day python challenge/day 19.txt", "r") as f:
        lihat = f.readlines()

        for i, no in enumerate(lihat):
            print(f"{i+1}. {no.strip()}")

    return lihat

def hapus_data():
    print("--- Pilih Data Untuk Dihapus ---")

    semua_data = lihat_data()

    if not semua_data:
        print("Data masih kosong, tidak ada yang bisa dihapus.")
        return 

    try:
        hapus = int(input("Masukkan nomor data yang akan dihapus: "))

        if 1 <= hapus <= len(semua_data):
            semua_data.pop(hapus - 1)

            with open("30 day python challenge/day 19.txt", "w") as f:
                f.writelines(semua_data)

            print(f"\nData nomor {hapus} berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")


while True:
    pilih = input('''
1. Tambah Data
2. Lihat Data
3. Hapus Data
4. Keluar

Masukkan pilihan: ''')

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        lihat_data()
    elif pilih == "3":
        hapus_data()
    elif pilih == "4":
        print("Keluar . . .")
        break
    else:
        print("Pilihan tidak valid.")
        continue

    input("Tekan Enter untuk kembali ke menu . . .")
    os.system("cls")