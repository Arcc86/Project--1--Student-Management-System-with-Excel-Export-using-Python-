#Funcionamiento
from classs import student, book, reunion, admin

def load_data():
    # Carga datos desde archivo o inicializa datos vacíos
    return {"Estudiantes": [], "Reuniones": []}

def show_menu():
    print("\n1. Añadir estudiante")
    print("2. Listar estudiantes")
    print("3. Salir")

def main():
    # Cargar datos
    data = load_data()
    students = data.get("Estudiantes", [])  # students lista
    reunions = data.get("Reuniones", [])
    
    print(f'\n =============================\n '
          f'=========================================\n'
          f'Sistema de gestion de estudiantes \n ===========================\n'
          f'=========================================')

    while True:
        show_menu()
        option = input("Elige una opcion: ")

        if option == "1":
            # Añade al estudiante
            name = input("Nombre: ")
            email = input("Correo: ")
            phone = input("Telefono: ")
            account = input("Numero de cuenta: ")
            age = input("Edad: ")
            books_read = input("Cantidad de libros leidos: ")

            # Crear diccionario con los datos
            nuevo_estudiante = {
                "Nombre": name,
                "Email": email,
                "Telefono": phone,
                "Cuenta": account,
                "Edad": age,
                "Libros leidos": books_read
            }

            # Añadir a la lista
            students.append(nuevo_estudiante)
            print(f" Estudiante {name} añadido.")

        elif option == "2":
            # Listado de estudiantes.
            print("\n --- Estudiantes Registrados --- ")
            if not students:  # students está definida aquí
                print("No hay estudiantes registrados aun...")
            else:
                for e in students:
                    print(f"- {e['Nombre']} - {e['Email']} - {e['Telefono']} - {e['Cuenta']} - {e['Edad']} - {e['Libros leidos']}")

        elif option == "3":
            print("Saliendo...")
            break

if __name__ == '__main__':
    main()  