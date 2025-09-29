print("===CALCULADORA DE SUEÑO Y ESTUDIO - 5TO GRADO ===")
print()

# Datos recomendados para 5TO grado (10-11 años)
horas-sueno-recomendadas = 9.5
horas-estudio-recomendadas=2

nombre = input("Cuál es tu nombre?")
print(f"\nHola{nombre}!Eres un estudiante de 5TO grado")

#Calcular sueño
hora_despertar=int(input("A qué hora te despiertas? (formato 24h,ej:7):"))
hora_dormir=hora_despertar-hora_sueno_recomendas

 if hora_dormir < 0:
    hora_dormir+=24
    