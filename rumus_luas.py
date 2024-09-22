import time
import math

#mengelompokan rumus
def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari):
    return math.pi* jari_jari**2

def luas_trapesium(sisi_a, sisi_b, tinggi):
    return 0.5 * (sisi_a + sisi_b) * tinggi

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

#user interface
print ("------------------------------")
print ("|      KALKULATOR  LUAS      |")
print ("|       by Ben Timothy       |")
localtime = time.asctime (time.localtime(time.time()))
print ("| ",localtime," |")
print ("------------------------------")
print ("ketik 'help' jika membutuhkan bantuan")
print (" ")

#input bangun datar
def inputcommand():
    print (" ")
    print ("Masukan Perintah!")
    ic = input("> ")

    if (ic == "help"):
        print("List Command")
        print("- Persegi = 'p'")
        print("- Persegi Panjang = 'pp'")
        print("- Segitiga = 's'")
        print("- Lingkaran = 'l'")
        print("- Trapesium = 't'")
        print("- Jajar Genjang = 'jg'")
        print("- Keluar = 'esc'")

    elif (ic == "esc"):
        print("---------------")
        print("| Terimakasih |")
        print("---------------")
        return

    elif (ic == "p"):
        print("Masukan Panjang Sisi!")
        sisi = float(input("> "))  
        print(" ")
        print("---------------------------")
        print(f"Luas Persegi : {luas_persegi(sisi)} ")
        print("---------------------------")     

    elif (ic == "pp"):
        print("Masukan Panjang!")
        panjang = float(input("> ")) 
        print("Masukan Lebar!")
        lebar = float(input("> "))  
        print(" ")
        print("-------------------------------")
        print(f"Luas Persegi Persegi : {luas_persegi_panjang(panjang, lebar)} ")
        print("-------------------------------")

    elif (ic == "s"):
        print("Masukan Alas!")
        alas = float(input("> ")) 
        print("Masukan Tinggi!")
        tinggi = float(input("> "))  
        print(" ")
        print("-------------------------------")
        print(f"Luas Segitiga : {luas_segitiga(alas, tinggi)} ")
        print("-------------------------------")

    elif (ic == "l"):
        print("Masukan Jari-Jari!")
        jari_jari = float(input("> "))  
        print(" ")
        print("---------------------------")
        print(f"Luas Lingkaran : {luas_persegi(jari_jari)} ")
        print("---------------------------")

    elif (ic == "t"):
        print("Masukan Sisi 1!")
        sisi_a = float(input("> ")) 
        print("Masukan Sisi 2!")
        sisi_b = float(input("> ")) 
        print("Masukan Tinggi!")
        tinggi = float(input("> "))  
        print(" ")
        print("-------------------------------")
        print(f"Luas Trapesium : {luas_trapesium(sisi_a, sisi_b, tinggi)} ")
        print("-------------------------------")

    elif (ic == "jg"):
        print("Masukan Alas!")
        alas = float(input("> ")) 
        print("Masukan Tinggi!")
        tinggi = float(input("> "))  
        print(" ")
        print("-------------------------------")
        print(f"Luas Jajar Genjang : {luas_jajar_genjang(alas, tinggi)} ")
        print("-------------------------------")

    else:
        print("Perintah Salah!!")
        print("Harap Ulangi Perintah Anda.")
        print(" ")

    inputcommand ()
inputcommand()