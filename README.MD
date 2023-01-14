
# Cadastro de Loja Online

2° Trabalho de **FUP** do 1º semestre do curso de **Engenharia de Software na UFC**.
<br>
Projeto desenvolvido em **Python**.
## Como Usar

Com o Python instalado, utilize o comando:

```python
  python main.py
```
## Dados do Cadrasto

- **Informações da Conta**
    <br>
    `Nome completo` `Data de nascimento`
    <br>
    `E-mail` `Login` `senha` `Número de celular`

- **Endereços para entrega**
    <br>
    `Rua` `Número` `Complemento` `Bairro`
    <br>
    `Cidade` `CEP` `Ponto de referência`


## Estrutura do Programa

- **[1] Cadastrar cliente :** adiciona um novo cliente com os dados mencionados na seção anterior, exceto o endereço.o. Não permita a criação de dois clientes com o mesmo login. Se o usuário escolher um login já existente, mostre uma mensagem de erro, não realize o cadastro e retorne ao menu principal.
- **[2] Adicionar endereço a cliente:** cadastra um endereço de entrega a um cliente previamente cadastrado. Caso o cliente escolhido não exista, o programa deve acusar um erro e voltar ao menu inicial. Caso contrário, o programa deve pedir as informações de endereço mencionadas na seção anterior e associá-las ao cliente escolhido.
- **[3] Mostrar dados do cliente:** deve exibir todos os dados de um cliente específico e os endereços associados a ele. Para acessar os dados de um cliente, peça o seu login. Se o login entrado não existir, mostre uma mensagem de erro e retorne ao menu principal.
- **[4] Mostrar clientes cadastrados:** exibe os nomes de todos os clientes já cadastrados no sistema e seus respectivos logins.
- **[0] Sair:** termina a execução do programa
## Desenvolvedor

[@lukaian](https://github.com/lukaian-k)
