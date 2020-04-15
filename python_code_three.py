numero1 = float(input("Determine o primeiro número:"))
numero2 = float(input("Determine o segundo número:"))
sinal = input("Determine a operação matemática:")

if sinal == "+":
  resultado = numero1 + numero2
elif sinal == "-":
  resultado = numero1 - numero2
elif sinal == "*":
  resultado = numero1 * numero2
elif sinal == "/":
  resultado = numero1 / numero2
else:
  resultado = "Essa não é uma operação matemática válida!" 

print(resultado)