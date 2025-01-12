cidade = input('Digite sua cidade: ').strip()


# verifica se a cidade tem Santo no nome
if cidade[:5].lower() == "santo":
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade não começa com Santo')

