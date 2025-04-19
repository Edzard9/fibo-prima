def jumlah_rekursif(n):
    if n == 1:
        return 1
    else:
        return (1 + (n - 1) * 3) + jumlah_rekursif(n - 1)

def tampilkan_proses(n):
    deret = [str(1 + (i * 3)) for i in range(n)]
    proses = " + ".join(deret)
    total = jumlah_rekursif(n)
    print(f"{proses} = {total}")

# Contoh penggunaan
tampilkan_proses(6)
