def programa_conjuntos():
    # Definición de los conjuntos base
    K = [7, 18, 3, 10]
    L = [3, 6, 9, 7]
    
    while True:
        print("\na) Juntar K y L.")
        print("b) Diferencia K - L")
        print("c) Diferencia L - K")
        print("d) Combinación K y L")
        print("e) Salir")
        
        opcion = input("Elija opción: ").lower()
        
        if opcion == 'a':
            # Une las listas manteniendo duplicados
            resultado = K + L
            print(f"Juntar K L = {resultado}")
            
        elif opcion == 'b':
            # Elementos en K que no están en L
            resultado = [x for x in K if x not in L]
            print(f"Diferencia K - L = {resultado}")
            
        elif opcion == 'c':
            # Elementos en L que no están en K
            resultado = [x for x in L if x not in K]
            print(f"Diferencia L - K = {resultado}")
            
        elif opcion == 'd':
            # Combinación (unión sin duplicados usando lógica de sets)
            resultado = list(set(K) | set(L))
            print(f"Combinación K y L = {resultado}")
            
        elif opcion == 'e':
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida")
            
        input("\nPresione Enter para continuar...")

# Para que el programa corra al abrir el archivo, quitamos el comentario a la siguiente línea:
if __name__ == "__main__":
    programa_conjuntos()