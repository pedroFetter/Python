nota1 = input("Informe a nota 1: ")
nota2 = input("Informe a nota 2: ")
media = ((float(nota1) + float(nota2))/2)

if media >= 6:
  print("Media:", media, "- Aprovado")
else:
  print("Media:", media, "- Reprovado")
