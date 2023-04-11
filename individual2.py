#En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.

#Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.

#Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce

#Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
usuarios = "Hugo Paco Luis Pedro Juan Diego Perico"
print(f"El string de usuarios es el siguiente \n    '{usuarios}' ")

#Ahora piensa en tres de ellos. Buscalos en la lista con el método adecuado.
print("Ahora, ingresaremos lo siguiente:")
print(">>>usuarios.find('Hugo')")
print(">>>usuarios.find('Paco')")
print(">>>usuarios.find('Luis')")
print("y el resultado es el siguiente:")      
print(usuarios.find("Hugo"))
print(usuarios.find("Paco"))
print(usuarios.find("Luis"))

#¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema?
#RESPUESTA: Si escribe el usuario en mayúsculas, no lo encontrará, entonces aplicaría el método title()


busqueda = (input("Busque un usuario: ").title())
resultado = usuarios.find(busqueda)
if resultado == -1:
    print("A ese no lo conoce nadie")
else:
    print(f"{busqueda} se encuentra en el index {resultado}")

#Convierte tu string en una lista, en la cual cada elemento es un usuario.

lista_usuarios = usuarios.split(" ")

#Imprime en pantalla la cantidad usuarios que tiene tu aplicación.
print(f"Ahora el string lo transformamos en lista: {lista_usuarios}")
print(f"La lista de usuarios tiene {(len(lista_usuarios))} elementos")

#Imprimir en pantalla un mensaje de saludo a los diferentes usuarios. 
# ¿Qué técnica puedes utilizar para realizar esto?

usuario_logueado = input("Indique su nombre de usuario:").title()
if usuarios.find(usuario_logueado) == -1:
    print("En este momento estamos comunicándonos con la PDI")
else:
    print(f"¡Bienvenido, {usuario_logueado}!")
 
