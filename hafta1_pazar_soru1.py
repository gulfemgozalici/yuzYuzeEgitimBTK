#Soru 1
"""
 Görev: Bir islem_merkezi(sayi1, sayi2) fonksiyonu yazın.
• Detay: Bu fonksiyonun içinde toplama, cikarma ve bolme adında 3
iç fonksiyon olsun.
• Çıktı: Ana fonksiyon çağrıldığında bu 3 işlemi de yapıp sonuçları
bir sözlük (dictionary) olarak döndürsün.
• Örn: {"toplam": 15, "fark": 5, "bolum": 2}
"""
def islem_merkezi(sayi1, sayi2):
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    def toplama(sayi1, sayi2):
        return sayi1 + sayi2
    def cikarma(sayi1, sayi2):
        return sayi1 - sayi2
    def bolme(sayi1, sayi2):
        return sayi1 / sayi2
    sonuc = {"Toplama": toplama(sayi1, sayi2), "Çıkarma": cikarma(sayi1, sayi2), "Bölme": bolme(sayi1, sayi2)}
    return sonuc

sayi1 = input("1. sayı = ")
sayi2 = input("2. sayı = ")

print(islem_merkezi(sayi1, sayi2))

