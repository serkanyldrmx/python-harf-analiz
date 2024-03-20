def frekans_analizi(metin):
    harf_sayısı = {}
    toplam_harfler = 0

    for karakter in metin:
        if karakter.isalpha():
            karakter = karakter.lower()
            harf_sayısı[karakter] = harf_sayısı.get(karakter, 0) + 1
            toplam_harfler += 1

    frekanslar = {harf: sayı / toplam_harfler * 100 for harf, sayı in harf_sayısı.items()}

    return frekanslar, harf_sayısı

def sonuçları_yazdır(frekanslar, harf_sayısı):
    print("Harf  Frekansı  Geçiş Sayısı")
    for harf, frekans in frekanslar.items():
        print(f"{harf}:    {frekans:.2f}%     {harf_sayısı[harf]}")

metin = """Burada bir metin örneği olarak kullanabileceğiniz uzun bir metin bulunmalıdır.
Bu metin Türkçe, İngilizce veya Almanca olabilir. Önemli olan metnin uzunluğudur.
Çünkü daha uzun metinler, harflerin frekansını daha doğru bir şekilde belirlememize olanak sağlar."""

for uzunluk in [100, 1000, 10000]:
    kısmi_metin = metin[:uzunluk]
    print(f"\nMetnin ilk {uzunluk} karakteri için frekans analizi:")
    frekanslar, harf_sayısı = frekans_analizi(kısmi_metin)
    sonuçları_yazdır(frekanslar, harf_sayısı)
