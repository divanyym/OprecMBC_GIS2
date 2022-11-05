#buat program pola n x n, bintang dan tanda pagar dengan jumlah n(integer) 
n = int(input("Masukan nilai N : "))
a = n+2
print("*  "*a)

for j in range(n):
    print("*"," # "*n,"*")
    
print("*  "*a)
