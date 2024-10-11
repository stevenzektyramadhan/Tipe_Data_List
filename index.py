# PYTHON LIST
buah = ["apel", "anggur", "jambu","jeruk"]
angka = [1,2,3,4,5]
print(buah[1])
print(angka[2])
# mengganti nilai
buah[1] = "cherry"
print(buah[1])

# insert data
# append
buah.append("rambutan")
print(buah[4])
# insert digunakan untuk menambah value dengan menentukan indexnya
buah.insert(2,"cabik")
print(buah[3])
# extend untuk menggabunhkan nilai variable dengan variabel sebelumnya
baru = ["berry","ubi","tomat"]
buah.extend(baru)
print(buah)

# MENGHAPUS DATA
# pop() untuk menghapus data di akhir dan untuk spesifik index
buah.pop()
print(buah)
# remove() untuk menghapus data menggunakan nama nilainya
buah.remove("ubi")
print(buah)
#  del untuk menghapus spesifik index atau menghapus semua nilai dari var
# spesifik
del buah[0]
print(buah)
# del + var
"""
del buah
print(buah)
"""
# clear() untuk menghapus nilai dari var
buah.clear()
print(buah)

# menampilkan data secara urut
buah = ["bawang","cabe","apel"]
buah.sort()
print(buah)

# check
if "apel" in buah :
    print("ada apel di dalam variabel buah")
    