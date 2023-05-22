'''
- Resolva os exercícios usando a linguagem de programação Python e o conceito de função (def):
1. Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. A função main chama a função passando os dois argumentos. 
'''

def mostrar_mensagem_e_numero(mensagem, numero):
    print(mensagem, numero)

if __name__ == '__main__':
    mensagem = "Olá, mundo!"
    numero = 4
    mostrar_mensagem_e_numero(mensagem, numero)
# ou

def mostrar_mensagem_e_numero(mensagem, numero):
    print(mensagem, numero)

def main():
    mensagem = "Olá, mundo!"
    numero = 42
    mostrar_mensagem_e_numero(mensagem, numero)

# Chamando a função main
main()

'''2. Implemente uma função que recebe dois valores e retorna a multiplicação deles. 
A função main chama essa função duas vezes. Use inputs.'''

def dois_valores(v1, v2):
    multiplicacao = v1 * v2
    return multiplicacao

if __name__ == '__main__':
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    multiplicacao = dois_valores(v1, v2)
    print('A multiplicação dos dois valores digitados é:', multiplicacao)
