data_karyawan = [
    {"nama": "Andi", "gaji": 7500000},
    {"nama": "Budi", "gaji": 4500000},
    {"nama": "Cici", "gaji": 9000000},
    {"nama": "Deni", "gaji": 3500000},
    {"nama": "Eka", "gaji": 6000000},
    {"nama": "Fani", "gaji": 8200000},
    {"nama": "Gita", "gaji": 5000000},
    {"nama": "Hadi", "gaji": 10000000},
    {"nama": "Indra", "gaji": 4000000},
    {"nama": "Joko", "gaji": 6500000}
]

def insertion_sort_gaji(data):
    arr = list(data)
    for index in range(1, len(arr)):
        kanan = arr[index]
        kiri = index - 1
        while kiri >= 0 and arr[kiri]["gaji"] > kanan["gaji"]:
            arr[kiri + 1] = arr[kiri]
            kiri -= 1
        arr[kiri + 1] = kanan
    return arr

def selection_sort_gaji(data):
    arr = list(data)
    for slot in range(len(arr) - 1):
        position = slot
        for location in range(len(arr) - 1, slot, -1):
            if arr[location]["gaji"] < arr[position]["gaji"]:
                position = location
        temp = arr[slot]
        arr[slot] = arr[position]
        arr[position] = temp
    return arr

print("--- DATA AWAL KARYAWAN ---")
for k in data_karyawan:
    print(f"Nama: {k['nama']:<10} | Gaji: Rp {k['gaji']:,}")

print("\n--- URUTAN GAJI (INSERTION SORT) ---")
hasil_insertion = insertion_sort_gaji(data_karyawan)
for k in hasil_insertion:
    print(f"Nama: {k['nama']:<10} | Gaji: Rp {k['gaji']:,}")

print("\n--- URUTAN GAJI (SELECTION SORT) ---")
hasil_selection = selection_sort_gaji(data_karyawan)
for k in hasil_selection:
    print(f"Nama: {k['nama']:<10} | Gaji: Rp {k['gaji']:,}")