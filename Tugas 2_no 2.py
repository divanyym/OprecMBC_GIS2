print("========== SELAMAT DATANG DI GIS 2 MART ==========")
totalbelanja = float(input('Masukkan Total Belanja Anda : '))
member = input ("Apakah Anda Member ? Silahkan Jawab y atau t: ")
if (member == "y"):
    if (totalbelanja >= 1000000):
        diskon = 8
    elif (totalbelanja >= 500000 and totalbelanja < 1000000):
        diskon = 7
    else : 
        diskon = 5
    print("Selamat anda mendapatkan diskon sebesar ", diskon, "%")
elif (member == "t"):
    if (totalbelanja >= 1000000):
        diskon = 3
    elif(totalbelanja >= 500000 and totalbelanja < 1000000):
        diskon = 2
    else:
        diskon = 0
    print("Terimakasih telah berbelanja, total diskon Anda adalah ", diskon, "%")
else:
    print("Maaf input yang anda masukkan salah")
    
