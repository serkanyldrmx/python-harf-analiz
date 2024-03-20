# Harf istatistiklerini hesaplamak için modülümüzü kullanma
import harf_istatistikleri

# Test metni
test_metni = """
Bu bir test metnidir. Bu metin içinde harflerin frekanslarını hesaplayacağız. 
Ödev için hazırlanmıştır ve harf istatistikleri modülü ile test edilecektir.
"""

# Harf istatistiklerini hesapla ve ekrana yazdır
frekanslar = harf_istatistikleri.harf_frekansi_hesapla(test_metni)
for harf, oran in frekanslar.items():
    print(f"{harf}: %{oran:.2f}")

# Modül yazarı bilgisini ve notu ekrana yazdır
harf_istatistikleri.bilgi_ver()
