#- importar copy para hacer deepcopy
import copy

#- Definir el stock de un producto en una variable.
stock = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}


#- Definir una forma de solicitar el stock disponible del producto por consola.

def consulta_stock(codigo_stock):
    print(f"El producto {codigo_stock} tiene un stock de {stock[codigo_stock]} unidades")
   

#- Definir una forma de solicitar unidades del producto por consola. Este número de productos se
#almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados_plantilla = dict()
productos_seleccionados = copy.deepcopy(productos_seleccionados_plantilla)

def pedir(codigo, cantidad):
    global productos_seleccionados #para usar el scope global de la variable
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
def borrar_carrito():
    productos_seleccionados.clear()
    print("Se ha limpiado el carrito")
    

    
  





