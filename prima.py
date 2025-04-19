def prima(n):                   #fungsi untuk memeriksa apakah n adalah bilangan prima
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_prima_hingga(n):        #fungsi untuk menghasilkan daftar bilangan prima hingga n
    primes = []
    for i in range(2, n + 1):
        if prima(i):
            primes.append(i)
    return primes

n = int(input("Masukkan angka: "))
if prima(n):                     #memeriksa apakah n adalah bilangan prima
    print(f"{n} adalah bilangan prima")
    print(f"Daftar bilangan prima hingga {n}: {list_prima_hingga(n)}")
else:
    print(f"{n} bukan bilangan prima")


