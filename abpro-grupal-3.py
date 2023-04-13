#- importar copy para hacer deepcopy
import copy


#- Definir el stock : se deja item 1 con stock de 10 para facilitar revisión (pedido de producto sin stock suficiente)
stock = {1: 10, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}

#se inicializa diccionario con carrito vacío

productos_seleccionados_plantilla = dict()
productos_seleccionados = copy.deepcopy(productos_seleccionados_plantilla)

#función reinicia stock

def reinicia_stock():
    global stock
    stock = {1: 10, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}
    print("Se ha reiniciado el stock.")

#función de pedir (o agregar al carrito)


def pedir(codigo, cantidad):
    global productos_seleccionados #para usar el scope global de la variables
    global stock
    # si pide más de 20:
    if cantidad > 20: 
        print(f"No se pueden pedir más de 20 unidades. Usted pidió {cantidad}")
    #si pide 12 o más, va uno de yapa
    elif (cantidad +1) <= stock[codigo] and cantidad >= 12: 
        productos_seleccionados[codigo] =  (cantidad + 1) #se agrega con yapa
        print(f"Producto {codigo} : Se agregaron {cantidad} más 1 unidad de yapa al pedido, {cantidad + 1} en total.")
        #se descuenta stock para reservar
        stock[codigo] -= cantidad+1
    #si son menos de 12
    elif cantidad <= stock[codigo]: 
        productos_seleccionados[codigo] = cantidad 
        #se descuenta stock para reservar:
        stock[codigo] -= cantidad
        print(f"Producto {codigo}: Se agregaron {cantidad} unidades al pedido")
    else: #si no hay stock suficiente: 
        print(f"No quedan suficientes unidades del Item {codigo}") 
       

#función borrar carrito:      
def reiniciar_carrito():
    global productos_seleccionados
    productos_seleccionados.clear()
    print("Se ha limpiado el carrito")
 
#función consulta stock 
def consulta_stock():
    global stock
    for key in stock:
        print(f"Producto {key}: {stock[key]} unidades.")
        
#función consulta carrito, si el carrito está vacío devuelve un mensaje avisando
def consulta_carrito():
    global productos_seleccionados
    if bool(productos_seleccionados) == False:
        print("El carrito está vacío")
    else:
        for key in productos_seleccionados:
            print(f"- {productos_seleccionados[key]} unidades del Producto2 N° {key}")        
        
#tecla para pausa y continuar 
def tecla():
    input("\nPara volver presione cualquier tecla: ")

#loop infinito que define menú y su comportamiento:
loop = True
while loop:
    print("Bienvenid@ a Te Lo Vendo \nIngrese el número de la opción solicitada.\n\n1   Agregar productos al carrito\n2   Consultar stock\n3   Ver Carrito\n4   Reiniciar todo\n5   Salir\n")
    opcion = int(input("Ingrese su opción aquí: "))
    
    if opcion == 1: #pedir
        codigo_pedido = int(input("Ingrese código de item a solicitar (1-10): "))
        while codigo_pedido > 10:
            print("Sólo se acepta un número del 1 al 10")
            codigo_pedido = int(input("Ingrese código de item a solicitar (1-10): "))
        print("\n")
        consulta_stock()
        cantidad_pedido = int(input("\n  ¿Cuántas unidades solicitará?\n  Si pide 12 o más unidades, va una de yapa.\n  Máximo se pueden pedir 20.\n\n Ingrese aquí cuántas unidades llevará: "))
        pedir(codigo_pedido, cantidad_pedido)
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
    else: #salir
        exit()
        

        
        
        
        
        
    
    
   
  
