#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data_mahasiswa = []

def tambah_data():
    nim = input("Masukkan NIM (11 digit): ")
    if len(nim) != 11 or not nim.isdigit():
        print("NIM harus 11 digit angka.")
        return

    nama = input("Masukkan NAMA (min 6 karakter): ")
    if len(nama) < 6:
        print("Nama minimal 6 karakter.")
        return

    alamat = input("Masukkan ALAMAT (min 10 karakter): ")
    if len(alamat) < 10:
        print("Alamat minimal 10 karakter.")
        return

    kelas = input("Masukkan KELAS (TI24H, TI24A, TI24G, TI24F): ").upper()
    if kelas not in ["TI24H", "TI24A", "TI24G", "TI24F"]:
        print("Kelas tidak valid.")
        return

    mahasiswa = {
        "NIM": nim,
        "NAMA": nama,
        "ALAMAT": alamat,
        "KELAS": kelas
    }
    data_mahasiswa.append(mahasiswa)
    print("Data berhasil ditambahkan.\n")

def tampilkan_data():
    if not data_mahasiswa:
        print("Belum ada data.")
    else:
        print("\n Data Mahasiswa:")
        for i, mhs in enumerate(data_mahasiswa, 1):
            print(f"{i}. {mhs['NIM']} - {mhs['NAMA']} - {mhs['ALAMAT']} - {mhs['KELAS']}")
    print()

while True:
    print("=== MENU ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ") 

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        print(" Keluar dari program.")
        break
    else:
        print(" Pilihan tidak valid.\n")

