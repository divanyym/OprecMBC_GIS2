print("========== SELAMAT DATANG DI GIS 2 MART ==========")
totalbelanja = int(input('Masukkan Total Belanja Anda : '))
member = input ("Apakah Anda Member ? Silahkan Jawab y atau t: ")
if (member == "y"):
    if (totalbelanja >= 1000000):
        diskon = 8
        print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")

    elif (500000 <= totalbelanja < 1000000):
        diskon = 7
        print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")

    elif (totalbelanja > 0): 
        diskon = 5
        print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")

    else:
        print("Nominal yang anda masukkan salah ex:(1000000, 500000)")

elif (member == "t"):
    if (totalbelanja >= 1000000):
        diskon = 3
        print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")

    elif(500000 <= totalbelanja < 1000000):
        diskon = 2
        print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")

    elif(totalbelanja > 0):
         print("Maaf anda tidak mendapat diskon")

    else:
        print("Nominal yang anda masukkan salah ex:(1000000, 500000)")

else:
    print("anda harus menginputkan y/t ")
