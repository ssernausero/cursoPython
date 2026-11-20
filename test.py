#Vamos a hacer una funcion que determine si un numero introducido por el usuario es primo.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return print("El numero no es primo");
    return print("El numero es primo");
    
n = int(input("Ingrese un numero: "));
print(is_prime(n));


