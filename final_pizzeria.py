"""Pizzeria Nino"""

pizzas={1: "Muzzarella", 2:"Napolitana", 3:"Cuatro quesos", 4:"Pepperoni", 5:"Margarita", 6:"Champiñones", 7: "Fugazzeta"}

grande={1:3500, 2:4200, 3:4900, 4:4900, 5: 4000, 6: 5600, 7: 4200}
pequeña={1:3000, 2:3700, 3:4400, 4:4400, 5: 3500, 6: 5100, 7: 3700}

total_pedido=0
nombre = ""
apellido = ""
direccion = ""
telefono = ""

def agregar_al_pedido(pizza, tamano, total):
    if pizza in pizzas:
        if tamano == "grande":
            precio = grande.get(pizza, 0)
        elif tamano == "chica":
            precio = pequeña.get(pizza, 0)
        else:
            return total
        if precio > 0:
            total += precio
            print(f"Se agregó {pizzas[pizza]} {tamano} de ${precio} al pedido.")
            print(f"Su total hasta el momento es ${total}")
        else:
            print("Pizza o tamaño no válidos. Por favor, seleccione una opción válida.")
    else:
        print("Pizza no válida. Elija un número de pizza válido.")
    return total

def envio_domicilio(nombre, apellido, direccion, telefono):
  print()
  print("Para finalizar necesitaríamos sus datos para realizar el envío")
  nombre=input("Por favor, coloque su nombre: ")
  apellido=input("Por favor, coloque su apellido: ")
  direccion=input("Por favor, coloque su direccion: ")
  telefono=input("Por favor, coloque su telefono: ")
  print()
  print("Muchas gracias por su atención, enseguida le enviaremos el pedido")
  return envio_domicilio

primer_pedido = True



print("*******Bienvenidos a Pizzería Nino*******")
print("----------------------------------------")

print("a. Realizar un pedido")
print("b. Salir")
print("----------------")
print()

eleccion=input("¿Qué acción desea realizar?: ")

if eleccion != "b" and eleccion != "a":
  print("Esa no es una opción válida.")
  print()
  input("Presione Enter para salir...")
elif eleccion=="b":
  print("Gracias por su visita")
  print()
  input("Presione Enter para salir...")

else:
  print("----------------")
  print("Lista de pizzas: ")
  print("----------------")
  print("{:<8} {:<13} {:<9} {:<9}".format("Menu", "Pizza", "Chica", "Grande"))
  for pizza in pizzas:
    print("{:<5} {:<16} ${:<8} ${:<8}".format(str(pizza), pizzas[pizza], pequeña[pizza], grande[pizza]))


  print()
  print("0. Cerrar pedido")
  print("----------------")

  while True:
    if primer_pedido:
      print()
      menu = input("¿Qué opción del menú desea?: ")
      primer_pedido = False
    else:
      print()
      menu = input("¿Le gustaría algo más?: ")

    if (menu=="0"):
      if total_pedido > 0:
        envio_domicilio(nombre, apellido, direccion, telefono)
        print("Recuerde que su total a pagar es de $"+ str(total_pedido))
        print()
        input("Presione Enter para salir...")
        break
      else:
        print()
        print("No has comprado nada... Espero que nos veamos pronto")
        print()
        input("Presione Enter para salir...")
        break
    elif menu.isdigit():
      pizza_elegida = int(menu)
      while True:
        tamano = input("¿Grande o chica?: ").lower()
        if tamano in ["grande","chica"]:
          total_pedido = agregar_al_pedido(pizza_elegida, tamano, total_pedido)
          break
        else:
          print("Te dije que eligieras entre grande y chica")
    else:
      print("Entrada no válida. Ingrese el número de la pizza que desea.")