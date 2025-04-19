def faktoial(n):
    if n == 0:
        return 1
    else:
        return n * faktoial(n-1)
    
n= int(input("Masukkan angka: "))
print(f"Faktorial dari {n} adalah: {faktoial(n)}")