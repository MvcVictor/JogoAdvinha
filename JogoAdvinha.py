import random ##importação da biblioteca random para gerar números aleatórios

print("Seja bem-vindo, digite um numero de 1 a 100") ##apresentação do jogo
choise_number = int(input("digite o numero: ")) ##input da escolha do usuario, o int e prara transformar a string em um numero inteiro

if str(choise_number).isdigit(): ##verifica se o usuario digitou um numero inteiro, caso não tenha digitado, o programa não segue
    choise_number = int(choise_number) ##transforma a string em um numero inteiro
else:
    print("erro, digite um numero inteiro") ##caso o usuario não tenha digitado um numero inteiro, o programa não continua
    quit() ##sai do programa

random_number = random.randint(0, choise_number) ##gera um numero aleatorio entre 0 e o numero digitado pelo usuario
print(f"o numero aleatorio gerado foi: {random_number}") ##apresenta o numero aleatorio gerado

while True: ##loop infinito, o programa continua até o usuario acertar o numero
    answer_user = input("adivinhe o numero: ") 

    if answer_user.isdigit(): ##verifica se o usuario digitou um numero inteiro, caso não tenha digitado, o programa não continua
        int(answer_user) ##transforma a string em um numero inteiro

    else:
        print("erro, digite um numero inteiro")
        continue

    if answer_user == random_number:
            print("acertou")
            break ##sai do loop infinito, o programa continua
    elif int(answer_user) < random_number: ##verifica se o numero digitado pelo usuario e menor que o numero aleatorio gerado
        ##caso o usuario tenha digitado um numero menor que o numero aleatorio gerado, o programa continua
            print("o numero e maior que o digitado") ##caso o usuario tenha digitado um numero menor que o numero aleatorio gerado, o programa continua
    else:
            print("o numero e menor que o digitado") ##caso o usuario tenha digitado um numero maior que o numero aleatorio gerado, o programa continua
            
print("parabens, voce acertou o numero") ##apresenta a mensagem de parabens ao usuario, caso o usuario tenha acertado o numero
level = 0 ##nivel do usuario, o usuario começa no nivel 0

