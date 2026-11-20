def calculadora():
    while True:
        operacion = input("Ingrese una operación: ").strip().lower()

        if operacion == "salir":
            print("Calculadora cerrada.")
            break

        operaciones_validas = {
            "suma",
            "resta",
            "multiplicación",
            "multiplicacion",
            "división",
            "division",
        }

        if operacion not in operaciones_validas:
            print("Operación no válida.")
            continue

        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Ingrese números válidos.")
            continue

        if operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "resta":
            resultado = numero1 - numero2
        elif operacion in ("multiplicación", "multiplicacion"):
            resultado = numero1 * numero2
        elif operacion in ("división", "division"):
            if numero2 == 0:
                print("No se puede dividir entre cero.")
                continue
            resultado = numero1 / numero2

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()
