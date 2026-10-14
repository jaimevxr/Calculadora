def mostrar_menu(resultado_actual):
    print("\n=== Calculadora Básica ===")
    if resultado_actual is not None:
        print(f"[*] Resultado en memoria: {resultado_actual}")
        print("[*] La próxima operación usará este resultado.")
    else:
        print("[*] Memoria vacía. Se pedirán ambos números.")
    
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. Limpiar (Empezar de nuevo)")
    print("7. Deshacer (Undo)")
    print("8. Rehacer (Redo)")
    print("==========================")

def main():
    resultado_actual = None
    historial_undo = []
    historial_redo = []

    def guardar_estado():
        """Guarda el estado actual en el historial antes de realizar una nueva acción."""
        historial_undo.append(resultado_actual)
        historial_redo.clear()

    while True:
        mostrar_menu(resultado_actual)
        opcion = input("Elige una opción (1-8): ")

        if opcion == '5':
            print("¡Hasta la próxima!")
            break

        if opcion == '6':
            if resultado_actual is not None:
                guardar_estado()
                resultado_actual = None
                print("Memoria limpiada. Empezando de cero.")
            else:
                print("La memoria ya estaba limpia.")
            continue

        if opcion == '7':  # Deshacer
            if historial_undo:
                historial_redo.append(resultado_actual)
                resultado_actual = historial_undo.pop()
                print(f"Operación deshecha. Resultado restaurado a: {resultado_actual}")
            else:
                print("No hay acciones para deshacer.")
            continue
            
        if opcion == '8':  # Rehacer
            if historial_redo:
                historial_undo.append(resultado_actual)
                resultado_actual = historial_redo.pop()
                print(f"Operación rehecha. Resultado restaurado a: {resultado_actual}")
            else:
                print("No hay acciones para rehacer.")
            continue

        # Operaciones matemáticas
        if opcion in ['1', '2', '3', '4']:
            try:
                # Si no hay resultado anterior, pedimos el primero
                if resultado_actual is None:
                    num1 = float(input("Introduce el primer número: "))
                else:
                    num1 = resultado_actual
                
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Error: Por favor, introduce un número válido.")
                continue

            # Guardamos el estado justo antes de operar con éxito
            guardar_estado()

            if opcion == '1':
                resultado_actual = num1+num2
                print(f"Operación: {num1} + {num2} = {resultado_actual}")
            elif opcion == '2':
                resultado_actual = num1-num2
                print(f"Operación: {num1} - {num2} = {resultado_actual}")
            elif opcion == '3':
                resultado_actual = num1*num2
                print(f"Operación: {num1} * {num2} = {resultado_actual}")
            elif opcion == '4':
                resultado = num1/num2
                if isinstance(resultado, str):  # En caso de error por dividir entre cero
                    print(resultado)
                    # Revertimos el guardado en el historial porque falló
                    resultado_actual = historial_undo.pop()
                else:
                    resultado_actual = resultado
                    print(f"Operación: {num1} / {num2} = {resultado_actual}")
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 8.")