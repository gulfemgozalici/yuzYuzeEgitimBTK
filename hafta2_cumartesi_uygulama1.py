# Görev: Bir Ogrenci sınıfı oluşturun.
# • Gereksinimler:
# • __init__ metodu ile öğrencinin ad, soyad ve ders_notu değerlerini alın.
# • durum_sorgula() adında bir instance metodu yazın. Bu metot, öğrencinin
# notu 50 ve üzerindeyse "Başarılı", değilse "Başarısız" döndürsün.
# • 2 farklı öğrenci nesnesi oluşturup durum_sorgula() metodunu test edin.

class Ogrenci:
    def __init__(self, ad, soyad, ders_notu):
        self.ad = ad
        self.soyad = soyad
        self.ders_notu = ders_notu

    def durum_sorgula(ad, soyad, ders_notu):
        if ders_notu > 50:
            return f"{ad} {soyad} => Başarılı, Ders Notu = {ders_notu}"
        else:
            return f"{ad} {soyad} => Başarısız, Ders Notu = {ders_notu}"

ogrenci1 = Ogrenci("Ad1", "Soyad1", 86)
ogrenci2 = Ogrenci("Ad2", "Soyad2", 48)
ogrenci3 = Ogrenci("Ad3", "Soyad3", 23)
ogrenci4 = Ogrenci("Ad4", "Soyad4", 78)

print(Ogrenci.durum_sorgula(ogrenci1.ad, ogrenci1.soyad, ogrenci1.ders_notu))
print(Ogrenci.durum_sorgula(ogrenci2.ad, ogrenci2.soyad, ogrenci2.ders_notu))
print(Ogrenci.durum_sorgula(ogrenci3.ad, ogrenci3.soyad, ogrenci3.ders_notu))
print(Ogrenci.durum_sorgula(ogrenci4.ad, ogrenci4.soyad, ogrenci4.ders_notu))

