

## STRINGS


# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela
print('Olá mundo!!!')

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
string = float(input('Digite um número: '))
print('O número digitado foi {}'.format(string))

# 3. Faça um Programa que peça dois números e imprima a soma.
number1 = float(input('Digite um número: '))
number2 = float(input('Digite mais um número: '))
sum = number1 + number2
print('Você digitou {0} e {1}. A soma deles é {2}'.format(number1, number2, sum))

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
value1 = float(input('Digite a nota do 1º bimestre: '))
value2 = float(input('Digite a nota do 2º bimestre: '))
value3 = float(input('Digite a nota do 3º bimestre: '))
value4 = float(input('Digite a nota do 4º bimestre: '))
mean = (value1 + value2 + value3 + value4) / 4
print('As suas notas foram {0}, {1}, {2} e {3} e a sua média é {4}'.format(value1, value2, value3, value4, mean))

# 5. Faça um Programa que converta metros para centímetros.
while True:
    try:
        value = float(input('Qual o valor da medida a ser convertida? '))
    except:
        print("Você não digitou um número!")
        continue
    else:
        break
while True:
    try:
        print('1-) Normal')
        print('2-) Quadrado')
        print('3-) Cubo')
        greatness = ()
        greatness = int(input('Qual a grandeza desta medida?[1/2/3] '))
    except :
        print("Você não digitou um número!")
        continue
    else:
        break
while True:
    try:
        print('1-) Milimetro(s)')
        print('2-) Centimetro(s)')
        print('3-) Decimetro(s)')
        print('4-) Metro(s)')
        source = int(input('Qual a unidade da sua medida?[1/2/3/4] '))
    except:
        print("Você não digitou um número!")
        continue
    else:
        break
while True:
    try:
        destiny = int(input('Para qual unidade você quer converter?[1/2/3/4] '))
    except:
        print("Você não digitou um número!")
        continue
    else:
        break

if greatness == 1:
    if source == 1:
        if destiny == 2:
           print('O valor convertido para centimetros é {0}'.format(value / 10))
        elif destiny == 3:
            print('O valor convertido para decimetros é {0}'.format(value / 100))
        elif destiny == 4:
            print('O valor convertido para metros é {0}'.format(value / 1000))
    elif source == 2:
        if destiny == 1:
           print('O valor convertido para milimetros é {0}'.format(value * 10))
        elif destiny == 3:
            print('O valor convertido para decimetros é {0}'.format(value / 10))
        elif destiny == 4:
            print('O valor convertido para metros é {0}'.format(value / 100))
    elif source == 3:
        if destiny == 1:
           print('O valor convertido para milimetros é {0}'.format(value * 100))
        elif destiny == 2:
            print('O valor convertido para centimetros é {0}'.format(value * 10))
        elif destiny == 4:
            print('O valor convertido para metros é {0}'.format(value / 10))
    elif source == 4:
        if destiny == 1:
           print('O valor convertido para milimetros é {0}'.format(value * 1000))
        elif destiny == 2:
            print('O valor convertido para centimetros é {0}'.format(value * 100))
        elif destiny == 3:
            print('O valor convertido para decimetros é {0}'.format(value * 10))
elif greatness == 2:
    if source == 1:
        if destiny == 2:
           print('O valor convertido para centimetros quadrados é {0}'.format((value / 10)**2))
        elif destiny == 3:
            print('O valor convertido para decimetros quadrados é {0}'.format((value / 100)**2))
        elif destiny == 4:
            print('O valor convertido para metros quadrados é {0}'.format((value / 1000)**2))
    elif source == 2:
        if destiny == 1:
           print('O valor convertido para milimetros quadrados é {0}'.format((value * 10)**2))
        elif destiny == 3:
            print('O valor convertido para decimetros quadrados é {0}'.format((value / 10)**2))
        elif destiny == 4:
            print('O valor convertido para metros quadrados é {0}'.format((value / 100)**2))
    elif source == 3:
        if destiny == 1:
           print('O valor convertido para milimetros quadrados é {0}'.format((value * 100)**2))
        elif destiny == 2:
            print('O valor convertido para centimetros quadrados é {0}'.format((value * 10)**2))
        elif destiny == 4:
            print('O valor convertido para metros quadrados é {0}'.format((value / 10)**2))
    elif source == 4:
        if destiny == 1:
           print('O valor convertido para milimetros quadrados é {0}'.format((value * 1000)**2))
        elif destiny == 2:
            print('O valor convertido para centimetros quadrados é {0}'.format((value * 100)**2))
        elif destiny == 3:
            print('O valor convertido para decimetros quadrados é {0}'.format((value * 10)**2))
elif greatness == 3:
    if source == 1:
        if destiny == 2:
           print('O valor convertido para centimetros cúbicos é {0}'.format((value / 10)**3))
        elif destiny == 3:
            print('O valor convertido para decimetros cúbicos é {0}'.format((value / 100)**3))
        elif destiny == 4:
            print('O valor convertido para metros cúbicos é {0}'.format((value / 1000)**3))
    elif source == 2:
        if destiny == 1:
           print('O valor convertido para milimetros cúbicos é {0}'.format((value * 10)**3))
        elif destiny == 3:
            print('O valor convertido para decimetros cúbicos é {0}'.format((value / 10)**3))
        elif destiny == 4:
            print('O valor convertido para metros cúbicos é {0}'.format((value / 100)**3))
    elif source == 3:
        if destiny == 1:
           print('O valor convertido para milimetros cúbicos é {0}'.format((value * 100)**3))
        elif destiny == 2:
            print('O valor convertido para centimetros cúbicos é {0}'.format((value * 10)**3))
        elif destiny == 4:
            print('O valor convertido para metros cúbicos é {0}'.format((value / 10)**3))
    elif source == 4:
        if destiny == 1:
           print('O valor convertido para milimetros cúbicos é {0}'.format((value * 1000)**3))
        elif destiny == 2:
            print('O valor convertido para centimetros cúbicos é {0}'.format((value * 100)**3))
        elif destiny == 3:
            print('O valor convertido para decimetros cúbicos é {0}'.format((value * 10)**3))

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

radius = float(input('Digite o valor do raio em metros: '))
R = lambda radius: (radius**2) * 3.1416
print('A área desta circunferência {0} metros quadrados'.format(round(R(radius),2)))

# 7. Faça um Programa que calcule as medidas de um quadrado através da área.

from math import sqrt

measure = float(input('Digite a área do quadrado em metros: '))
print('Cada lado do quadrado mede {0}'.format(sqrt(measure)))

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

print('Vamos calcular o seu salário...')
money = float(input('Quanto você recebe por hora?R$ '))
hours = int(input('Quantas horas você trabalha por dia? '))
days = int(input('Você trabalha quantos dias por semana?[de 1 a 7] '))
weeks = int(input('Quantas semanas você trabalha?[de 1 a 4] '))
salary = money * hours * days * weeks
print('O seu salário será R${0}'.format(salary))

# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

celsius = [30,40,50,60,70,80]
farenheit = [(5 * (F-32) / 9) for F in celsius]
for i in farenheit:
    print(round(i,2))



# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

C = float(input('Digite a temperatura em celsius para converter para farenheit: '))

def Farenheit(C):
    F = C * 1.8 + 32
    print(round(F,2))
Farenheit(C)

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

while True:
    try:
        number1 = int(input('Digite um número inteiro: '))
    except:
        print('Você ainda não digitou um número.')
        continue
    else:
        break
while True:
    try:
        number2 = int(input('Digite outro número inteiro: '))
    except:
        print('Você ainda não digitou um número.')
        continue
    else:
        break
while True:
    try:
        number3 = float(input('Digite um número decimal: '))
    except:
        print('Você ainda não digitou um número.')
        continue
    else:
        break

def Multiplication (number1, number2):
    M = (number1*2) * (number2/2)
    print(round(M,2))
Multiplication(number1, number2)

def Sum (number1, number3):
    S = (number1*3) + number3
    print(round(S,2))
Sum(number1, number3)

def Cube (number3):
    C = number3**3
    print(round(C,2))
Cube(number3)

# 12. e 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

while True:
    try:
        gender = str(input('Qual é o seu sexo?[F/M] '))
    except:
        print('Você ainda não digitou seu sexo.')
        continue
    else:
        break
while True:
    try:
        height = float(input('Qual é a sua altura? '))
    except:
        print('Você ainda não digitou sua altura.')
        continue
    else:
        break
if gender == 'F':
    weight = (62.1*height) - 44.7
    print('Seu peso ideal é {0}'.format(round(weight,2)))
elif gender == 'M':
    weight = (72.7*height) - 58
    print('Seu peso ideal é {0}'.format(round(weight,2)))

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
while True:
    try:
        pounds = float(input('Quantos quilos de peixes você pegou hoje? '))
    except:
        print('Você ainda não digitou o peso')
        continue
    else:
        print('Obrigado por digitar o peso.')
        break
if pounds <= 50:
    print('Você não precisa pagar multa. Boa Viagem!!!')
elif pounds > 50:
    excess = (pounds - 50)
    forfeit = excess * 4
    print('O exesso pescado foi de {0} kg e portanto sua multa é de R$ {1}'.format(excess, forfeit))

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido

while True:
    try:
        workingHours = int(input('Digite quantas horas você trabalha por dia: '))
    except:
        print('Você ainda não digitou quantas horas você trabalha por dia.')
        continue
    else:
        break
while True:
    try:
        money = float(input('Digite quanto você ganha por hora:R$ '))
    except:
        print('Você ainda não digitou o quanto você ganha por hora.')
        continue
    else:
        print('Obrigado por informar')
        break
grossSalary = workingHours * money * 20
ir = grossSalary * 0.11
inss = grossSalary * 0.08
syndicate = grossSalary * 0.05
dicounts = ir + inss + syndicate
netSalary = grossSalary - dicounts
print('O seu salário bruto é de R${0}, o valor total de descontos foi R${1}, sendo R${2} de imposto de renda, R${3} '
      'de INSS e R${4} de sindicato. Portanto, seu salário líquido e de R${5}'.format(grossSalary, dicounts, ir, inss, syndicate, netSalary))

# 16 e 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
# isto é, considere latas cheias.

meters = float(input('Quantos metros quadrados você precisa pintar? '))
liters = (meters*0.1) / 6
if ((liters % 18) >= 0) and (round((liters % 10.8),2) <= 7.19):
    result = liters/18


## LISTAS


# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vector = []
cont = 1
while cont < 6:
    while True:
        try:
            number = int(input('Digite o {0}º número inteiro de 5: '.format(cont)))
        except:
            print('Você ainda não digitou o {0}º número inteiro de 5.'.format(cont))
            continue
        else:
            vector.append(number)
            cont += 1
            break
print(vector)


# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vector = []
cont = 1
while cont < 11:
    while True:
        try:
            number = int(input('Digite o {0}º número inteiro de 10: '.format(cont)))
        except:
            print('Você ainda não digitou o {0}º número inteiro de 10.'.format(cont))
            continue
        else:
            vector.append(number)
            cont += 1
            break
print(list(reversed(vector)))

# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
dic = {}
dicFinal = {}
cont = 1
while True:
    try:
        name = str(input('Qual é o seu nome?'))
    except:
        print('Você ainda não digitou o seu nome.')
    if name == '' or name == '0' or name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or\
            name == '6' or name == '7' or name == '8' or name == '9':
        print('Digite um nome válido.')
        continue
    else:
        break
while cont < 5:
    while True:
        try:
            note = int(input('Qual foi sua nota no {0}º trimestre? '.format(cont)))
        except:
            print('Você ainda não digitou a nota do {0}º trimesre.'.format(cont))
            continue
        else:
            dic[cont] = note
            dicFinal[name] = dic
            cont += 1
            break
print('{0}, as suas notas foram {1} e a sua média é {2}.'.format(name, dic, sum(dic.values()) / 4))
cont = 1
while True:
    try:
        choice = str(input('Gostaria de colocar as notas de mais alguém?[S/N] '))
        choice = choice.upper()
    except:
        print('Você ainda não informou se quer colocar as notas de mais alguém.')
        continue
    if choice != 'S' and choice != 'N':
        print('Escolha inválida.Tente novamente...')
        continue
    elif choice == 'N':
        break
    elif choice == 'S':
        while True:
            try:
                name = str(input('Qual é o nome?'))
            except:
                print('Você ainda não digitou o nome.')
            if name == '' or name == '0' or name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or name == '6' or name == '7' or name == '8' or name == '9':
                print('Digite um nome válido')
                continue
            else:
                break
        while cont < 5:
            while True:
                try:
                    note = int(input('Qual foi sua nota no {0}º trimestre? '.format(cont)))
                except:
                    print('Você ainda não digitou a nota do {0}º trimesre.'.format(cont))
                    continue
                else:
                    dic[cont] = note
                    dicFinal[name] = dic
                    cont += 1
                    break
        print('As notas do(a) {0} foram {1} e a média dele(a) é {2}.'.format(name, dic, sum(dic.values()) / 4))
        print(dicFinal)
        cont = 1

# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

cont = 1
contCons = 0
contVogal = 0
while cont < 11:
    while True:
        try:
            letter = str(input('Digite a {0}ª letra de 10: '.format(cont)))
            letter = letter.lower()
        except:
            print('Você ainda não digitou a {0}ª letra.'.format(cont))
            continue
        if letter == '' or letter == '0' or letter == '1' or letter == '2' or letter == '3' or letter == '4'\
                or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9':
            print('Inválido. Digite apenas letras.')
        elif letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
            cont += 1
            contCons += 1
        else:
            cont += 1
            contVogal += 1
print('De 10 letras, você digitou {0} vogais e {1} consoantes.'.format(contVogal, contCons))

## ESTRUTURA DE DECISÃO

# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
while True:
    try:
        number = int(input('Digite um número de zero a 10: '))
    except:
        print('Você ainda não digitou un número.')
        continue
    if 0 <= number <= 10:
        print('Obrigado por digitar!')
        break
    else:
        print('Número inválido.')
        continue

# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    while True:
        name = str(input('Qual o seu nome? '))
        name1 = name.capitalize()
        if name1 == '':
            print('Você ainda não informou seu nome.')
            continue
        else:
            break

    while True:
        password = str(input('Digite uma senha: '))
        password1 = password.capitalize()
        if password1 == '':
            print('Você ainda não digitou uma senha.')
            continue
        else:
            break
    if name1 == password1:
        print('A senha tem que ser diferente do seu nome.')
        continue
    else:
        break

# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    name = str(input('Qual é o seu nome? '))
    if name == '':
        print('Você ainda não digitou o seu nome.')
        continue
    elif len(name) > 3:
        name1 = name.capitalize()
        break
while True:
    old = int(input('Quantos anos você tem? '))
    if old == '':
        print('Você ainda não informou sua idade.')
        continue
    if 0 <= old <= 150:
        break
    elif old > 150 or old < 0:
        print('Idade Inválida')
        continue
while True:
    salary = float(input('Qual é o seu salário? '))
    if salary > 0:
        break
    elif salary == '':
        print('Você ainda não informou seu salário.')
        continue
    elif salary < 1:
        print('Salário Inválido!')
        continue
while True:
    genre = str(input('Qual o seu gênero:[F/M] '))
    genre1 = genre.upper()
    if genre1 == 'F' or genre1 == 'M':
        break
    elif genre1 == '':
        print('Você ainda não digitou seu gênero.')
        continue
    else:
        print('Gênero Inválido.')
        continue
while True:
    print('S - Solteiro')
    print('C - Casado')
    print('D - Divorciado')
    print('V - Viúvo')
    status = str(input('Qual é o seu estado civil?'))
    status1 = status.upper()
    if status1 == 'S' or status1 == 'C' or status1 == 'D' or status1 == 'V':
        break
    elif status1 == '':
        print('Você ainda não digitou seu estado civil.')
    else:
        print('Estado Civil Inválido.')

# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
popA = 80000
popB = 200000
cont = 0
while True:
    if popA < popB:
        popA = popA * 1.03
        popB = popB * 1.015
        cont += 1
        continue
    else:
        break
print('Em {0} ano(s) as populações de A e B estarão quantitativamente iguais'.format(cont))

# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

while True:
    while True:
        try:
            popA = int(input('Quanto será a população de A? '))
        except:
            print('Você ainda não informou a população de A.')
            continue
        else:
            break
    while True:
        try:
            popB = int(input('Quanto será a população de B? '))
        except:
            print('Você ainda não informou a população de B.')
            continue
        else:
            break
    while True:
        try:
            cresA = float(input('Quanto será o crescimento em A? '))
        except:
            print('Você ainda não informou quanto será o crescimento em A')
            continue
        else:
            break
    while True:
        try:
            cresB = float(input('Quanto será o crescimento em B? '))
        except:
            print('Você ainda não informou quanto será o crescimento em B')
            continue
        else:
            break
    if ((popA > popB) and (cresA < cresB)) or ((popA < popB ) and (cresA > cresB)):
        print('Operação executado com sucesso.')
        print('Você indicou que a população A é de {0} e a população B é de {1} e que o crescimento populacional de A'
          ' é {2} e que o crescimento populacional de B é {3}. Portanto a população delas irá se igualar em {4}'.format(
        popA, popB, cresA, cresB, cont))
        break
    else:
        print('OPERAÇÃO NÃO PERMITIDA.')
        print('Valores inválidos. Coloque valores que permitam a operação de forma correta.')
        continue

# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
# ele mostre os números um ao lado do outro.

print(list(range(1,21)))
for i in range(1,21):
    print(i)

# 7. Faça um programa que leia 5 números e informe o maior número.
# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 1
lista = []
while True:
    try:
        number = int(input('Digite o {0}º número: '.format(cont)))
    except:
        print('Você ainda não digitou o {0}º número.'.format(cont))
        continue
    if cont < 5:
        lista.append(number)
        cont += 1
        continue
    else:
        break
soma = sum(lista)
media = soma / 5
print('O número máximo desta lista de números é {0}'.format(max(lista)))
print('A soma destes números é {0} e a sua média é {1}'.format(soma, media))


# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print(list(range(1, 50, 2)))

# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# 11. Altere o programa anterior para mostrar no final a soma dos números.
while True:
    try:
        inteiro1 = int(input('Digite um número inteiro: '))
    except:
        print('Você ainda não digitou um número inteiro.')
        continue
    else:
        break
while True:
    try:
        inteiro2 = int(input('Digite um número inteiro: '))
    except:
        print('Você ainda não digitou um número inteiro.')
        continue
    else:
        break
print('A soma destes números inteiros é {0}'.format(inteiro1 + inteiro2))
print(list(range(inteiro1, inteiro2)))

# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
cont = 1
number = 1
while True:
    try:
        number = int(input('De 1 a 10, qual a tabuada que você deseja saber: '))
    except:
        print('Você ainda não digitou um número.')
    else:
        break
for i in range(1, 11):
    print('{0} X {1} = {2}'.format(number, i, number*i))

# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

while True:
    try:
        base = int(input('Digite um número inteiro: '))
    except:
        print('Você ainda não digitou um número inteiro.')
        continue
    else:
        break
while True:
    try:
        exponent = int(input('Digite mais um número inteiro: '))
    except:
        print('Você ainda não digitou um número inteiro.')
        continue
    else:
        break
print(pow(base,exponent))
print(base**exponent)

# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
cont = 1
pair = 0
odd = 0

while True:
    try:
        number = int(input('Digite o {0}º número inteiro de 10: '.format(cont)))
    except:
        print('Você ainda não digitou o {0}º número inteiro de 10.'.format(cont))
        continue
    if cont < 10:
        if number % 2 == 0:
            pair += 1
            cont += 1
        elif number % 2 != 0:
            odd += 1
            cont += 1
    else:
        break
print('Nessa amostragem, há {0} números pares e {1} números ímpares.'.format(pair, odd))

# 15.A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
# 16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.
fib = 1
fib1 = 1
cont = 1
print(1)
while True:
    try:
        parada = int(input('Digite até qual intereção de Fibonacci você gostaria: '))
    except:
        print('Você ainda não informou até qual intereção de Fibonacci você gostaria.')
        continue
    while cont < parada:
        fib += fib1
        fib1 += fib
        cont += 1
        print(fib)
        continue
    else:
        break
# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
value = 1
cont = 1
while True:
    try:
        fat = int(input('Digite um número inteiro para fazer seu fatorial: '))
    except:
        print('Você ainda não digitou um número inteiro.')
        continue
    while cont < fat:
        value = value*(cont+1)
        cont += 1
        continue
    else:
        break
print('O valor do {0}º fatorial é {1}'.format(fat, value))

# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.
lista = []
cont = 1
number = 0
while True:
    try:
        number = int(input('Digite o {0} número inteiro menor que 1000: '.format(cont)))
    except:
        print('Você ainda não digitou o {0} número inteiro.'.format(cont))
        continue
    if number <= 1000:
        break
    else:
        print('Número menor que 1000. Tente novamente.')
        continue
lista.append(number)
cont += 1
while True:
    try:
        number = int(input('Digite o {0} número inteiro menor que 1000: '.format(cont)))
    except:
        print('Você ainda não digitou o {0} número inteiro.'.format(cont))
        continue
    if number <= 1000:
        break
    else:
        print('Número menor que 1000. Tente novamente.')
        continue
lista.append(number)
cont += 1
while True:
    while True:
        try:
            choice = str(input('Você quer digitar mais um número inteiro:[S/N] '))
            choice = choice.upper()
        except:
            print('Você ainda não escolheu se quer digitar outro número inteiro ou não.')
            continue
        if choice == 'S':
            try:
                number = int(input('Digite o {0} número inteiro menor que 1000: '.format(cont)))
            except:
                print('Você ainda não digitou o {0} número inteiro.'.format(cont))
                continue
            if number <= 1000:
                lista.append(number)
                cont += 1
                continue
            elif number > 1000:
                print('Número menor que 1000. Tente novamente.')
                continue
        elif choice == 'N':
            print('Operação concluída!')
            break
        else:
            print('Escolha inválida! Tente novamente...')
            continue
    print('O maior valor dos números digitados é {0} e o menor é {1}'.format(max(lista), min(lista)))
    break

## ESTRUTURA DE REPETIÇÃO


# 1. Faça um Programa que peça dois números e imprima o maior deles.

while True:
    try:
        number1 = float(input('Digite um número: '))
    except:
        print('Você ainda não digitou o 1º número!')
        continue
    else:
        break
while True:
    try:
        number2 = float(input('Digite mais um número: '))
    except:
        print('Você ainda não digitou o 2º número!')
        continue
    else:
        break
lista = [number1,number2]
choice = str(input('Você quer continuar digitando números?[S/N] '))
count = 3
while choice == 'S':
    try:
        number3 = float(input('Digite mais um número: '))
        lista.append(number3)
        choice = str(input('Você quer continuar digitando números?[S/N] '))
        count += 1
    except:
        print('Você ainda não digitou o {}º número!'.format(count))
        continue



print('O maior número da lista é {0}'.format(max(lista)))
print('E o menor número da lista é {0}'.format(min(lista)))
print(lista)

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:
    try:
        value = float(input('Digite um valor: '))
    except:
        print('Voçê ainda não digitou um número.')
        continue
    else:
        break
if value > 0:
    print('Este número é positivo!')
elif value < 0:
    print('Este número é negativo!')
else:
    print('Este número é o zero!')

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.


while True:
    try:
        genre = str(input('Qual é o seu gênero:[M/F]'))
    except:
        print('Você ainda não digitou seu gênero.')
        continue
    else:
        break
if genre == 'M':
    print('Você é do sexo masculino!')
elif genre == 'F':
    print('Você é do gênero feminino!')
else:
    print('Sexo Inválido!')

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:
    try:
        letter = str(input('Digite uma letra: '))
    except:
        print('Você aida não digitou uma letra')
        continue
    else:
        break
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('Esta letra é uma vogal!')
else:
    print('Esta letra é uma consoante!')

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

while True:
    try:
        note1 = float(input('Digite a sua 1ª nota: '))
    except:
        print('Você ainda não digitou a 1ª nota.')
        continue
    else:
        break
while True:
    try:
        note2 = float(input('Digite a sua 2ª nota: '))
    except:
        print('Você ainda não digitou a 2ª nota.')
        continue
    else:
        break
average = (note1 + note2) / 2
if average <= 7:
    print('Reprovado!')
elif average == 10:
    print('Aprovado com Distinção!')
elif average >= 7:
    print('Aprovado!')

# 6. Faça um Programa que leia três números e mostre o maior deles.
# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

while True:
    try:
        number1 = float(input('Digite um número: '))
    except:
        print('Você ainda não digitou o 1º número!')
        continue
    else:
        break
while True:
    try:
        number2 = float(input('Digite mais um número: '))
    except:
        print('Você ainda não digitou o 2º número!')
        continue
    else:
        break
lista = [number1,number2]
choice = str(input('Você quer continuar digitando números?[S/N] '))
count = 3
while choice == 'S':
    try:
        number3 = float(input('Digite mais um número: '))
        lista.append(number3)
        choice = str(input('Você quer continuar digitando números?[S/N] '))
        count += 1
    except:
        print('Você ainda não digitou o {}º número!'.format(count))
        continue



print('O maior número da lista é {0}'.format(max(lista)))
print('E o menor número da lista é {0}'.format(min(lista)))
print(lista)

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato

while True:
    try:
        product1 = float(input('Qual o valor do Jeep Renegate?R$ '))
    except:
        print('Você ainda não digitou o valor do Jeep Renegate!')
        continue
    else:
        break
while True:
    try:
        product2 = float(input('Qual o valor da Range Rover Evoque?R$ '))
    except:
        print('Voçê ainda não digitou o preço da Range Rover!')
        continue
    else:
        break
while True:
    try:
        product3 = float(input('qual o valor da Range Rover Discovery Sport?RS '))
    except:
        print('Você ainda não digitou ainda não digitou o valor da Range Rover Dicovery Sport!')
        continue
    else:
        break

if product1 < product2 and product1 < product3:
    print('O carro mais barato é {0}'.format(product1))
elif product2 < product1 and product2 < product3:
    print('O carro mais barato é {0}'.format(product2))
else:
    print('O carro mais barato é {0}'.format(product3))

# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

from operator import itemgetter
dict = {'Evoque':product1, 'Dicovery':product2, 'Renegate':product3}
print('O valor dos carros em ordem decrescente é {0}'.format(sorted(dict.items(), key=itemgetter(1), reverse=True)))


# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

while True:
    try:
        print('M-matutino, V-Vespertino ou N- Noturno')
        shift = str(input('Em que turno você estuda?[M/V/N] '))
    except:
        print('Você ainda não digitou seu turno.')
        continue
    else:
        break
if shift == 'M':
    print('Bom dia!')
elif shift == 'V':
    print('Boa tarde!')
elif shift == 'N':
    print('Boa noite!')
else:
    print('Turno inválido!')

# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

while True:
    try:
        print('M-matutino, V-Vespertino ou N- Noturno')
        shift = str(input('Em que turno você estuda?[M/V/N] '))
    except:
        print('Você ainda não digitou seu turno.')
        continue
    else:
        break
if shift == 'M':
    print('Bom dia!')
elif shift == 'V':
    print('Boa tarde!')
elif shift == 'N':
    print('Boa noite!')
else:
    print('Turno inválido!')

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

while True:
    try:
        salary = float(input('Digite seu salário?R$ '))
    except:
        print('Você ainda não digitou seu salário.')
        continue
    else:
        break
if salary <= 280:
    newSalary = salary * 1.2
elif 280 < salary <= 700:
    newSalary = salary * 1.15
elif 700 < salary <= 1500:
    newSalary = salary * 1.1
elif 1500 < salary:
    newSalary = salary * 1.05
print('O seu salário passou de R${0} para R${1}'.format(round(salary,2),round(newSalary,2)))

# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

while True:
    try:
        hours = int(input('Quantas horas você trabalha por dia? '))
    except:
        print('Você ainda não digitou quantas horas você trabalha por dia.')
        continue
    else:
        break
while True:
    try:
        cost = float(input('Quanto você ganha por hora? '))
    except:
        print('Você ainda não digitou quanto você ganha por hora.')
        continue
    else:
        break
salary = hours * 20 * cost
FGTS = salary * 0.11
INSS = salary * 0.1
syndicate = salary * 0.03
if salary <= 900:
    IR = salary * 0
elif 900 < salary >= 1500:
    IR = salary * 0.05
elif 1500 < salary >= 2500:
    IR = salary * 0.1
elif 2500 < salary:
    IR = salary * 0.2
netSalary = salary - (IR + INSS + syndicate)
print('Seu salário bruto é R${0}. Você paga R${1} de INSS, R${2} de sindicato, e a empresa paga R${3} de FGTS. Portanto'
      ' seu salário líquido é R${4}.'.format(round(salary,2),round(INSS,2),round(syndicate,2),round(FGTS,2),round(netSalary,2)))

# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.
print('1 - Domingo')
print('2 - Segunda-feira')
print('3- Terça-feira')
print('4 - Quarta-feira')
print('5 - Quinta-feira')
print('6 - Sexta-feira')
print('7 - Sábado')
while True:
    try:
        dayOfWeek = int(input('Que dia da semana é hoje?[1 a 7} '))
    except:
        print('Você ainda não escolheu uma opção.')
        continue
    if dayOfWeek == 1 or dayOfWeek == 2 or dayOfWeek == 3 or dayOfWeek == 4 or dayOfWeek == 5 or dayOfWeek == 6 or dayOfWeek == 7:
        break
    else:
        print('Valor inválido!')
        continue
if dayOfWeek == 1:
    print('hoje é Domingo!')
elif dayOfWeek == 2:
    print('Hoje é Segunda!')
elif dayOfWeek == 3:
    print('Hoje é Terça!')
elif dayOfWeek == 4:
    print('Hoje é Quarta!')
elif dayOfWeek == 5:
    print('Hoje é quinta!')
elif dayOfWeek == 6:
        print('Hoje é Sexta!')
elif dayOfWeek == 7:
    print('Hoje é Sábado!')

# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

while True:
    try:
        note1 = float(input('Digite sua 1ª nota: '))
    except:
        print('Você ainda não digitou sua 1ª nota.')
        continue
    else:
        break
while True:
    try:
        note2 = float(input('Digite sua 2ª nota: '))
    except:
        print('Você ainda não digitou sua 2ª nota.')
        continue
    else:
        break
finalNote = (note1 + note2) / 2
if 9.0 < finalNote <= 10:
    note = 'A'
elif 7.5 < finalNote <= 9.0:
    note = 'B'
elif 6.0 < finalNote <= 7.5:
    note = 'C'
elif 4.0 < finalNote <= 6.0:
    note = 'D'
elif 0.0 < finalNote <= 4.0:
    note = 'E'
if note == 'A' or note == 'B' or note == 'C':
    approval = 'Parabéns, você foi aprovado!'
elif note == 'D' or note == 'E':
    approval = 'Infelizmente você foi reprovado.'
print('Sua primeira nota foi {0} e a sua segunda nota foi {1}. Portanto sua média é {2} e sua nota é {3}. Enfim... {4}'.format(note1,note2,finalNote,note,approval))

# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
while True:
    try:
        side1 = int(input('Digite o tamanho do 1º lado do triângulo: '))
    except:
        print('Você ainda não digitou o tamanho do 1º lado do triângulo.')
        continue
    else:
        break
while True:
    try:
        side2 = int(input('Digite o tamanho do 2º lado do triângulo: '))
    except:
        print('Você ainda não digitou o tamanho do 2º lado do triângulo.')
        continue
    else:
        break
while True:
    try:
        side3 = int(input('Digite o tamanho do 3º lado do triângulo: '))
    except:
        print('Você ainda não digitou o tamanho do 3º lado do triângulo.')
        continue
    else:
        break
if abs(side2 - side3) < side1 < side2 + side3 and abs(side1 - side3) < side2 < side1 + side3 and abs(side1 - side3) < side3 < side1 + side3:
    if side1 == side2 == side3:
        print('Este é um triângulo equilátero!')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Este é um triângulo isósceles')
    elif side1 != side2 != side3:
        print('Este é um triângulo escaleno!')
else:
    print('Estas medidas não são consideradas um triângulo.')

# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt


# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import date
while True:
    try:
        print('Digite uma data...')
        day = int(input('Dia: '))
    except:
        print('Você ainda não digitou um dia.')
        continue
    else:
        break
while True:
    try:
        month = int(input('Mês: '))
    except:
        print('Você ainda não digitou um mês.')
        continue
    else:
        break
while True:
    try:
        year = int(input('Ano: '))
    except:
        print('Você ainda não digitou um ano.')
        continue
    else:
        break
print(day,'/',month,'/',year)
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto!')

# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
while True:
    try:
        loto = str(input('Digite um número menor 1 trilhão: '))
    except:
        print('Você ainda não digitou um número.')
        continue
    else:
        break
if len(loto) == 1:
    print(loto[-1],'Unidade(s) de Real(is)')
elif len(loto) == 2:
    print(loto[-2],'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 3:
    print(loto[-3],'Centena(s)', loto[-2],'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 4:
    print(loto[-4], 'Milhar(es)', loto[-3],'Centena(s)', loto[-2],'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 5:
    print(loto[-5], 'Dezena(s) de', loto[-4], 'Milhar(es)', loto[-3],'Centena(s)', loto[-2],'Dezena(s) e', loto[-1],
          'Unidade(s) de Reais')
elif len(loto) == 6:
    print(loto[-6], 'Centena(s)', loto[-5], 'Dezena(s) de', loto[-4], 'Milhar(es)', loto[-3],'Centena(s)', loto[-2],
          'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 7:
    print(loto[-7], 'Milhão(ões)', loto[-6], 'Centena(s)', loto[-5], 'Dezena(s) de', loto[-4], 'Milhar(es)', loto[-3],
          'Centena(s)', loto[-2], 'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 8:
    print(loto[-8], 'Dezena(s) de', loto[-7], 'Milhão(ões)', loto[-6], 'Centena(s)', loto[-5], 'Dezena(s) de', loto[-4],
          'Milhares', loto[-3], 'Centena(s)', loto[-2], 'Dezena(s)', loto[-1], 'Unidade(s) de Reais')
elif len(loto) == 9:
    print(loto[-9], 'Centena(s) e', loto[-8], 'Dezena(s) de', loto[-7], 'Milhão(ões) e', loto[-6], 'Centena(s) e', loto[-5],
    'Dezena(s) de', loto[-4], 'Milhar(es)', loto[-3], 'Centena(s)', loto[-2], 'Dezena(s) e', loto[-1], 'Unidade(s) de Reais')
    print('Parabéns! Você é o mais novo MILHONÁRIO!!!!!!!')
else:
    print('Número inválido.')

# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

while True:
    try:
        note1 = float(input('Digite sua 1ª nota: '))
    except:
        print('Você ainda não digitou sua 1ª nota')
        continue
    else:
        break
while True:
    try:
        note2 = float(input('Digite sua 2ª nota: '))
    except:
        print('Você ainda não digitou sua 2ª nota')
        continue
    else:
        break
median = (note1 + note2) / 2
if median < 7:
    approval = 'Reprovado'
elif median == 10:
    approval = 'Aprovado com Distinção'
elif median >= 7:
    approval = 'Aprovado'
print('Sua média foi {0} portanto você foi {1}.'.format(median,approval))

# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
# uma nota de 5 e quatro notas de 1.

while True:
    try:
        money = str(input('De R$1,00 a R$600,00. Qual o valor do saque? '))
    except IndexError:
        print('Você ainda não digitou o valor do saque.')
    if money[-3] == '1' or money[-3] == '2' or money[-3] == '3' or money[-3] == '4' or money[-3] == '5' or (money[-3] == '6' and money[-2] == '0' and money[-1] == '0'):
        print('Obrigado pela preferência!')
        break
    else:
        continue
hundred = 0
fifty = 0
ten = 0
five = 0
one = 0
if money[-3] == '1':
    hundred = 1
elif money[-3] == '2':
    hundred = 2
elif money[-3] == '3':
    hundred = 3
elif money[-3] == '4':
    hundred = 4
elif money[-3] == '5':
    hundred = 5
elif money[-3] == '6':
    hundred = 6

if money[-2] == '1':
    ten = 1
elif money[-2] == '2':
    ten = 2
elif money[-2] == '3':
    ten = 3
elif money[-2] == '4':
    ten = 4
elif money[-2] == '5':
    fifty = 1
elif money[-2] == '6':
    fifty = 1
    ten = 1
elif money[-2] == '7':
    fifty = 1
    ten = 2
elif money[-2] == '8':
    fifty = 1
    ten = 3
elif money[-2] == '9':
    fifty = 1
    ten = 4

if money[-1] == '1':
    one = 1
elif money[-1] == '2':
    one = 2
elif money[-1] == '3':
    one = 3
elif money[-1] == '4':
    one = 4
elif money[-1] == '5':
    five = 1
elif money[-1] == '6':
    five = 1
    one = 1
elif money[-1] == '7':
    five = 1
    one = 2
elif money[-1] == '8':
    five = 1
    one = 3
elif money[-1] == '9':
    five = 1
    one = 4
print('Você precisa sacar R${0}. Portanto,  receberá: {1} nota(s) de R$100, {2} nota(s) de R$50, {3} nota(s) de R$10,'
      ' {4} nota(s) de R$5 e {5} moedas de R$1'.format(money,hundred,fifty,ten,five,one))

# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
while True:
    try:
        number = float(input('Digite um número: '))
    except:
        print('Você ainda não digitou um número.')
        continue
    else:
         break

if (number // 1 == number):
    entireOrDecimal = 'inteiro'
    if number % 2 == 0:
        evenOrOdd = 'par'
        if number > 0:
            positiveOrNegative = 'positivo'
        elif number < 0:
            positiveOrNegative = 'negativo'
        print('Este número é {0}, {1} e {2}'.format(positiveOrNegative, entireOrDecimal, evenOrOdd))
    elif number % 2 != 0:
        evenOrOdd = 'ímpar'
        if number > 0:
            positiveOrNegative = 'positivo'
        elif number < 0:
            positiveOrNegative = 'negativo'
        print('Este número é {0}, {1} e {2}'.format(positiveOrNegative, entireOrDecimal, evenOrOdd))
else:
    entireOrDecimal = 'decimal'
    if number > 0:
        positiveOrNegative = 'positivo'
    elif number < 0:
        positiveOrNegative = 'negativo'
    print('Este número é {0} e {1}'.format(positiveOrNegative,entireOrDecimal))

# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

while True:
    try:
        print('Responda "s" para SIM e "n" para NÃO')
        phoned = str(input('Telefonou para a vítima?'))
    except:
        print('Você ainda não respondeu à pergunta.')
        continue
    if phoned == 'n' or phoned == 's':
        break
while True:
    try:
        print('Responda "s" para SIM e "n" para NÃO')
        place = str(input('Esteve no local do crime?'))
    except:
        print('Você ainda não respondeu à pergunta.')
        continue
    if place == 'n' or place == 's':
        break
while True:
    try:
        print('Responda "s" para SIM e "n" para NÃO')
        live = str(input('Mora perto da vítima?'))
    except:
        print('Você ainda não respondeu à pergunta.')
        continue
    if live == 'n' or live == 's':
        break
while True:
    try:
        print('Responda "s" para SIM e "n" para NÃO')
        debt = str(input('Devia para a vítima?'))
    except:
        print('Você ainda não respondeu à pergunta.')
        continue
    if debt == 'n' or debt == 's':
        break
while True:
    try:
        print('Responda "s" para SIM e "n" para NÃO')
        worked = str(input('Já trabalhou com a vítima?'))
    except:
        print('Você ainda não respondeu à pergunta.')
        continue
    if worked == 'n' or worked == 's':
        break
point = 0
if phoned == 's':
    point += 1
if place == 's':
    point += 1
if live == 's':
    point += 1
if debt == 's':
    point += 1
if worked == 's':
    point += 1
if point < 2:
    print('Inocente!')
if point == 2:
    print('Suspeita!')
if 2 < point <= 4:
    print('Cumplice!')
if point == 5:
    print('Culpado(a)!')






















