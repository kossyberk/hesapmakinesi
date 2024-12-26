import tkinter as tk

def toplam():
    sonuc = float(sayi1.get()) + float(sayi2.get())
    guncelle_sonuc(sonuc)

def cikar():
    sonuc = float(sayi1.get()) - float(sayi2.get())
    guncelle_sonuc(sonuc)

def carp():
    sonuc = float(sayi1.get()) * float(sayi2.get())
    guncelle_sonuc(sonuc)

def bol():
    try:
        sonuc = float(sayi1.get()) / float(sayi2.get())
        guncelle_sonuc(sonuc)
    except ZeroDivisionError:
        toplami.config(text="Hata: Bölme sıfıra yapılamaz!")

def sifirla():
    sayi1.delete(0, tk.END)
    sayi2.delete(0, tk.END)
    toplami.config(text="")

def guncelle_sonuc(sonuc):
    # Sonucu 1. sayı girişine yaz ve 2. sayıyı temizle
    sayi1.delete(0, tk.END)
    sayi1.insert(0, str(sonuc))
    sayi2.delete(0, tk.END)
    toplami.config(text=f"Sonuç: {sonuc}")

# Arayüz oluşturma
arayuz = tk.Tk()
arayuz.title("Hesap Makinesi")
arayuz.geometry("300x300")

# 1. Sayı
sayi11 = tk.Label(arayuz, text="1. Sayı")
sayi11.place(x=25, y=30)

sayi1 = tk.Entry(arayuz)
sayi1.place(x=25, y=50)

# 2. Sayı
sayi22 = tk.Label(arayuz, text="2. Sayı")
sayi22.place(x=25, y=70)

sayi2 = tk.Entry(arayuz)
sayi2.place(x=25, y=90)

# Sonuç etiketi
toplami = tk.Label(arayuz, text="")
toplami.place(x=25, y=120)

# Butonlar
toplama = tk.Button(arayuz, text="Toplama", command=toplam)
toplama.place(x=200, y=30)

cikarma = tk.Button(arayuz, text="Çıkarma", command=cikar)
cikarma.place(x=200, y=70)

carpma = tk.Button(arayuz, text="Çarpma", command=carp)
carpma.place(x=200, y=110)

bolme = tk.Button(arayuz, text="Bölme", command=bol)
bolme.place(x=200, y=150)

# Sıfırlama butonu
sifirlama = tk.Button(arayuz, text="Sıfırla", command=sifirla)
sifirlama.place(x=200, y=190)

arayuz.mainloop()
