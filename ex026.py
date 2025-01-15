frase = input("Digite uma frase: ").strip()


print("A sua frase tem {}".format(frase.count("a")))
print("A primeira letra a aparece em {}".format(frase.find("a")+1))
print("A última letra a aparece em {}".format(frase.rfind("a")+1))
