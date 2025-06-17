cv = {}                     # Diccionario para los datos personales
academic_training = []      # Lista para la formación académica
professional_experience=[]  #Lista para la informacion de experiencia laboral
personal_references=[]      #Lista para referencias personales
skills_or_certificates=[]   #Lista para añadir certificados y habilidades


def personal_data():
    cedula = int(input("Ingrese número de cédula: "))
    if "personal_data" in cv:
        print("Ya existe una hoja de vida")
        return
    
    nombre = input("Por favor ingrese su nombre: ")
    correo = input("Por favor ingrese su correo electrónico: ")
    telefono = int(input("Teléfono: "))
    direccion = input("Dirección: ")
    fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")

    # Guardamos los datos personales en el diccionario cv
    cv["personal_data"] = {
        "nombre": nombre,
        "cedula": (cedula,),  # Tupla de un solo elemento
        "fecha_nacimiento": (fecha_nacimiento,),  # Tupla de un solo elemento
        "correo": correo,
        "telefono": telefono,
        "direccion": direccion
    }

def academic_training_func():
    while True:
        print("\nPor favor ingrese sus títulos de estudios")
        institute = input("Institución donde estudió: ")
        title = input("Título adquirido: ")
        duration = input("Año de inicio y finalización (ej. 2010-2015): ")
        
        # Añadimos un diccionario con los datos académicos a la lista
        academic_training.append({
            "institute": institute,
            "titulo": title,
            "duracion": duration
        })
        
        if input("¿Desea agregar otro título? (S/N): ").lower() != 's':
            break
    
    # Guardamos la lista academic_training en el diccionario cv
    cv["academic_training"] = academic_training
    
def professional_experience_func():
    while True:
        print("\nVAMOS A INGRESAR EXPERIENCIA LABORAL")
        company=input("Por favor ingresa el nombre de la empresa donde trabajaste: ")
        area= input("Por favor ingresa el cargo que desempeño: ")
        funtion=input("Describa la funciones laborales ejercidas: ")
        time= input("Por favor ingresa el tiempo de duracion (ej: 2010-2015): ")
        
        professional_experience.append({
            "name":company,
            "area":area,
            "funtion":funtion,
            "time":time           
        })
        if input("Deseas agregar mas experiencia labora? (S/N): ").lower() != 's':
            break
        cv[professional_experience]= professional_experience
        
def personal_references_func():    
    while True:
        print("\nVAMOS A GUARDAR LAS REFERENCIAS PERSONALES Y FAMILIARES")
        name=input("Por favor ingresa el nombre de la persona: ")
        relation= input("Por favor ingresa el parentezco: ")
        numberphone=int(input("por favor ingresa el numero de telefono de la persona: "))
        
        personal_references.append({
            "name":name,
            "relation":relation,
            "tel":numberphone,          
        })
        if input("Deseas agregar otra referencia personal o familiar? (S/N): ").lower() != 's':
            break
        cv[personal_references]= personal_references
        
def skills_or_certificates():
    while True:
        print("VAMOS A GUARDAR HABILIDADES Y CERTIFICADOS")
        skills=input("Escriba las 5 habilidades que más lo identifican separadas por coma(,): ")
        certificate=input("Escriba el nombre de los certificados adicionales: ")
        date=input("Ingrese año (ej: 2010-2015): ")
        skills_or_certificates.appened({
            "name": certificate,
            "date": date,
            "skills": skills,
        })
        cv[skills_or_certificates]= skills_or_certificates
        

# Ejecutamos las funciones
personal_data()
academic_training_func()
professional_experience_func()
personal_references_func()

# Mostramos el CV completo
print("\n--- Hoja de Vida ---")
print(cv)

