def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def resta(a, b):
    """Devuelve la resta de a y b."""
    return a - b

def multiplicar(a, b):
    """Devuelve la multiplicación de a y b."""
    return a * b

def dividir(a, b):
    """Devuelve la división de a y b. Muestra un mensaje si se divide por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

