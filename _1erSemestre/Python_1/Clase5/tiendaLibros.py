# Ejercicio: Tienda de libros

nombreLibro = input("Digite el nombre del libro: ")
idLibro = int(input("Digite el ID del libro: "))
valor = float(input("Digite el precio del libro: "))
envio = input("¿El envío es gratuito? True/False: ")

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "El valor es incorrecto, debe escribir True/False"

print(f"""
      Nombre: {nombreLibro}
      ID: {idLibro}
      Precio: {valor}
      Envío gratuito? {envio}
""")