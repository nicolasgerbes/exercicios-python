#Carrinho de compras

produtos = {
    "banana": 3.50,
    "maçã": 2.20,
    "arroz": 25.00,
    "feijão": 8.90,
    "leite": 4.80,
    "pão": 7.50,
    "café": 15.00,
    "açúcar": 6.40,
    "óleo": 9.70,
    "ovos": 12.00
}


total = 0

while True:
  entrada = input("Digite um item e a quantidade (ou sair): ")
  if entrada.lower() == 'sair':
    break

  try:
    item, quantidade = entrada.split(', ')
    item = item.strip().lower()
    quantidade = float(quantidade.strip())
  

    if item in produtos:
      subtotal = produtos[item] * quantidade
      total += subtotal
      print(f'{quantidade} * {item} = R$ {subtotal:.2f}')
    else:
      print('Produto não encontrado:')
      
  except ValueError:
    print('Formato inválido. Use: produto, quantidade')

print(f'Total da compra: R$ {total:.2f}')