import random

data_mahasiswa = []
for i in range(1, 101):
    data_mahasiswa.append({
        "nama": f"Mhs_{i}",
        "basis_data": random.randint(50, 100),
        "sistem_operasi": random.randint(50, 100),
        "struktur_data": random.randint(50, 100)
    })

def bubble_sort_matkul(data, key):
    arr = list(data)
    sesi = len(arr)
    perubahan = True
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if arr[j][key] > arr[j - 1][key]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                perubahan = True
            j += 1
        sesi -= 1
    return arr

def tampilkan_top5(matkul, key):
    sorted_data = bubble_sort_matkul(data_mahasiswa, key)
    print(f"\n=== 5 MAHASISWA TERBAIK MATA KULIAH {matkul} ===")
    for idx, mhs in enumerate(sorted_data[:5], 1):
        print(f"{idx}. {mhs['nama']:<8} - Nilai: {mhs[key]}")

tampilkan_top5("BASIS DATA", "basis_data")
tampilkan_top5("SISTEM OPERASI", "sistem_operasi")
tampilkan_top5("STRUKTUR DATA", "struktur_data")