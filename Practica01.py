texto="""
esto es para
usarlo para
varias lineas
"""
#REALIZADO POR DAVID MARAVER CEBALLOS

print(texto)


#PARTE 2
s=input("Dime tu nombre: ")
print(f"Hola  {s}")


#PARTE 3
print(f"Hola {s.upper()}")

print(f"{len(s)}")


#PARTE 4

numeropar=int(input("Dime un numero: "))



for i in range (0,numeropar):
   i += 2
   print(i)





'''
try:
    num=int(input("Dime un numero: "))
except:
    print ("fallo")

print(f"el numero puesto es {num}")
'''

