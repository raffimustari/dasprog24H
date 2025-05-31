def reverse_per_kata(kalimat):
    kata_list = kalimat.split()
    hasil_balik = [kata[::-1] for kata in kata_list]
    return ' '.join(hasil_balik)

def urutkan_kalimat(kalimat, urutan):
    kata_list = kalimat.split()
    hasil_urut = []
    for idx in urutan:
        if 1 <= idx <= len(kata_list):
            hasil_urut.append(kata_list[idx - 1])
        else:
            hasil_urut.append('')
    return ' '.join(hasil_urut)

def ganti_vokal(kalimat, opsi):
    pengganti_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'}
    pengganti_besar = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'}
    hasil = ''
    for char in kalimat:
        if opsi == 1 and char in pengganti_kecil:
            hasil += pengganti_kecil[char]
        elif opsi == 2 and char in pengganti_besar:
            hasil += pengganti_besar[char]
        else:
            hasil += char
    return hasil

print("Hasil reverse_per_kata:")
print(reverse_per_kata("AKU CINTA KAMU"))

print("\nHasil urutkan_kalimat:")
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))

print("\nHasil ganti_vokal (opsi 1):")
print(ganti_vokal("Aku Cinta Kamu", 1))

print("\nHasil ganti_vokal (opsi 2):")
print(ganti_vokal("Aku Cinta Kamu", 2))