def fibo(n):                          #fungsi untuk menghitung bilangan Fibo secara rekursif
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("Masukkan angka: "))
print(f"fibo ke-{n} adalah: {fibo(n)}")
print(f"dengan list fibo ke-{n} adalah: ", end=" ")

for i in range(0, n+1):               #loop untuk menampilkan bilangan Fibo hingga n
    print(fibo(i), end=" ")
