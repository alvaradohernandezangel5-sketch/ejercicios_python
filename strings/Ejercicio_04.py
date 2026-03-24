frase = input('Escribe una frase:')
words = frase.split(" ")
print(words)
print(f"La frase {frase} tiene {len(words)} palabras")

words = []
word = ''
for letra in frase:
    if letra != ' ':
        word += letra
    else:
        words.append(word)
        word = ''
words.append(word)

print(word)