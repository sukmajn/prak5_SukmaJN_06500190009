# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:22:35 2021

@author: Sukma Julia Nada
"""

def mulai():
    while True:
        masuk = input("\nElkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "e":
            break
        else:
            print("Pilih 1 atau 2, e untuk keluar\n")


def elkom1():
    print("--DERET FIBONACCI--")
    jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))

    putaran = 0

    if jumlah_bilangan <= 0:
        print("Jumlah bilangan harus > 0")

    elif jumlah_bilangan == 1:
        pertama = int(input("Masukkan bilangan pertama: "))
        print(pertama)

    else:
        pertama, kedua = int(input("Masukkan bilangan pertama: ")), int(input("Masukkan bilangan kedua: "))
        while putaran < jumlah_bilangan:
            print(pertama)
            ke_n = pertama + kedua
            pertama = kedua
            kedua = ke_n
            putaran += 1


def elkom2():
    konversi, jadwal_kerja, gaji_perhari, gaji_lembur, shift, jam_kerja, lembur, jam_lembur = 60, 8, 175000, 15000, [
        300, 600, 900, 1080], 0, 0, 0

    def sapaan(waktu):
        if shift[0] <= waktu <= shift[1]:
            print("Selamat Pagi")

        elif shift[1] <= waktu <= shift[2]:
            print("Selamat Siang")

        elif shift[2] <= waktu <= shift[3]:
            print("Selamat Sore")

        else:
            print("Selamat Malam")

    print("--HITUNG GAJI HARIAN--")

    str_masuk = str(input("Jam masuk kerja: "))
    masuk_splitted = str_masuk.split('.')
    waktu_masuk = (int(masuk_splitted[0]) * konversi) + int(masuk_splitted[1])
    sapaan(waktu_masuk)

    str_keluar = str(input("Jam keluar kerja: "))
    keluar_splitted = str_keluar.split('.')
    waktu_keluar = (int(keluar_splitted[0]) * konversi) + int(keluar_splitted[1])
    sapaan(waktu_keluar)

    print("--RINCIAN GAJI--")

    if waktu_keluar > waktu_masuk:
        jam_kerja = (waktu_keluar - waktu_masuk) // konversi

    else:
        jam_kerja = ((1440 - waktu_masuk) + waktu_keluar) // konversi

    print("Waktu Kerja\t:", jam_kerja, "Jam", "(" + str_masuk, "s/d", str_keluar + ")")
    print("Gaji per Hari\t: Rp.", str(f'{gaji_perhari:,}').replace(',', '.'))

    if jam_kerja > 8:
        jam_lembur = jam_kerja - jadwal_kerja
        lembur = gaji_lembur * jam_lembur

    print("Lembur\t\t: Rp.", str(f'{lembur:,}').replace(',', '.'), "(" + str(jam_lembur), "jam x @ Rp. 15.000)")

    print("Total_gaji\t: Rp.", str(f'{gaji_perhari + lembur:,}').replace(',', '.'))


if __name__ == "__main__":
    mulai()