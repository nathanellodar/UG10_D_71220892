pertama = input("Masukan nama pemain pertama: ")
kedua = input("Masukan nama pemain kedua: ")
ketiga = input("Masukan nama pemain ketiga: ")
in1 = int(input("Masukan jumlah kartu pemain pertama: "))
in2 = int(input("Masukan jumlah kartu pemain kedua: "))
in3 = int(input("Masukan jumlah kartu pemain ketiga: "))

if (in1> in2 and in3):
    print(pertama, "menang dengan jumlah kartu sebanyak", in1)
elif (in2> in1 and in3):
    print(kedua, "menang dengan jumlah kartu sebanyak", in2)
elif (in3> in1 and in3):
    print(ketiga, "menang dengan jumlah kartu sebanyak", in3)
elif (in1>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
elif (in2>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
elif (in3>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
