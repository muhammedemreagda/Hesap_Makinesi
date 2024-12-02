def add(a,b):
    return a + b
def subt(a,b):
    if a >= b :
        return a - b
    else:
        return b - a
def mult(a,b):
    return a * b
def div(a,b):
    if a > b:
        if b == 0:
            return print("Sıfır sayısı payda olamaz!")
        else:
            return float(a / b)
    else:
        if a == 0:
            return print("Sıfır sayısı payda olamaz!")
        else:
            return float(b / a)
def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a-1)
def mod(a,b):
    if a==0 or b==0:
        return print("Sıfır sayısı payda olamaz!")
    else:
        if a > b:
            return a%b
        else:
            return b%a
def degr(a,b):
    if b == 0:
        return 1
    else:
        c = 1
        for i in range(b):
            c *= a
        return c

while 1:
    print("Yapmak istediğiniz işlemi seçin!!!\n\n0-Çıkış\n1-Toplama İşlemi\n2-Çıkarma işlemi\n3-Çarpma İşlemi\n4-Bölme İşlemi\n5-Faktöriyel hesaplama\n6-Mod hesaplama\n7-Üs hesaplama")
    x = int(input("Tercih:"))
    if x < 0 or x > 7:
        print("Lütfen tanımlı bir işlem seçiniz!")
    if x == 0:
        break
    elif x == 1:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Toplam:",add(a,b))
    elif x == 2:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Fark:",subt(a,b))
    elif x == 3:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Çarpım:",mult(a,b))
    elif x == 4:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Bölüm:",div(a,b))
    elif x == 5:
        a = int(input("Değeri giriniz:"))
        print(f"Faktöriyeli:{fact(a)}")
    elif x == 6:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Modu:",mod(a,b))
    elif x == 7:
        a = int(input("İlk değeri giriniz:"))
        b = int(input("İkinci değeri giriniz:"))
        print("Üssü:",degr(a,b))
    
