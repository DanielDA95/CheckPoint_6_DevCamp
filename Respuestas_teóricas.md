# Respuestas a las cuestiones teóricas del **sexto punto de control** 
En este material explicativo, voy a explicar algunos conceptos fundamentales que nos permitiran avanzar mas en el conocimiento de este gran lenguaje de programacion como lo es Python;
A continuacion voy a ir hablando de cada punto. 

## 1.	¿Para qué usamos Clases en Python?
R/. Las clases en Python son fundamentales para la programación orientada a objetos (POO). Permiten definir un conjunto de métodos y atributos que describen un objeto o entidad. Las clases en Python son como planos o plantillas; Un objeto es una entidad que tiene características (atributos) y comportamientos (métodos). Las clases nos ayudan a organizar nuestro código de manera modular y reutilizable, haciendo que nuestros programas sean más eficientes y fáciles de mantener.

 Algunas razones para usar clases son:
- Reutilización de código: Las clases pueden reutilizarse en diferentes partes del programa o en distintos programas, lo que ahorra tiempo y reduce la duplicación de código.
- Encapsulación: Permiten ocultar la complejidad de un objeto y exponer solo una interfaz simple y fácil de usar para interactuar con él.
- Modularidad: Descomponen un programa en componentes más pequeños y manejables, facilitando el mantenimiento y la solución de problemas.
- Polimorfismo: Ayudan a implementar el mismo conjunto de métodos con diferentes comportamientos para distintos tipos de objetos, lo que permite una mayor flexibilidad y extensibilidad en el diseño de programas.
En conclusión y como ejemplo Las clases en Python nos permiten modelar objetos y sus propiedades. Son esenciales para la programación orientada a objetos (POO). Aquí hay un ejemplo de cómo definir una clase Persona con atributos como nombre y edad:

*Ejemplo*
  class Persona:
      def __init__(self, nombre, edad):
          self.nombre = nombre
          self.edad = edad
  
  *Otro ejemplo:* Imaginemos que queremos crear un programa para gestionar una biblioteca. Podemos crear una clase llamada "Libro" que tenga atributos como título, autor, ISBN y género. También podemos definir métodos para agregar libros a la biblioteca, buscarlos por título o autor, y eliminarlos.
  
## 2. Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

- El método especial llamado constructor se ejecuta automáticamente cuando se crea una nueva instancia de una clase. En Python, **este método se llama __init__ y se utiliza para inicializar las propiedades del objeto.** Se ejecuta automáticamente al crear una instancia de una clase.
*Aquí está el ejemplo ampliado:*
  
  class Persona:
      def __init__(self, nombre, edad):
          self.nombre = nombre
          self.edad = edad
  
  **persona1 = Persona(nombre="Ana", edad=30)**
*Para el ejemplo del libro:* La clase "Libro", el método __init__ podría inicializar los atributos del libro con los valores proporcionados al crear la instancia.

## 3.	¿Cuáles son los tres verbos de API? 
R/. Los tres verbos principales en una arquitectura REST (Representational State Transfer) son:

-	GET: Se utiliza para consultar un recurso sin causar efectos secundarios en el servidor. En pocas palabras Consulta un recurso sin modificarlo.
-	POST: Crea recursos nuevos.
-	PUT/PATCH: Modifican un recurso existente (PUT sustituye completamente, PATCH actualiza algunos elementos).

*Ejemplo de solicitud POST con la biblioteca requests*
import requests

data = {"nombre": "Ana", "edad": 30}
response = requests.post("https://api.example.com/personas", json=data)

## 4.	¿Es MongoDB una base de datos SQL o NoSQL? 
R/.	MongoDB es una base de datos NoSQL. A diferencia de las bases de datos relacionales (SQL), MongoDB almacena datos en un formato flexible y fácil de cambiar.  En otras palabras Las bases de datos NoSQL como MongoDB son bases de datos no relacionales que almacenan datos en estructuras flexibles, como documentos JSON. Es ideal para manejar grandes cantidades de datos no estructurados.

## 5.	¿Qué es una API? 
R/. Una API (Interfaz de Programación de Aplicaciones) es un conjunto de definiciones y protocolos que se utiliza para desarrollar e integrar el software de las aplicaciones. Permite la comunicación entre dos aplicaciones de software a través de un conjunto de reglas.
- Una API es una interfaz que permite la comunicación entre aplicaciones.
*Aquí tenemos un ejemplo de cómo consumir una API pública:*
import requests

response = requests.get("https://api.example.com/data")
datos = response.json()

## 6.	¿Qué es Postman?
R/. Postman es una herramienta popular para probar y documentar APIs. Permite enviar solicitudes HTTP a servidores web y ver las respuestas, lo que facilita la depuración y el desarrollo de APIs.

## 7.	¿Qué es el polimorfismo?
R/. El polimorfismo es un concepto de POO que permite que un objeto pueda tomar diferentes formas o comportamientos según el contexto. Permite implementar el mismo método con diferentes comportamientos en distintas clases. El polimorfismo permite que objetos de diferentes clases respondan al mismo método. 
*Aquí tenemos un ejemplo:*
Imagina que tenemos una clase base llamada "Bebé" con un método llamado "hacer_ruido". Podemos crear clases derivadas como "recien_nacido" y "bebe_grande" que hereden de la clase "Bebé" y sobrescriban el método "hacer_ruido" para emitir sonidos específicos de cada bebé.

## 8.	¿Qué es un método dunder?
R/. Los métodos dunder (double underscore) son métodos especiales en Python que comienzan y terminan con dos guiones bajos. Ejemplos comunes son __init__, __str__, y __len__. Estos métodos tienen un significado especial y se utilizan para operaciones específicas en las clases. Se utilizan para sobrecargar los métodos integrados de Python y sus operadores
*Aquí está un ejemplo:*

class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Valor: {self.valor}"

objeto = MiClase(valor=42)
print(objeto)  # Imprime "Valor: 42"

## 9.	¿Qué es un decorador de Python?
R/. Un decorador en Python es una función que modifica o extiende el comportamiento de otra función o método. Se utilizan para agregar funcionalidad adicional sin modificar directamente el código original.

*Ejemplo*
Un decorador común es el decorador @staticmethod. Este decorador indica que un método no está vinculado a una instancia de clase específica y se puede llamar directamente desde la clase.
