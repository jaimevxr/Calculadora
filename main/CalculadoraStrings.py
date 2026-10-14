# Decorador
def aviso_decorador(funcion):
    def envoltorio(n1, op, n2):
        print("\n[+] Calculando...")
        return funcion(n1, op, n2)
    return envoltorio

# operaciones
@aviso_decorador
def calcular(n1, operador, n2):
    if operador == '+': return n1 + n2
    if operador == '-': return n1 - n2
    if operador == '*': return n1 * n2
    if operador == '/':
        if n2 == 0: raise ZeroDivisionError("Error: División por cero.")
        return n1 / n2

def mostrar_menu(resultado_actual, historial_str):
    print("\n=== Calculadora Básica ===")
    if resultado_actual is not None:
        print(f"[*] Resultado en memoria: {resultado_actual}")
        print(f"[*] Expresión completa: {historial_str}") 
    else:
        print("[*] Memoria vacía. Se pedirán ambos números.")
    
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    print("6. Limpiar (Empezar de nuevo)")
    print("7. Deshacer (Undo) - Adaptado a strings")
    print("==========================")

def main():
    resultado_actual = None
    historial_str = ""

    while True:
        mostrar_menu(resultado_actual, historial_str)
        opcion = input("Elige una opción (1-7): ")

        if opcion == '5':
            print("¡Hasta la próxima!")
            break

        if opcion == '6':
            if resultado_actual is not None:
                resultado_actual = None
                historial_str = "" 
                print("Memoria limpiada. Empezando de cero.")
            else:
                print("La memoria ya estaba limpia.")
            continue

        if opcion == '7':  # Deshacer
            if historial_str != "" and historial_str.startswith('('):
                texto_sin_bordes = historial_str[1:-1] # Quita el primer y último paréntesis
                
                ult_pos = max(texto_sin_bordes.rfind('+'), texto_sin_bordes.rfind('-'), texto_sin_bordes.rfind('*'), texto_sin_bordes.rfind('/'))
                
                if ult_pos != -1:
                    historial_str = texto_sin_bordes[:ult_pos] # Pega el tijeretazo en ese signo
                    resultado_actual = eval(historial_str) # Recupera el valor que da esa cadena
                    print(f"Operación deshecha. Resultado restaurado a: {resultado_actual}")
                else:
                    resultado_actual = None
                    historial_str = ""
                    print("Se deshizo todo. Memoria limpia.")
            else:
                print("No hay acciones para deshacer.")
            continue

        if opcion in ['1', '2', '3', '4']:
            try:
                if resultado_actual is None:
                    num1 = float(input("Introduce el primer número: "))
                    historial_str = str(num1) 
                else:
                    num1 = resultado_actual
                
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Error: Por favor, introduce un número válido.")
                continue

            op = '+' if opcion == '1' else '-' if opcion == '2' else '*' if opcion == '3' else '/'

            try:
                resultado_actual = calcular(num1, op, num2)
                
                historial_str = f"({historial_str}{op}{num2})"
                
                print(f"Operación: {num1} {op} {num2} = {resultado_actual}")
            except Exception as e:
                print(e)
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 7.")

main()