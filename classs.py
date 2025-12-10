#Primer archivo que contiene las clases.

class person:
    def __init__(self, name, age, account, email):                   #La Solicitud de informacion de estudiantes.
        
        self.name = name
        self.age = age
        self.account = account
        self.email = email

class student(person):
    def __init__(self, name, email, phone, books_read=int, current_book=None):               #Informacion de estudiantes
        super().__init__(name, email, phone, books_read)
        self.phone = phone
        self.books_read = books_read
        self.name = name
        self.email = email
        self.current_book = current_book
    
    def book_read(self):
        self.book_read = self.books_read
        print(f"{self.name} ha leido un total de: {self.book_read} libros.")
    
    def __str__(self):
        if self.current_book:
            return f"{self.name} se esta leyendo actualmente {self.current_book}"
        else:
            return f"{self.name} no esta leyendo ningun libro actualmente"

class admin(person):
    def management_students(self, student):
        print(f"Admin {self.name} esta gestionando a {student.name}")

class book:
    def __init__(self, title, author, start_date, end_date):                    #Libros
        self.title = title
        self.author = author
        self.start_date = start_date
        self.end_date = end_date
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
        

class reunion:
    def __init__(self, date, theme, students):                  #Reuniones 
        self.date = date
        self.theme = theme
        self.students = students
    
    def __str__(self):
        return f"reunion con tematica de {self.theme} con fecha en {self.date} y manejado por {self.students}."


