a= 30
b= 5
print (a+b)
print (a-b)
print (a/b)
print (a*b)

print ("program operasi matematika sederhana ")
#masukkan Angka 
a = int(input("masukkan angka a: "))
b = int(input("masukkan angka b: "))

#Operasi aritmatika
Penjumlahan = a+b 
Pengurangan = a-b
Perkalian = a*b
#cegah pembagian dengan nol
if b !=0:
    pembagian = a/b
else:
    pembagian="tidak bisa dibagi dengan nol"

#Hasil
print("Hasil operasi") 
print("penjumlahan :", Penjumlahan)   
print("pengurangan :", Pengurangan)
print("perkalian :", Perkalian)
print("pembagian :", pembagian)
