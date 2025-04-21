# Ejercicio: Rango entre las edades 20 y 30 años

edad = int(input("Decime tu edad: "))
"""veinte = edad >= 20 and edad <= 30
print(veinte)
treinta = edad >= 30 and edad <= 40
print(treinta)

if veinte or treinta:
    if veinte:
        print('Estas dentro del rango de los (20\'0)')
        #si usamos comilla simpre, se utiliza la diagonal inversa para que no se confunda
    elif treinta:
        print('Estas dentro del rango de los (30\'0) años')
    else:
        print("No estas dentro del rango")
        #aca no es necesario usar diagonal, por las comillas dobles
"""
if (edad>=20 and edad< 30) or (edad>=30 and edad< 40):
    
    print("Estas dentro del rango de los (20'0) a (30'0) años")
else:
    print("No estas dentro del rango")    

#simplificada
# if (20 <= edad < 30) or (30 <= edad < 40):