# Görev: Bir Urun sınıfı oluşturun.
# • Gereksinimler:
# • Sınıf seviyesinde urun_adet adında bir değişken tanımlayın (başlangıç
# değeri 0).
# • __init__ içinde her yeni ürün oluşturulduğunda urun_adet değişkenini 1
# artırın.
# • @classmethod olarak toplam_urun_sayisini_getir() adında bir metot yazın
# ve bu metot mevcut ürün sayısını ekrana yazdırsın.

class Urun:
    urun_adet = 0
    def __init__(self, urun):
        self.urun = urun
        Urun.urun_adet += 1

    @classmethod
    def urun_sayisini_getir(cls):
        return f"Şu ana kadar {cls.urun_adet} adet ürün oluşturuldu."

urun1 = Urun("Ürün1")
urun2 = Urun("Ürün2")
urun3 = Urun("Ürün3")


print(Urun.urun_sayisini_getir())
