hari=input("Masukkan nama hari : ")
if (hari == "senin" ):
    print("Seragam anda hari ini adalah merah")
elif (hari == "selasa" or "rabu"):
    print("Seragam anda hari ini adalah putih")
elif (hari == "kamis" or "sabtu"):
    print("Seragam kamu hari ini adalah baju bebas")
elif (hari == "jumat"):
    print("Seragam kamu hari ini adlah baju batik")
else:
    print("maaf kamu salah memasukan nama hari (ex:senin,jumat)")
