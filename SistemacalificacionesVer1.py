#Ejercicio sistema de calificaciones

Calif = int(input("Proporciona la calificación "))
Aprobado = None
if Calif >= 6 and Calif <= 10: 
    Aprobado = "Aprobado"

elif Calif <= 5 and Calif >= 0:
    Aprobado = "Reprobado"

else:
    Aprobado ="Inserte valor valido"
    
print("La calificación es: ", Calif, "El alumno está:", Aprobado)