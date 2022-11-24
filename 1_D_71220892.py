print("\(^0^) Selamat datang di kalkulator sederhana(^0^)/")
print("Ketik 1 untuk menghitung penjumlahan")
print("Ketik 2 untuk menghitung pengurangan")
print("Ketik 3 untuk menghitung perkalian")
print("Ketik 4 untuk menghitung pembagian")
print("Ketik 5 untuk menghitung sisa hasil bagi (modulus)")
print("Ketik 6 untuk menghitung pemangkatan")
pilihan = 1
if pilihan <=5:
    pilihan = int(input("masukan pilhan anda:"))
    if pilihan == 1:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus1=(p+d)
        print("hasil dari", p, "di jumlahkan dengan", d, "adalah", rumus1)
        
    elif pilihan == 2:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus2=(p-d)
        print("hasil dari", p, "di pengurangan dengan", d, "adalah", rumus2)
    elif pilihan == 3:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus2=(p*d)
        print("hasil dari", p, "di perkalian dengan", d, "adalah", rumus2)
    elif pilihan == 4:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus2=(p/d)
        print("hasil dari", p, "di pembagian dengan", d, "adalah", rumus2)
    elif pilihan == 5:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus2=(p%d)
        print("hasil dari", p, "di modulo dengan", d, "adalah", rumus2)
    elif pilihan == 6:
        p=int(input("Masukan bilangan pertama:"))
        d=int(input("Masukan bilangan kedua:"))
        rumus2=(p**d)
        print("hasil dari", p, "di pemangkatan dengan", d, "adalah", rumus2)
    
