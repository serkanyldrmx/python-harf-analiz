def harf_mi(karakter):
    """Karakterin bir harf olup olmadığını kontrol eder."""
    return karakter.isalpha()

def kucuk_harf_yap(karakter):
    """Gelen karakteri küçük harfe dönüştürür."""
    return karakter.lower()

def harf_sikligi_hesapla(metin):
    """Gelen metindeki harflerin kullanım sıklığını yüzdelik oran olarak hesaplar."""
    harf_sayisi = {}
    toplam_harfler = 0

    for karakter in metin:
        if karakter.isalpha():
            karakter = karakter.lower()
            harf_sayisi[karakter] = harf_sayisi.get(karakter, 0) + 1
            toplam_harfler += 1

    frekanslar = {harf: sayi / toplam_harfler * 100 for harf, sayi in harf_sayisi.items()}

    return frekanslar

def bilgi_ver():
    """Modülü kullanan kişiye bilgi verir."""
    print("Bu modül, harf kontrolü, harfleri küçük harfe dönüştürme ve harf sıklığı hesaplama fonksiyonları içerir.")
    print("Oluşturan: Serkan yıldırım")
    print("Öğrenci Numarası: 211220028")
    print("Not: Python herkesin anlayabileceği ve kullanabileceği güçlü bir programlama dilidir.")

# Modülü çağırıldığında bilgi ver
bilgi_ver()
