productNames = ['Arroz', 'Feijão', 'Massa']
prices = [2.5, 3.5, 2,4]
amount = [10,10,15]

def PrintProduct():
    i = 0
    for product in productNames:
        print(i ,productNames[i])
        i += 1
    number = int(input('Escolha um produto para saber seu valor e quantidade: '))
    print('Produto: ',productNames[number], 'Preço: ', prices[number], 'Quantidade: ', amount[number])

def DeleteProduct():
    i = 0
    for product in productNames:
        print(i ,productNames[i])
        i += 1
    number = int(input('Escolha um produto para ser deletado: '))
    
    productNames.pop(number)
    prices.pop(number)
    amount.pop(number)
    print('Produto deletado com sucesso!')
     

PrintProduct()
DeleteProduct()
