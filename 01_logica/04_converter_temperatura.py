def converter_temperatura(valor, de, para):
  # Primeiro converte a temperatura de origem para Celsius
  if de == "C":
      celsius = valor
  elif de == "F":
      celsius = (valor - 32) * 5/9
  else:
      return "Unidade de origem inválida!"

  # Agora converte de Celsius para a unidade desejada
  if para == "C":
      return celsius
  elif para == "F":
      return (celsius * 9/5) + 32
  else:
      return "Unidade de destino inválida!"


print(converter_temperatura(31, 'C', 'F'))