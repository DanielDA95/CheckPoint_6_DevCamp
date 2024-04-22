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
**Como nos puede servier MongoDB como base de datos NoSQL:** Como es una amplia clase de sistemas de gestión de bases de datos que difieren del modelo clásico de SGBDR (Sistema de Gestión de Bases de Datos Relacionales) en aspectos importantes. La característica más destacada es que no utilizan SQL como lenguaje principal de consultas. Los datos almacenados no requieren estructuras fijas como tablas, y normalmente no soportan operaciones JOIN ni garantizan completamente ACID (atomicidad, consistencia, aislamiento y durabilidad). Además, suelen escalar bien horizontalmente. A veces, estos sistemas se denominan “no solo SQL” para subrayar el hecho de que también pueden soportar lenguajes de consulta de tipo SQL.

Los investigadores académicos suelen referirse a este tipo de bases de datos como almacenamiento estructurado, un término que también abarca las bases de datos relacionales clásicas. Las bases de datos NoSQL se clasifican según su forma de almacenar los datos y comprenden categorías como clave-valor, implementaciones de BigTable, bases de datos documentales y bases de datos orientadas a grafos.

Estos sistemas crecieron junto con las principales redes sociales, como Google, Amazon, Twitter y Facebook. Estas empresas se enfrentaron a desafíos en el tratamiento de datos que las tradicionales SGBDR no podían resolver. Con el crecimiento de la web en tiempo real, surgió la necesidad de proporcionar información procesada a partir de grandes volúmenes de datos con estructuras horizontales más o menos similares. Las compañías se dieron cuenta de que el rendimiento y las propiedades de tiempo real eran más importantes que la coherencia, en la que las bases de datos relacionales tradicionales dedicaban una gran cantidad de tiempo de proceso.

En ese sentido, las bases de datos NoSQL suelen estar altamente optimizadas para las operaciones de recuperación y agregación, y normalmente no ofrecen mucho más que la funcionalidad de almacenar registros (por ejemplo, almacenamiento clave-valor). Aunque pierden flexibilidad en tiempo de ejecución en comparación con los sistemas SQL clásicos, compensan esta pérdida con ganancias significativas en escalabilidad y rendimiento cuando se trata de ciertos modelos de datos.


## ¿Qué es una API?
Una API (siglas en inglés de application programming interface, que en español significa interfaz de programación de aplicaciones) es como un puente entre diferentes aplicaciones. Imagina que las aplicaciones son personas que hablan idiomas distintos. La API les permite comunicarse y compartir información.

*Por ejemplo,* supongamos que tienes una aplicación de recetas en tu teléfono. Si buscas una receta específica, la API puede hablar con un sitio web de recetas y pedirle las recetas que coinciden con tus criterios. La API recibe la solicitud, busca las recetas adecuadas y luego envía los resultados de vuelta a tu aplicación. Así, las aplicaciones pueden trabajar juntas de manera más eficiente y efectiva gracias a las APIs.

**Características de las APIs:**
**Comunicación**: Las APIs permiten que diferentes partes de un programa se hablen entre sí. Son como el teléfono o el correo electrónico que usamos para comunicarnos.
**Abstracción**: Las APIs nos ayudan a simplificar tareas complicadas. Por ejemplo, en lugar de escribir todo el código para dibujar ventanas o iconos en la pantalla, podemos usar una API que ya tiene esas funciones.
**Generalidad**: Las APIs proporcionan un conjunto de funciones útiles que muchos programadores pueden aprovechar. Esto nos ahorra tiempo y esfuerzo al no tener que programar todo desde cero. Además, las APIs son abstractas, lo que significa que no necesitamos saber cómo funcionan por dentro; solo necesitamos saber cómo usarlas.


## 6.	¿Qué es Postman?
R/. Postman, en el ámbito del desarrollo de software, es una herramienta fundamental que permite a los desarrolladores probar, depurar y documentar APIs. Su utilidad se destaca especialmente para aquellos que trabajan en aplicaciones basadas en APIs y necesitan evaluar el comportamiento de estas interfaces.
En los últimos años, Postman ha ganado gran popularidad como una de las herramientas más destacadas en el campo del desarrollo de software. Su éxito se atribuye en gran medida a su capacidad para simplificar el proceso de prueba de APIs. La herramienta ofrece una interfaz intuitiva que facilita la evaluación de APIs, la documentación de sus características y la realización de pruebas de carga.
Postman es más que una simple herramienta que te permite explorar, probar y afinar tus APIs con facilidad y eficiencia. Con Postman, puedes enviar solicitudes a los puntos finales de API, recibir respuestas y, lo más importante, comprobar si todo funciona como debería. Ya sea que estés construyendo una aplicación móvil, una plataforma web o cualquier otro proyecto tecnológico, Postman te brinda la capacidad de simular peticiones y obtener respuestas instantáneas.

Con Postman, puedes organizar tus solicitudes en colecciones, lo que te permite tener un flujo de trabajo más ordenado y eficiente. Además, puedes utilizar variables para personalizar las solicitudes y automatizar tareas repetitivas. Esto significa que puedes ahorrar tiempo y esfuerzo al realizar pruebas en diferentes escenarios sin tener que escribir cada solicitud desde cero. Postman también ofrece una interfaz intuitiva y amigable que te permite visualizar las respuestas de las API de forma clara y comprensible. Puedes examinar los detalles de cada respuesta, desde el código de estado hasta los datos devueltos. Además, puedes realizar pruebas de autenticación, enviar encabezados personalizados y probar diferentes métodos de solicitud, todo desde una única plataforma

**Ventajas y uso de Postman.**
- Simplifica el proceso de pruebas
Postman simplifica el proceso de pruebas de API. Los desarrolladores pueden realizar pruebas de API sin tener que escribir líneas de código. Esto significa que el proceso de prueba de API es mucho más rápido y sencillo.
Postman también proporciona a los desarrolladores la capacidad de depurar y documentar API. Esto significa que los desarrolladores pueden ver el código de una API, depurarlo y documentarlo de forma sencilla. Esto ayuda a los desarrolladores a entender mejor el comportamiento de las API y a identificar posibles errores.

En resumen, Postman es una herramienta esencial para los desarrolladores que desean asegurar la calidad y el correcto funcionamiento de sus APIs, contribuyendo así al éxito de sus aplicaciones.

## 7.	¿Qué es el polimorfismo?
R/. El polimorfismo es un concepto de la **Programación orientada a objetos** que permite que un objeto pueda tomar diferentes formas o comportamientos según el contexto. Permite implementar el mismo método con diferentes comportamientos en distintas clases. El polimorfismo permite que objetos de diferentes clases respondan al mismo método.
El polimorfismo permite crear una jerarquía de clases relacionadas que se comportan de manera diferente pero que comparten una interfaz común. Esto hace que el código sea más fácil de mantener y actualizar, ya que se puede agregar una nueva clase sin afectar el código existente.
**Ventajas del polimorfismo.**
- Código más limpio y organizado: Al utilizar polimorfismo, se puede escribir código genérico que funcione con diferentes tipos de objetos. Esto facilita la adición de nuevas funcionalidades sin tener que modificar el código existente.
- Reutilización de código: El polimorfismo permite que los objetos tomen diferentes formas y respondan a un mismo mensaje de diferentes maneras. Esto promueve la reutilización de métodos y comportamientos en diferentes clases.
- Flexibilidad en el diseño del software: Al aplicar polimorfismo, se pueden crear relaciones IS-A entre objetos y sus superclases. Esto proporciona flexibilidad en el diseño y permite adaptar el software a cambios futuros sin afectar su funcionamiento.
- Mayor abstracción: El polimorfismo permite abstraer conceptos comunes en superclases, lo que facilita la comprensión y el mantenimiento del código. Los objetos pueden actuar de manera polimórfica sin preocuparse por los detalles específicos de su implementación.
- Mejor legibilidad y comprensión del código: Al utilizar polimorfismo, se evita la duplicación de código y se simplifica la estructura del programa. Esto mejora la legibilidad y facilita la colaboración entre desarrolladores.
*Aquí tenemos un ejemplo:*
Imagina que tenemos una clase base llamada "Bebé" con un método llamado "hacer_ruido". Podemos crear clases derivadas como "recien_nacido" y "bebe_grande" que hereden de la clase "Bebé" y sobrescriban el método "hacer_ruido" para emitir sonidos específicos de cada bebé.

## 8.	¿Qué es un método dunder?
R/. Los métodos dunder (double underscore) son métodos especiales en Python que comienzan y terminan con dos guiones bajos. Ejemplos comunes son __init__, __str__, y __len__. Estos métodos tienen un significado especial y se utilizan para operaciones específicas en las clases. Se utilizan para sobrecargar los métodos integrados de Python y sus operadores
La sobrecarga de operadores significa cambiar la forma en que los operadores se comportan en diferentes situaciones. Es un tipo de polimorfismo. Con la sobrecarga de operadores, podemos agregar significado o funcionalidad adicional a un operador para realizar más de una operación. Por ejemplo, el operador + realiza sumas con operandos enteros. Pero cuando se usa con operandos de cadena, realiza la concatenación porque el operador + está sobrecargado.

*Aquí está un ejemplo:*

class MiClase:
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f"Valor: {self.valor}"
objeto = MiClase(valor=42)
print(objeto)  # Imprime "Valor: 42"

**Varios tipos de métodos que podemos usar:**
- __init__(): Aunque a menudo se le llama constructor, no es un verdadero constructor. El método __new__() es el constructor real. __new__() crea una instancia de la clase y luego se pasa a __init__() junto con otros argumentos. Este método se utiliza para inicializar objetos cuando se crean1.
- __repr__() y __str__():
- __repr__(): Define la representación de cadena “oficial” de un elemento. Idealmente, debería generar una cadena que sea una declaración de Python válida y se pueda usar para recrear el objeto. Se utiliza principalmente para la depuración.
- __str__(): Devuelve una representación de cadena del objeto que no necesita ser una declaración de Python válida. Se utiliza en funciones incorporadas como format() y print(), para que el usuario final pueda leer la representación de la cadena1.
- __len__(): Se utiliza para implementar el método integrado len(). Debería devolver la longitud del objeto. Por ejemplo, para un vector, tiene sentido que len() devuelva la intensidad del vector1.

## 9.	¿Qué es un decorador de Python?
R/. Un decorador en Python es una función que modifica o extiende el comportamiento de otra función o método. Se utilizan para agregar funcionalidad adicional sin modificar directamente el código original. Para profundizar mejor en la explicacion podemos pensar en que un decorador es un *interruptor* que podemos encender o apagar para añadir funcionalidad extra a una función sin necesidad de añadir más código al cuerpo de dicha función. En la práctica un decorador se indica con el signo @ y se pone encima de la función que decora. 

*Ejemplos*
- @staticmethod: Este decorador se aplica a un método dentro de una clase y lo convierte en un método estático. Los métodos estáticos no requieren una instancia de la clase para ser llamados y son útiles para funciones que no dependen de los atributos de la instancia.
- @classmethod: Similar al decorador @staticmethod, pero se aplica a un método de clase. Los métodos de clase reciben la clase como su primer argumento y son útiles para operaciones que afectan a toda la clase.
- @property: Convierte un método en una propiedad. Permite acceder a un atributo como si fuera una propiedad, sin necesidad de llamar a un método explícito.
- @abstractmethod: Define un método abstracto en una clase base. Las clases derivadas deben implementar este método. Es útil para definir una interfaz común en clases derivadas.
- @wraps: Se utiliza para preservar los metadatos (como el nombre y la documentación) de una función decorada. Ayuda a mantener la información original de la función.
- @lru_cache: Crea una caché de resultados para una función. Almacena en memoria los resultados anteriores para evitar recálculos costosos.
- @timing: Un decorador personalizado para medir el tiempo de ejecución de una función. Puede ser útil para optimizar el rendimiento.
- @retry: Intenta ejecutar una función varias veces si falla debido a excepciones específicas. Útil para manejar conexiones de red o llamadas a API.
- @log: Registra información sobre las llamadas a una función. Puede ser útil para depurar o rastrear el flujo de ejecución.
- @deprecated: Marca una función como obsoleta y muestra una advertencia cuando se llama. Útil para indicar que una función será eliminada en futuras versiones.

*Ventajas de usar los decoradores*
-Modularidad y Reutilización: Los decoradores permiten separar la funcionalidad adicional de una función o método en una función independiente. Esto facilita la reutilización de la misma lógica en diferentes partes del código.
-Sintaxis Concisa: Los decoradores ayudan a mantener el código limpio y conciso. En lugar de repetir la misma lógica en varios lugares, puedes aplicar un decorador a varias funciones con una sola línea de código.
-Aspectos y Funcionalidades Adicionales: Los decoradores pueden agregar características adicionales a las funciones sin modificar su implementación original. Por ejemplo, puedes usar un decorador para medir el tiempo de ejecución de una función o para manejar excepciones de manera centralizada.
-Separación de Responsabilidades: Los decoradores permiten separar las preocupaciones específicas de una función. Por ejemplo, puedes tener un decorador para autenticar una función y otro para registrar sus llamadas, sin mezclar estas responsabilidades en la función principal.
-Extensibilidad: Los decoradores son flexibles y se pueden aplicar a cualquier función o método. Esto facilita la extensión del comportamiento de las funciones existentes sin modificar su código fuente.
