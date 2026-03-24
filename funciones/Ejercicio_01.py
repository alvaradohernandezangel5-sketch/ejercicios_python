def centrar(cad):
    for i in range(40 - (len(cad) // 2)):
        print(" ", end="")
    print(cad)
     #imprimo un subrayado con "="
    for i in range (40 - (len(cad) // 2)):
        print(" ", end="")
    for i in range(len(cad)):
        print("=", end="")
    print("")

message_1 = "Un mensaje centrado"
centrar(message_1)
message_2 = "HOLAAAAA PATSS"
centrar(message_2)