''''
money=float(input("¿Cuantos € quieres meter en tu cuenta de ahorros "))
years=3


for i in range (years):
 money=money+((money*4)/100)
 print("En el años",i+1,"tus ahorros son:",round(money,2),"€")
'''

'''Ejercicio Barras de Pan
barra normal : 3.49
barra no fresa 60% descuento
barras=int(input("¿Cuantas barricas de pan de ayer se han vendido? "))
precioNormal=barras*3.49
precioDescuento=(60*3.49)/100
print("El precio normal si fueran barras de hoy seria",round(precioNormal,2),"€")
print("Precio aplicando el 60% descuento es :",round(precioDescuento,2)*barras,"€")

Ejercicio 15 

nombre=input("¿Cual es tu nombre? ")
print("Ahora estas en la matrix",nombre)


Ejercicios 16
num1=int(input("Intrduzca el primero numero, porfavor "))
num2=int(input("Intrduzca el segundo numero, porfavor "))
resultado=num1+num2
print("Resultado de la suma de los nuemros introducidos",resultado)
num3=int(input("Introduce el tecer numero, porfavor "))
resultado2=resultado*num3
print("El resultado de la multiplicación del sumatorio anterior multiplicado por el último número introducido:",resultado2)

Ejercicio 17
texto=input("Introduzca una cadena de caracteres ")
letras=len(texto)
print("Tu cadena de caracteres tiene:",len(texto)," caracteres")
num=int(input("Introduzca un numero entre 0 y el total de caracteres ,por favor "))
letraTexto=texto[num]
print("La letra elegida es:",letraTexto)

Ejercicio 18

num=int(input("Introduzca un numero entero , por favor "))

if num<0: 
  valor= num*-1
  print("El valor absoluto de",num,"es:",valor)
else :
  valor=num
  print("El valor absoluto de",num,"es:",valor)


  Ejericicio 19 

num1=int(input("Introduzca el primer numero "))
num2=int(input("Introduzca el segundo numero "))
if num1<num2 :
  print("El segundo numero(",num2,") es mayor que el primer numero(",num1,").")
else :
  print("El primer numero(",num1,") es mayor que el segundo numero(",num2,").")
  def vocalConsonante(letrita):  
  if letrita in vocalitas:  
   print(letrita," es vocal.")  
  else:  
   print(letrita," es consonante")  
 vocalConsonante(letra)  

  Ejercicio 20

letra=input("Introduzca una letra por favor " )
vocales=["a","e","i","o","u"]
def esVocal(letra):
  if letra in vocales:
    print("La letra introducida(",letra,") es vocal")
  else :
    print("La letra introducida(",letra,") NO es vocal")  
if len(letra)>1 :
  print("NO SE PUEDE PROCESAR EL DATO")
else :
  esVocal(letra)

  

Ejercicio 21
num1=int(input("Introduzca el primer numero "))
num2=int(input("Introduzca el segundo numero "))
num3=int(input("Introduzca el tercer numero "))

if num1<num2 and num1<num3:
  menor = num1
elif num2<num1 and num2<num3:
  menor=num2
elif num3<num1 and num3<num1:
  menor=num3
print("El menor de los tres numeros es:",menor)  
clave = 2
prueba =0
print("EMPIEZA EL JUEGO")
while prueba!=clave:
  print("Adivina un numero entre 0 y 100, listillo")
  prueba=int(input())
print("Has acertado, si que eres un listillo")

Ejercicio 22
def usuarioContrasena(usuario,contraseña):
  usu="Gwenevere"
  pas="excalibur"
  
  if(usuario!=usu and contrasena!= pas):
    print("ACCESO DENEGADO")
  else:
    print("Usuario y contraseña correctos.")
      
      

usuario=input("Introduce un nombre de usuario, porfavor ")
contrasena=input("Introduce una contraseña, porfavor ")
usuarioContrasena(usuario,contrasena)

Ejercicio 23

def minMayus(frase):
  minusculas=0
  mayusculas=0
  for i in frase:
    if i.islower():
      minusculas+=1
    elif i.isupper():
      mayusculas+=1
  print("El numero de mayusculas es:",mayusculas,"y el numero de minusculas es:",minusculas)   
def vocales(frase):
  vocales=["a","e","i","o","u","A","E","I","O","U"]
  vocal=0
  for i in vocales:
    for j in frase:
      if(i==j):
        vocal+=1
  print("El numero de vocales es",vocal)      

frase=input("Introduzca una frase ")
minMayus(frase)
vocales(frase)

Ejercicio 24
def factorialNum(numero):
  if numero>=0:
    factorial=1
    if numero== 0 or numero == 1:
        factorial=1 
    else:
        for i in range(1,numero+1):
            factorial*=i
    print("El factorial de",numero,"!=",factorial)      
  else:
    print("El numero introducido NO es entero positivo. ERROR.")  

numero=int(input("Introduzca un numero postivo entero "))
factorialNum(numero) 

Ejercicio 25'''

frase=input("Introduzca una frase ")
fraseInvertida=frase[::-1]
print("La frase invertida es:",fraseInvertida)





  
  






  





  





