def harf_frekansi(metin):
    harf_sayilari = {}
    for harf in metin:
        if harf.isalpha():  # Sadece harfleri say
            harf = harf.lower()  # Büyük-küçük harf ayrımı yapma
            if harf in harf_sayilari:
                harf_sayilari[harf] += 1
            else:
                harf_sayilari[harf] = 1

    toplam_harf_sayisi = sum(harf_sayilari.values())
    harf_oranlari = {harf: (sayi / toplam_harf_sayisi) * 100 for harf, sayi in harf_sayilari.items()}
    return harf_oranlari

def metin_uzunluklarina_gore_harf_orani_hesapla(metin):
    sonuclar = {}
    for uzunluk in [100, 1000, 10000]:
        kesit = metin[:uzunluk]
        frekanslar = harf_frekansi(kesit)
        sonuclar[f"İlk {uzunluk} Karakter"] = frekanslar
    return sonuclar

# Test metni
test_metni = """
Burada örnek bir metin var. Bu metin, Türkçe karakterlerle dolu bir örnektir. 
Ödev için test edilecek ve harf frekanslarını hesaplayacak bir uygulama geliştiriyoruz. 
Herkesin ödevini kolaylıkla test edebilmesi için örnek metni buraya ekliyoruz.
"""

# Metin uzunluklarına göre harf oranlarını hesapla
sonuclar = metin_uzunluklarina_gore_harf_orani_hesapla(test_metni)
for uzunluk, frekanslar in sonuclar.items():
    print(uzunluk + ":")
    for harf, oran in frekanslar.items():
        print(f"{harf}: %{oran:.2f}")
    print()
