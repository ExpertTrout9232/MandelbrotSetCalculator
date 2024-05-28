def compute_mandelbrot_iterations(c, max_iter):
    z = complex(0, 0)
    for i in range(max_iter):
        z = z*z + c
        print(f"Iterace {i+1}: z = {z}")
        if abs(z) > 2:
            return f"Hodnota absolutní hodnoty z přesáhla 2 v iteraci {i+1}."
    return "Absolutní hodnota z nepřesáhla 2, maximální počet iterací dosažen."

# Init
real_part = float(input("Zadejte reálnou část komplexního čísla c: "))
imaginary_part = float(input("Zadejte imaginární část komplexního čísla c: "))
c = complex(real_part, imaginary_part)

max_iter = int(input("Zadejte maximální počet iterací: "))

# Calculation
result = compute_mandelbrot_iterations(c, max_iter)
print(result)