#- importar copy para hacer deepcopy

import copy

#- Definir el stock de un producto en una variable.
stock = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100], [6, 100], [7, 100], [8, 100], [9, 100], [10, 100]]


#- Definir una forma de solicitar el stock disponible del producto por consola.
def mostrar_stock(codigo):
    print(f"El producto {codigo} tiene un stock de {stock[codigo-1][1]} unidades")
   

#- Definir una forma de solicitar unidades del producto por consola. Este número de productos se
#almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados_plantilla = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]
productos_seleccionados = copy.deepcopy[productos_seleccionados_plantilla]

def pedir(codigo, cantidad):# corregir: agregar verificación de stock
    global productos_seleccionados #para usar el scope global de la variable
    productos_seleccionados[(codigo-1)][1] = cantidad #corregir: lista de sólo los itemes seleccionados
     
    

#- Los productos reubicados serán descontados del stock inicial.

for item in productos_seleccionados:
    if ((stock[item[0]-1][1]) - (productos_seleccionados[item[0]-1][1])) < 0: ##- El programa debe verificar que existan unidades disponibles.
        print(f"No hay suficiente stock del producto código N° {item[0]}")
    else:
        stock[item[0]-1][1] = (stock[item[0]-1][1]) - (productos_seleccionados[item[0]-1][1]) #si hay stock, descuenta
       
#borrar carrito       
productos_seleccionados = copy.deepcopy[productos_seleccionados_plantilla]    
    
  




#- Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen
#más de 12 unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las
#unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.



#- No se pueden solicitar más de 20 unidades en un mismo pedido.



#- Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no
#es posible realizar esta acción debido a que no hay stock suficiente.