import pickle
import os

def agregar():
    content=str(input("Ingrese su nombre completo:  "))
    list=[]
    list.append(content)
    archivo_bin=open("list","wb")
    pickle.dump(list,archivo_bin)
    archivo_bin.close()


def restaurar():
    archivo_bin=open("list","rb")
    lista=pickle.load(archivo_bin)
    print(lista) 
    archivo_bin.close()

if __name__ == "__main__":
    salir=False
    while not salir:
        print("Programa uso de pickle:Vargas Lopez David Guadalupe \n")
        print("1.- Ingresar datos ")
        print("2.- Recuperar datos almacenados.")
        print("3.- Salir \n")
        try:
            opc=int(input("Elija una opcion:  "))
            if opc==1:
                agregar()
                os.system("pause")
                os.system("cls")
            elif opc==2:
                restaurar()
                os.system("pause")
                os.system("cls")

            elif opc ==3:
                print("Gracias por usar el programa.")
                salir=True
            else:
                print("opcion invalida intente de nuevo")
                os.system("pause")
                os.system("cls")
        except:
            print("opcion invalida, intente de nuevo con un numero entero ente 1 y 3")

  
 

