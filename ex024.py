cidade = input('Digite sua cidade: ').strip()

res = cidade.upper()[:5] == "SANTO"

print(res)