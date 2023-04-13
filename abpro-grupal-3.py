#- importar copy para hacer deepcopy
import copy
import time

#- Definir el stock de un producto en una variable, se deja item código 1 con stock de 10 para facilitar revisión
stock = {1: 10, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}

productos_seleccionados_plantilla = dict()
productos_seleccionados = copy.deepcopy(productos_seleccionados_plantilla)

def reinicia_stock():
    global stock
    stock = {1: 10, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}

productos_seleccionados_plantilla = dict()
productos_seleccionados = copy.deepcopy(productos_seleccionados_plantilla)
    
#- Definir una forma de solicitar el stock disponible del producto por consola.

def consulta_stock(codigo):
    global stock
    print(f"El producto {codigo} tiene un stock de {stock[codigo]} unidades")
   

#- Definir una forma de solicitar unidades del producto por consola. Este número de productos se
#almacenarán en una nueva variable llamada ‘Productos seleccionados’.


def pedir(codigo, cantidad):
    global productos_seleccionados #para usar el scope global de la variable
    global stock
    if cantidad > 20: # si pide más de 20
        print(f"No se pueden pedir más de 20 unidades. Usted pidió {cantidad}")
    elif (cantidad +1) <= stock[codigo] and cantidad >= 12: #si pide 12 o más, va uno de yapa
        productos_seleccionados[codigo] =  (cantidad + 1) #se agrega con yapa
        print(f"Producto {codigo} : Se agregaron {cantidad} más 1 unidad de yapa al pedido, {cantidad + 1} en total.")
        #se descuenta stock para reservar
        stock[codigo] -= cantidad+1
    elif cantidad <= stock[codigo]: #si son menos de 12
        productos_seleccionados[codigo] = cantidad 
        #se descuenta stock para reservar
        stock[codigo] -= cantidad
        print(f"Producto {codigo}: Se agregaron {cantidad} unidades al pedido")
    else: #si no queda stock  
        print(f"No quedan suficientes unidades del Item {codigo}") 
       

#borrar carrito       
def reiniciar_carrito():
    global productos_seleccionados
    productos_seleccionados.clear()
    print("Se ha limpiado el carrito")
 
#consulta stock 
def consulta_stock():
    global stock
    for key in stock:
        print(f"Item {key}: {stock[key]} unidades.")
#consulta carrito
def consulta_carrito():
    global productos_seleccionados
    for key in productos_seleccionados:
        print(f"- {productos_seleccionados[key]} unidades del iten N° {key}")        
        
#tecla para continuar
def tecla():
    input("\nPara volver presione cualquier tecla: ")

infinito = 1    
while infinito > 1:    
    print("Bienvenid@ a Te Lo Vendo \nIngrese el número de la opción solicitada.\n\n1   Realizar Pedido\n2   Consultar stock\n3   Ver Carrito\n4   Reiniciar todo\n5   Salir\n")
    opcion = int(input("Ingrese su opción aquí: "))
    if opcion == 1: #pedir
        codigo_pedido = int(input("Ingrese código de item a solicitar (1-10): "))
        print("\n")
        consulta_stock(codigo_pedido)
        cantidad_pedido = int(input("\n  ¿Cuántas unidades solicitará?\n  Si pide 12 o más unidades, va una de yapa.\n  Máximo se pueden pedir 20.\n\n Ingrese aquí cuántas unidades llevará: "))
        pedir(codigo_pedido, cantidad_pedido)
        print(f"\nSe ha agregado {cantidad_pedido} unidades del item {codigo_pedido} al carrito.")
        tecla()
    elif opcion == 2: #consultar stock
        consulta_stock()
        tecla()
    elif opcion == 3: #ver carrito
        consulta_carrito()
        tecla()
    elif opcion == 4: #Reiniciar todo
        reinicia_stock()
        reiniciar_carrito()
        tecla()
    else:
        exit()
        

        
        
        
        
        
    
    
   
  
