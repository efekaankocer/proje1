import islemler

while True:
    print("\n╔═════════════════════╗")
    print("║   HESAP MAKİNESİ    ║")
    print("║                     ║")
    print("║  1-toplama          ║")
    print("║  2-çıkarma          ║")
    print("║  3-çarpma           ║")
    print("║  4-bölme            ║")
    print("║  5-üs alma          ║")
    print("║  6-kare             ║")
    print("║  7-karekök          ║")
    print("║  8-kalan alma       ║")
    print("║  9-mutlak değer     ║")
    print("║  10-KDV Hesaplama   ║")
    print("║  0-çıkış            ║")
    print("╚═════════════════════╝")

    secim = input("Seçiminiz: ")

    if secim == "1":
        islemler.toplama()
    elif secim == "2":
        islemler.cikarma()
    elif secim == "3":
        islemler.carpma()
    elif secim == "4":
        islemler.bolme()
    elif secim == "5":
        islemler.us_alma()
    elif secim == "6":
        islemler.kare()
    elif secim == "7":
        islemler.karekok()
    elif secim == "8":
        islemler.kalan_alma()
    elif secim == "9":
        islemler.mutlak_deger()
    elif secim == "10":
        islemler.kdv_hesapla()
    elif secim == "0":
        print("Çıkış yapıldı.")
        break
    else:
        print("Hatalı seçim!")
