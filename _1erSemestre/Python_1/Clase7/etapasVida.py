'''Ejercicio 4: Etapas de Vida
Haremos un programa que cuando el usuario ingrese su edad le diga, o imprima
la etapa de su vida en una breve oración:
0 a 9: La infancia es increible y bella
10 a 19: Tienes muchos cambios, mucho que estudiar
20 a 29: Amor y comienza el trabajo
30 a 39: Nuevas etapas, cosas que hacer y concretar :D
40 a 49: Disfrutas cada momento
50 a 59: Disfrutas a tus nietos
60 a 69: La vida es hermosa
70 a 79: Miras al pasado con respeto, y disfrutas cada dia.
80 o para arriba: Eres increible por continuar viviendo, que valor..
'''
edad = int(input('Digite su edad: '))

mensaje = None     #Seteamos a mensaje como 'none'
if 0 < edad < 10:
    mensaje = 'La infancia es increíble y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Nuevas etapas, cosas que hacer y concretar :D'
elif 40 <= edad < 50:
    mensaje = 'Disfrutas cada momento'
elif 50 <= edad < 60:
    mensaje = 'Disfrutas a tus nietos'
elif 60 <= edad < 70:
    mensaje = 'La vida es hermosa'
elif 70 <= edad < 80:
    mensaje = 'Miras al pasado con respeto, y disfrutas cada dia'
elif 80 <= edad < 90:
    mensaje = 'Eres increible por continuar viviendo, que valor..'
else:
    mensaje = 'Error, no hay ningún mensaje para ti :('


print(f'Tu edad es {edad} y mi mensaje para ti es: {mensaje}')