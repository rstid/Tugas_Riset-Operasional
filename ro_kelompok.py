from tabulate import tabulate
import os

clear = lambda: os.system('clear')

# Mendefinisikan fungsi
def sumber_tempat(nomor):
    if nomor == 1:
        return "Jakarta"
    elif nomor == 2:
        return "Bekasi"
    elif nomor == 3:
        return "Tanggerang"
    else:
        return "Tidak ada"

def tujuan_tempat(nomor):
    if nomor == 1:
        return "Cirebon"
    elif nomor == 2:
        return "Bandung"
    elif nomor == 3:
        return "Sukabumi"
    else:
        return "Tidak ada"

clear()

# Inisialisasi biaya unit, kebutuhan tujuan
biaya_unit = []

print("= = = = = = Masukkan biaya unit dari sumber ke tujuan. = = = = = =")
for i in range(3):
    row = []
    for j in range(3):
        while True:
            try:
                nilai = int(input(f"Masukkan Biaya Dari {sumber_tempat(i+1)} ke {tujuan_tempat(j+1)}: "))
                if nilai > 0:
                    break
                else:
                    print("Harap masukan biaya")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        row.append(nilai)
    biaya_unit.append(row)

# Daftar baris dan kolom yang akan dicetak
baris_sumber = ["Jakarta", "Bekasi", "Tangerang"]
kolom_tujuan = ["Cirebon", "Bandung", "Sukabumi"]

# Membuat list berdasarkan baris yang akan dicetak
data = []
for i in range(len(biaya_unit)):
    if i < len(baris_sumber):
        row = [baris_sumber[i]]
        for j in range(len(biaya_unit[i])):
            if j < len(kolom_tujuan):
                row.append(biaya_unit[i][j])
        data.append(row)

clear()

# Mencetak tabel menggunakan tabulate
table = tabulate(data, headers=[""] + kolom_tujuan, tablefmt="grid")
print(table)

print("")

# Inisialisasi Kapasitas Pemasok
print("= = = = = = Masukan Kapasitas Pemasok = = = = = =")
kapasitas_pemasok = []
for i in range(3):
    while True:
        try:
            kapasitas = int(input(f"Kapasitas pemasok {sumber_tempat(i+1)}: "))
            if kapasitas > 0:
                break
            else:
                print("Harap masukan kapasitas pemasok")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    kapasitas_pemasok.append(kapasitas)

    

print("")

# Inisialisasi Kebutuhan Tujuan
print("= = = = = = = = Masukan Kebutuhan = = = = = = = =")
kebutuhan_tujuan = []
for i in range(3):
    while True:
        try:
            kebutuhan = int(input(f"Kebutuhan tujuan {tujuan_tempat(i+1)}: "))
            if kebutuhan > 0:
                break
            else:
                print("Harap masukan kebutuhan tujuan")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    kebutuhan_tujuan.append(kebutuhan)   

print("")

# Inisialisasi variabel untuk menyimpan jumlah unit yang dikirimkan
jumlah_unit_dikirim = [[0, 0, 0] for _ in range(3)]

# Fungsi untuk menentukan sel berikutnya dengan biaya terendah
def cari_sel_terendah(biaya_unit, kapasitas_pemasok, kebutuhan_tujuan):
    min_biaya = float('inf')
    min_i, min_j = -1, -1

    for i in range(len(biaya_unit)):
        for j in range(len(biaya_unit[0])):
            if biaya_unit[i][j] < min_biaya and kapasitas_pemasok[i] > 0 and kebutuhan_tujuan[j] > 0:
                min_biaya = biaya_unit[i][j]
                min_i, min_j = i, j

    return min_i, min_j

# Algoritma Least Unit Cost
while True:
    i, j = cari_sel_terendah(biaya_unit, kapasitas_pemasok, kebutuhan_tujuan)
    if i == -1:
        break

    unit_yang_dikirim = min(kapasitas_pemasok[i], kebutuhan_tujuan[j])
    jumlah_unit_dikirim[i][j] = unit_yang_dikirim
    kapasitas_pemasok[i] -= unit_yang_dikirim
    kebutuhan_tujuan[j] -= unit_yang_dikirim

# Menampilkan hasil
print("= = = = = = = = = = = HASIL = = = = = = = = = = = =")
for i in range(len(biaya_unit)):
    for j in range(len(biaya_unit[0])):
        if jumlah_unit_dikirim[i][j] > 0:
            int_Sumber = i + 1
            int_dst_Tujuan = j + 1

            print(f"Sumber daya {sumber_tempat(int_Sumber)} -> Tujuan {sumber_tempat(int_dst_Tujuan)}: {jumlah_unit_dikirim[i][j]} unit")
