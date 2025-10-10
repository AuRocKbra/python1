
def validar_numero_par_impar():
    numero_escolhido = int(input('Informe um número:'))
    if numero_escolhido % 2 == 0:
        print(f'O numero {numero_escolhido} é par')
    else:
        print(f'O número {numero_escolhido} é impar')

def valida_idade():
    idade = int(input('Informe sua idade: '))
    if 0 <= idade <= 12:
        print('você está classificado como criança')
    elif 13 <= idade <= 18:
        print('você está classificado como adolescente')
    else:
        print('você está classificado como adulto')

def valida_usuario_senha():
    usuario = input('Informe seu login:')
    senha = input('Informe sua senha:')
    if(usuario == 'admin' and senha == 'admin'):
        print('Login efetuado com sucesso')
    else:
        print('Login ou senha incorretos')

def validar_coordenadas():
    x = int(input('Informe a coordenada x:'))
    y = int(input('Informe a coordenada y:'))
    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('Ponto definido na origem')

validar_numero_par_impar()
valida_idade()
valida_usuario_senha()
validar_coordenadas()