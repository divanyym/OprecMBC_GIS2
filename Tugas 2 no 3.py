hari=input("Masukkan nama hari : ")
if (hari == "senin" ):
    print("Seragam kamu hari ini adalah kemeja merah")
elif (hari == "selasa" or "rabu"):
    print("Seragam kamu hari ini adalah kemeja putih")
elif (hari == "kamis" or "sabtu"):
    print("Seragam kamu hari ini adalah kemeja bebas")
elif (hari == "jumat"):
    print("Seragam kamu hari ini adalah kemeja batik")
else:
    print("maaf kamu salah memasukan nama hari (ex:senin,jumat)")
