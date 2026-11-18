conteo_android = 0
conteo_ios = 0
conteo_nulos = 0
while True:
    print("Ingrese su código:")
    id_votante = int(input())
    if id_votante != 0:
        print("Ingrese su elección (Android / iOS):")
        opcion_elegida = input()
        opcion_elegida = opcion_elegida
        if opcion_elegida == "android":
            conteo_android = conteo_android + 1
        else:
            if opcion_elegida == "ios":
                conteo_ios = conteo_ios + 1
            else:
                print("el voto no se tendrá en cuenta.")
                conteo_nulos = conteo_nulos + 1
    if id_votante == 0:
        break

print("Votos Android:", conteo_android)
print("Votos iOS:", conteo_ios)
print("Votos no válidos (no contados):", conteo_nulos)

if conteo_android > conteo_ios:
    print("La plataforma elegida es: Android")
else:
    if conteo_ios > conteo_android:
        print("La plataforma elegida es: iOS")
    else:
        print("Hay empate: se debe usar otro mecanismo de elección.")
