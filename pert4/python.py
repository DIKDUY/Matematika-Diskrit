# Fungsi perkalian
def perkalian(a, b):
    return a * b

# Fungsi pembagian
def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol tidak dapat dilakukan."

# Fungsi penjumlahan
def penjumlahan(a, b):
    return a + b

# Fungsi pengurangan
def pengurangan(a, b):
    return a - b

# Contoh penggunaan fungsi-fungsi tersebut
if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print("Hasil perkalian:", perkalian(num1, num2))
    print("Hasil pembagian:", pembagian(num1, num2))
    print("Hasil penjumlahan:", penjumlahan(num1, num2))
    print("Hasil pengurangan:", pengurangan(num1, num2)) 