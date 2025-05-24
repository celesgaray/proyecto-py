
db_productos = [] # Lista

while True:
    print ("\n-- Menú --")
    print ("1. Agregar producto")
    print ("2. Mostrar productos")
    print ("3. Buscar producto por su nombre")
    print ("4. Eliminar producto")
    print ("5. Salir")

    opciones = input("\nIngrese la opción correspondiente: ").strip()

    match opciones: 
        
        case "1": #AGREGAR PRODUCTO

            while True: 

                # Nombre

                while True:
                    nombre_producto = input("Ingresá nombre del producto: ").strip().lower()
                    if nombre_producto =="" :
                        print("No puede estar vacío el campo del nombre del producto.")
                    else: 
                        break

            # Categorías

                while True: 
                    categoria_producto = input("Ingresá categoría del producto: ").strip().lower()
                    if categoria_producto  =="":
                        print("No puede estar vacío el campo de categoría del producto.")
                    else:
                        break

            # Precio

                while True: 
                    precio_producto = input("Ingresá precio del producto (sólo números enteros): ")

                    if precio_producto.isdigit():
                        precio_producto = int(precio_producto)
                        if precio_producto == 0:
                            print("El precio del producto no puede ser negativo.")
                        else:
                            break
                    else:
                        print("El precio ingresado no es válido.")

                # Agregar a la lista

                db_productos.append([nombre_producto,categoria_producto,precio_producto])     # Sublista:ACÁ TIENE QUE ALMACENARSE DENTRO DE db_productos = []
                print ("Producto agregado.")


                # ¿Agregar otro producto?
                salida_funcion = False
                while True:
                    salida = input("¿Desea agregar otro producto? Ingrese s/n: ").strip().lower()

                    if salida == "n":
                        nombresProd_sub = [producto[0].capitalize() for producto in db_productos]
                        print(f"Carga de productos completa. Productos: {nombresProd_sub}")
                        salida_funcion = True
                        break  
                    elif salida == "s":
                        salida_carga = False
                        break  
                    else:
                        print("Respuesta no válida. Por favor ingrese 's' o 'n'.")            
                if salida_funcion:
                    break

            # FIN DE AGREGAR PRODUCTOS          
                    
        case "2": #MOSTRAR PRODUCTOS
            if not db_productos:
                print(" -- No hay productos cargados para mostrar. --")
            else:
                print("\n--- Lista de productos ---")
                for indice in range(len(db_productos)):
                    print(f" {indice + 1}.\t {str(db_productos[indice][0]).capitalize()} \t {str(db_productos[indice][1]).capitalize()}\t${db_productos[indice][2]}")
                
        case "3": #Buscar producto: por su nombre
                if not db_productos:
                    print("-- No hay productos cargados para mostrar. --")
                else:
                
                    while True:
                        nombresProd_sub = [producto[0].capitalize() for producto in db_productos]
                        print(f"Productos: {nombresProd_sub}")
                        producto_buscado = input("Ingrese nombre del producto: ").strip().lower()
                        producto_encontrado = False
                        for producto in (db_productos):
                            if producto [0].lower() == producto_buscado:
                                producto_encontrado = True
                                print(f"\nProducto {indice}: {producto[0].capitalize()} |\t{producto[1].capitalize()} |\t ${producto[2]}")
                        
                        if not producto_encontrado:
                            print ("\nNo se encontró ningún producto con ese nombre")
                                
                        break
                      
        case "4": #Eliminar producto
            if not db_productos:
                print(" -- No hay productos cargados para mostrar. --")
            else:
                
                while True:
                    nombresProd_sub = [producto[0].capitalize() for producto in db_productos]
                    print(f"Productos: {nombresProd_sub}")
                    producto_eliminar = input(f"Escribe el nombre del producto que quiere eliminar: ").strip().lower()
                    
                    producto_encontrado = False
                    for producto in db_productos:
                        if producto[0].lower() == producto_eliminar:
                            db_productos.remove(producto)
                            print(f"\n'{producto_eliminar}' fue eliminado. Lista actualizada.")
                            producto_encontrado = True
                            break
                    if not producto_encontrado:
                        print ("No se encontro el producto")
                    break

        case "5": #Salir
            print("Saliendo... ")
            break

        case _:
            print("Opción inválida.")
               
    
            

    