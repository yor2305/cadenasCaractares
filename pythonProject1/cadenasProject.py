
#Strinng Concatenacion
text1 = "Fundamentos con "
texto2 = "Python"
#testo = srt(5)
texto = str(5)
result = texto + texto2
print(result)

nombre = "Yordy"
apellido = "Fajardo"
nombreCompleto = nombre + " " + apellido
print(nombreCompleto)

#formato de String
precio = 97
texto3 = f"el precio es {precio: .2f} pesos"
print(texto3)

#Operaciones Matematicas
texto4 = f"la multiplicacion es {20 * 59}"
print(texto4)

#String capitalize()
texto5 = "python es un lenguaje de alto nivel de programación"
resultado1 = texto5.capitalize()
print(resultado1)

#string casefold()
titulo = "Cien Años de Soledad"
tituloConvertido = titulo.casefold()
print(tituloConvertido)

#String center()
fruta = "Banana"
textoCentrado = fruta.center(20, "_")
print(textoCentrado)


#String count()
titulo1 = "yo amo manzanas , manzanas es mi fruta favorita"
resultado2 = titulo1.count("manzanas")
print(resultado2)

#String endswith
texto6 = "Curso , fundamentos con python."
resultado3 = texto6.endswith(".")
print(resultado3)

#String expandtabs

letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String find
texto7 = "Hola , bienvenidos a Colombia."
resultado4 = texto7.find("bienvenidos")
print(resultado4)

#Funcion titlle
texto8 = "Bienvenidos A Mi Mundo"
resultado5 = texto8.title()
print(resultado5)

#Funcion isalnum

alfanumerico = "Python312"
resultado6 = alfanumerico.isalnum()
print(resultado6)

#Funcion isalpha
letras = "Space X"
resultado7 = letras.isalpha()
print(resultado7)

