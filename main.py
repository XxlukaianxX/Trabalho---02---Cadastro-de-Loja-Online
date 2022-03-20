#Funções#

#Informações iniciais para o funcionamento do programa
def informacoes_padrao():
    #Variáveis globais
    global sim_nao, opcoes, cadastrados, perguntas_cadastro, texto_def, perguntas_login, perguntas_endereco

    #Texto main - Pergunta para o usuário o que deseja fazer
    opcoes = """\n    _-========- Loja -========-_ 
 _-¨                            ¨-_
* [1] Cadastrar cliente            *
* [2] Adicionar endereço a cliente *
* [3] Mostrar dados do cliente     *
* [4] Mostrar clientes cadastrados *
* [0] Sair                         *
*_                                _*
  ¨-============================-¨

O que deseja fazer? """

    #Listas para o funcionamento do programa - 0, 1
    sim_nao = [['sim', 's', 'yes', 'y'], ['não', 'nao', 'n', 'no']]
    
    #Lista de cadastrados
    cadastrados = []

    #Listas de perguntas
    #0, 1, 2, 3, 4, 5
    perguntas_cadastro = ['Nome completo: ', 'Data de nascimento: ', 'E-mail: ', 'Login: ', 'Senha: ', 'Número de celular: ']
    #0, 1
    perguntas_login = ['Qual o login do cliente? ', 'Informe a senha para prosseguir: ']
    #0, 1, 2, 3, 4, 5, 6
    perguntas_endereco = ['Rua: ', 'Número: ', 'Complemento: ', 'Bairro: ', 'Cidade: ', 'CEP: ', 'Ponto de referência: ']
    #Textos das def - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    texto_def = ['\nEsse E-mail já está associado a uma conta cadastrada. Informe outro E-mail para prosseguir!','\nEsse login já está sendo usado! Por favor, escolha outro login.', '\nDeseja enviar o cadastro? (S/N) ', '\n\nO envio do cadastro foi cancelado. Para tentar novamente o cadastro, basta escolher a opção "[1] Cadastrar cliente" e preencher os campos novamente!', '\nDeseja mesmo sair? (S/N) ', f'\nPrograma finalizado com êxito!\n{criador_linhas(30, "¨")}', '\nDeseja enviar as informações acima? ', f'\n\nEnvio cancelado com êxito!\n{criador_linhas(26, "¨")}', '\nDeseja voltar ao menu inicial? ', '\nInforme um login existente para prosseguir.']

#Função para não deixar o campo em branco ser enviado
def sem_texto_nao(i, info, pergunta):
    while True:
        info = input(f'{pergunta[i]}').strip()
        if (info == ''):
            print('\n*Campo em branco* Preencha para prosseguir.')
        elif (info in sim_nao[0] or info in sim_nao[1]):
            print('Esse nome não pode ser utilizado aqui.')
        else:
            return info

#Checa se o login, E-mail e entre outras informações estão disponíveis para uso
def checando_disponibilidade(info, texto, pergunta, variacao):
    while True:
        ja_existente = False

        for i in range(len(cadastrados)):
            if (pergunta == 3 and info == cadastrados[i][3][7:] or pergunta == 2 and info == cadastrados[i][2][8:]):
                print(texto)
                ja_existente = True

                #Caso exista o login
                if (variacao == 'login'):
                    return i

            #Caso não exista o login
            if (variacao == 'login' and i == len(cadastrados)-1):
                return 'inexistente'

        if (ja_existente == True):
            info = input(f'\n{perguntas_cadastro[pergunta]}').strip()
            if (info == ''):
                print('*Campo em branco* Preencha para prosseguir')
        elif (ja_existente == False and info != ''):
            return info

#Design - Criador de Linhas
def criador_linhas(tamanho, caracter):
    linha = ''
    for i in range(tamanho):
        linha += caracter
    return linha

#Cadastrar cliente
def cadastrar_cliente():
    #Início
    print(f'\nPreenchar todos os campos corretamente a seguir para realizar o cadastro!\n{criador_linhas(73, "¨")}')
    
    #Informações do usuário
    informacoes_usuario = []

    #Perguntas para o usuário responder - add em uma lista
    for i in range(len(perguntas_cadastro)):
        #Perguntas para o cadastro
        informacao = ''
        informacao = sem_texto_nao(i, informacao, perguntas_cadastro)

        #Confere se o login e E-mail digitado já existe e pede para ao usuário que escolher outro
        #E-mail
        if (i == 2):
            informacao = checando_disponibilidade(informacao, texto_def[0], 2, None)
        #Login
        elif (i == 3):
            informacao = checando_disponibilidade(informacao, texto_def[1], 3, None)

        informacoes_usuario += [perguntas_cadastro[i] + informacao]
    
    #Exibe ao usuário os dados digitados e pergunta se deseja enviar ou cancelar para refazer
    print('\n\nConfira se todas as informações estão corretas.\n')
    print(f'{criador_linhas(27, "= ")}')
    for i in range(len(informacoes_usuario)):
        print(f'{informacoes_usuario[i]}')
    print(f'{criador_linhas(27, "= ")}')
    
    sair(texto_def[2], texto_def[3], 0, informacoes_usuario)

#Adiciona o endereço dos clientes
def add_endereco_cliente():
    #Sistema de login
    permissao = login(perguntas_login)

    #Lista de informações sobre o endereço
    endereco = []
    informacao = ''

    if (cadastrados != []):
        if (permissao[0] == True):
            print(f'\nPara adicionar um endereço a um cliente, basta informa o login e senha do mesmo.\n{criador_linhas(80, "¨")}')

            for i in range(len(perguntas_endereco)):
                informacao = sem_texto_nao(i, informacao, perguntas_endereco)
                endereco += [perguntas_endereco[i] + informacao]
                
            print(f'\n\nCertifique-se se as informações abaixo estão correta.\n{criador_linhas(27, "¨ ")}')
            for i in range(len(endereco)):
                print(f'{endereco[i]}')
            print(f'{criador_linhas(27, "- ")}')
                
            if (sair(texto_def[6], texto_def[7], 2, None) == True):
                print(f'\n\nEndereço cadastrado com sucesso!\n{criador_linhas(32, "¨")}')
                cadastrados[permissao[1]] += [endereco]

#Mostra dados do cliente
def dados_clientes():
    #Sistema de login
    permissao = login(perguntas_login)
    
    #Print - Todas as informações do usuário
    if (cadastrados != []):
        if (permissao[0] == True):
            #Variáveis
            n = 0
            #Texto informativo
            print(f'\nEssas são todos as informações do {cadastrados[permissao[1]][3][7:]}.\n{criador_linhas(35+len(cadastrados[permissao[1]][3][7:]), "¨")}')

            for i in range(len(cadastrados[permissao[1]])):
                if (i > 5):
                    n += 1
                    print(f'\nEndereço {n}\n{criador_linhas(54, "¨")}')

                    for x in range(len(cadastrados[permissao[1]][i])):
                        print(f'{cadastrados[permissao[1]][i][x]}')
                else:
                    print(f'{cadastrados[permissao[1]][i]}')
            print(criador_linhas(27, '= '))

        input('\n\nPressione "Enter" para voltar ao menu inicial...')

#Clientes cadastrados
def clientes_cadastrados():
    print()
    if (cadastrados == []):
        print('Nenhum cliente foi cadastrado ainda. Para cadastrar novos clientes bastas ir na opção: "[1] Cadastrar cliente".')
    else:
        print(f'Está lista mostra o nome e login de todos os usuários cadastrados.\n{criador_linhas(66, "¨")}')

        for i in range(len(cadastrados)):
            print(f'{criador_linhas(27, "= ")}')
            print(f'Usuário número: {i+1}\n\n{cadastrados[i][0]}\n{cadastrados[i][3]}')
        print(f'{criador_linhas(27, "= ")}')
        print(f'\nTotal de usuários cadastrados: {i+1}')

    input('\n\nPressione "Enter" para voltar ao menu inicial...')

#Sistema de login
def login(perguntas):
    #Caso não tenha nenhum cadastro
    if (cadastrados == []):
        print('\nNenhum cliente foi cadastrado ainda. Para cadastrar novos clientes bastas ir na opção: "[1] Cadastrar cliente".')
        input('\n\nPressione "Enter" para voltar ao menu inicial...')
    #Caso tenha
    else:
        informacao = ''
        voltar = False
        print()

        for i in range(len(perguntas)):
            informacao = sem_texto_nao(i, informacao, perguntas)
            
            #Checa se o login existe
            if (i == 0):
                while True:
                    informacao = checando_disponibilidade(informacao, '', 3, 'login')
                    #Caso não exista
                    if (informacao == 'inexistente'):
                        print('\nLogin inexistente! Por favor, informe um login existente.')
                        voltar = sair(texto_def[8], texto_def[9], 2, None)
                        if (voltar == True):
                            return False, None

                        #Pergunta novamente o login
                        informacao = sem_texto_nao(0, informacao, perguntas)
                    #Caso exista
                    else:
                        login = informacao
                        break

            #Verificação da senha
            else:
                for i in range(5):
                    if (informacao == cadastrados[login][4][7:]):
                        print(f'\n{criador_linhas(27, "= ")}')
                        print(f'Usuário:{cadastrados[login][3][6:]}\n- - -\nLogin bem sucedido!')
                        print(f'{criador_linhas(27, "= ")}')
                        return True, login

                    elif (i == 4):
                        print('\nLimite de tentativas excedidas! Você será redirecionado ao menu inicial.')
                        return False, None
                    else:
                        print('\nSenha incorreta! Informe a senha correta.')
                        #Pergunta novamente a senha
                        informacao = sem_texto_nao(1, informacao, perguntas)

#Sair
def sair(t1, t2, acao, info_user):
    #Variáveis globais
    global cadastrados

    while True:
        #Pergunta para o usuário
        sair = input(t1).lower().strip()

        if (sair in sim_nao[0] or sair in sim_nao[1]):
            if (sair in sim_nao[0]):
                #Adiciona as informações para a lista de cadastrados
                if (acao == 0):
                    print('\n\nCadastro finalizado com sucesso!')
                    cadastrados += [info_user]
                
                #Fecha o programa
                elif (acao == 1):
                    print(t2)
                    exit()

                return True
            else:
                if (acao != 1):
                    print(t2)
                return False
        else:
            print('\n***Tente usar "sim" ou "não" para responder.***')


#Main#

#Standart - Sistema
informacoes_padrao()

#Loop principal
while True:
    #Pergunta para usuário
    escolha_do_usuario = input(f'\n{opcoes}')

    #Cadastrar cliente
    match escolha_do_usuario:
        case '1':
            cadastrar_cliente()

        #Adicionar endereço a cliente
        case '2':
            add_endereco_cliente()

        #Mostrar dados do cliente
        case '3':
            dados_clientes()

        #Mostrar clientes cadastrados
        case '4':
            clientes_cadastrados()

        #Sair
        case '0':
            sair(texto_def[4], texto_def[5], 1, None)

        case _:
            print('\nItem inexistente! Escolha uma das opções abaixo.')
