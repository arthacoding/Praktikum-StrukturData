def tukar(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]

def bubble(listku):
    perubahan = True
    sesi = len(listku)
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j] < listku[j - 1]:
                perubahan = True
                tukar(listku, j, j - 1)
            j += 1
        print(listku)
        if not perubahan:
            print("hasil akhir = %s" % str(listku))
        sesi -= 1

# Input data mandiri oleh user
panjangList = int(input("Masukkan jumlah data yang diinginkan: "))
mylist = []
for i in range(1, panjangList + 1):
    angka = int(input("Masukkan data ke-%i: " % i))
    mylist.append(angka)

print("==================================================")
print("Sebelum Bubble Sort:")
print(mylist)
print("Setelah Bubble Sort:")
bubble(mylist)