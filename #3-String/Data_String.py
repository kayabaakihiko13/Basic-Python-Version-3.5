"""==== Pengenalan String ===="""
kalimat="Halooo Iqbal-san"
print(kalimat)

"""====operation and manipulation string===
*note: "\manipulasi string ada banyak \""""

# 1.menyambungkan string()

namaDepan="Iqbal"
namatengah="Ramadhan"
namaakhir="Anniswa"
nama=namaDepan+" "+namatengah+' '+namaakhir
print(nama)
#2.menghitung panjang string
panjang= len(namaDepan)
print(panjang)
#3.operator untuk string
##mengecheck sebuah char atau sting
check="z"
status=check in nama
print(check+"it in inside of"+nama+" "+str(status))

#mengulangi string
print(10*"baka")
#indexing 
print("index ke-->0: "+nama[0])
print("index ke-->4: "+nama[4])
print("index ke-->(-2): "+nama[-2])
#slicing
print("slicing (0,4): "+nama[:4])
print("slicing (2,7): "+nama[2:7])
##slicing with step(start:end:step)
print("slicing (0,4): "+nama[:4:2])
print("slicing (2,7): "+nama[2:7:2])

#item paling besar 
print("paling besar: "+max(nama))
ascii_code=ord("w")
print("ascii code dari: "+max(nama)+"adalah"+str(ascii_code))
#item paling kecil
print("paling kecil: "+min(nama))
ascii_code=ord(" ")
print("ascii code dari:"+min(nama)+"adalah"+str(ascii_code))

## merubah case dari string
### merubah semua ke upper case 
salam="brrroooo!!!!!"
salam=salam.upper()
print(salam)
### merubah semua menjadi lower case
kata="AKuuu otONg"
kata=kata.lower()
print(kata)

## pengecheckan dengan isX method
#pengecheckan lowercase
kata="baka"
print(kata.islower())
#mengcheckan uppercase
kata="AYAM"
print("apakah"+kata+"itu uppercase?="+str(kata.isupper()))
print(nama.isalpha())#bersifat katanya kecil semua atau besar semua

##mengecheck komponen starswith() endswith()
#startswith()
nama_starstwith=nama.startswith("Iqbal")
print(nama_starstwith)#berouput True karna sesuai dengan string berada di depan
nama_starstwith=nama.startswith("Joko")
print(nama_starstwith)#berouput False karna sesuai dengan string berada di depan

##penggunaan  .join() and .split()
#.join() --> berfungsi sebagai menggabungkan string di pada kondisi terpisah
l=["aku","suka","makan","Ramen"]#for information list can fill element one type data or variation type data etc
gabung=" ".join(l)
print(gabung)
li=("aku","adalah","mahasiswa")
gabung_2=",".join(li)
print(gabung_2)
#.split()
pisah=gabung.split()
print(pisah)
UNgroup=gabung_2.split()
print(UNgroup)
