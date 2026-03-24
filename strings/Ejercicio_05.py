
fullname = input('Escribe tu nombre completo')
# print(fullname.title())
words = fullname.split(' ')
iniciales = ''
for word in words:
    iniciales += word[0]

print(iniciales.upper())