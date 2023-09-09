def cal_imc (peso_kg, altura):
    altura_mt = altura / 100
    imc = peso_kg / (altura_mt ** 2)
    return imc

def interpretacion (imc):
  if imc < 18.5:
    return "Bajo"
  elif 18.5 <= imc <= 24.9: 
    return "Normal"
  elif 25 <= imc <= 29.9:
    return "Sobrepeso"
  else:
    return "Obeso"

calculadora = "Calculadora de índice de Masa Corporal"
calculadora = calculadora.upper()
print (calculadora)

peso_kg = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en cm: "))
imc = cal_imc(peso_kg, estatura)
analisis = interpretacion(imc)

print (f"Tu IMC es de: {imc:.2f}")
print (f"Análisis: {analisis}")

