texto="""
esto es para
usarlo para
varias lineas
"""

print(texto)

s=input("Dime tu nombre")
print(f"Hola  {s}")
try:
    num=int(input("Dime un numero"))
except:
    print ("fallo")