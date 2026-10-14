def insertionSort(myList):
    for index in range(1, len(myList)):
        Kanan = myList[index]
        Kiri = index - 1
        while Kiri >= 0 and myList[Kiri] > Kanan:
            myList[Kiri + 1] = myList[Kiri]
            Kiri -= 1
        myList[Kiri + 1] = Kanan

index = 0
panjangList = int(input("Panjang data yang diinginkan = "))
myList = []
for i in range(1, panjangList + 1):
    angka = int(input("Masukan data yang ke %i untuk List = " % i))
    myList.append(angka)

print("Sebelum di insertion sort = ")
print(myList)
insertionSort(myList)
print("Setelah di insertion sort = ")
print(myList)