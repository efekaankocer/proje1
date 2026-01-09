import math

def toplama():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a + b)

def cikarma():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a - b)

def carpma():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a * b)

def bolme():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    if b == 0:
        print("Hata: Sıfıra bölünemez!")
    else:
        print("Sonuç:", a / b)

def us_alma():
    a = float(input("Taban: "))
    b = float(input("Üs: "))
    print("Sonuç:", a ** b)

def kare():
    a = float(input("Sayı: "))
    print("Sonuç:", a ** 2)

def karekok():
    a = float(input("Sayı: "))
    if a < 0:
        print("Negatif sayının karekökü alınamaz")
    else:
        print("Sonuç:", math.sqrt(a))

def kalan_alma():
    a = int(input("1. sayı: "))
    b = int(input("2. sayı: "))
    print("Sonuç:", a % b)

def mutlak_deger():
    a = float(input("Sayı: "))
    print("Sonuç:", abs(a))

def kdv_hesapla():
    fiyat = float(input("Ürün fiyatı: "))
    kdv_oran = float(input("KDV oranı (%): "))
    kdv_tutar = fiyat * kdv_oran / 100
    toplam = fiyat + kdv_tutar
    print("KDV tutarı:", kdv_tutar)
    print("KDV dahil fiyat:", toplam)

