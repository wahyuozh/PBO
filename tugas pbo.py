#kode program functional programming
def luas_segitiga (t, a): #fungsi dengan parameter tinggi dan alas 
    luas_segitiga = 0.5*t*a #rumus untuk menghitung luas segitiga 
    print(luas_segitiga) #memanggil atau me print hasil proses kode program 
luas_segitiga(5,4) #data parameter untuk melalukukan penghitungan luas segitiga 

#kode program OOP
class Aritmatika : #class artitmatika 
    def jumlahkan(self, x,y): #fungsi dengan parameter x,y penjumlahan
        return x+y #mengembalikan nilai untuk x + y 
    def kurangi (self, x,y):  #fungsi dengan parameter x,y penguranagn
        return x-y #mengembalikan nilai untuk x - y 
    def kali(self, x,y): #fungsi dengan parameter x,y perkalian
        return x*y #mengembalikan nilai untuk x * y 
    def bagi (self, x, y): #fungsi dengan parameter x,y pembagian
        return x/y #mengembalikan nilai untuk x / y
    
aritmatika = Aritmatika() #membuat class baru dari aritmatika dengan tanpa parameter
print ("penjumlahan 5 dan 3 adalah : " + str(aritmatika.kali(5, 3))) # memanggil proses perkalian dengan parameter merupakan data yang akan di proses 
