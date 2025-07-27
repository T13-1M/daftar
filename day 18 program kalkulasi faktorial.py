def faktorial(n):
    """ Fungsi faktorial """

    if n < 0:
        print("Harus bilangan positif tidak boleh di bawah 0.")
    elif n == 0:
        return 1
    
    else:
        hasil = 1

        for i in range(1, n + 1):
            hasil = hasil * i
        return hasil
try:
    user = int(input("Masukkan angka untuk hitungan faktorial: "))

    hasil = faktorial(user)

    print(f"Hasil dari faktorial dari {user} adalah {hasil}")

except ValueError:
    print("Input harus angka gk boleh yang lain.")