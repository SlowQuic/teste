print("Digite a largura do terreno:") 
largura = int(input())
print("Digite o comprimento do terreno:")
comprimento = int(input())
print("Digite o valor do metro quadrado:")
metro = int(input())

area = largura * comprimento
custo = area * metro

print()
print("Area do terreno: ", area)
print("Preco do terreno: R$", custo)