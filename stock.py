class Urun:
    def __init__(self, ad, stok_miktari, fiyat):
        self.ad = ad
        self.stok_miktari = stok_miktari
        self.fiyat = fiyat

class Stok:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)

    def urun_cikar(self, urun):
        self.urunler.remove(urun)

    def stok_goruntule(self):
        for urun in self.urunler:
            print("Ürün adı:", urun.ad)
            print("Stok miktari:", urun.stok_miktari)
            print("Fiyat:", urun.fiyat)

stok = Stok()

while True:
    print("1- Yeni bir ürün ekle")
    print("2- Bir ürünü stoktan çıkar")
    print("3- Mevcut stokları görüntüle")
    print("4- Çıkış yap")

    secim = int(input("Seçiminizi yapın: "))

    if secim == 1:
        ad = input("Ürün adı: ")
        stok_miktari = int(input("Stok miktarı: "))
        fiyat = (input("Fiyat: "))

        urun = Urun(ad, stok_miktari, fiyat)
        stok.urun_ekle(urun)

    elif secim == 2:
        ad = input("Çıkarmak istediğiniz ürünün adını girin: ")
        for urun in stok.urunler:
            if urun.ad == ad:
                stok.urun_cikar(urun)
                print(ad, "stoktan çıkarıldı.")
                break
        else:
            print("Ürün bulunamadı.")

    elif secim == 3:
        stok.stok_goruntule()

    elif secim == 4:
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")