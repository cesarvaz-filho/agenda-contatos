
# Agenda de Contatos - CLI

Este é um projeto de linha de comando (CLI) desenvolvido em Python para gerenciar uma agenda de contatos. O programa permite criar, listar, atualizar e deletar contatos, armazenando os dados em um arquivo `.csv`.

## Funcionalidades

1. **Criar Contato**: Adicionar um novo contato com Nome, Telefone e Email.
2. **Listar Contatos**: Exibir todos os contatos cadastrados.
3. **Atualizar Contato**: Editar as informações de um contato existente.
4. **Deletar Contato**: Remover um contato da agenda.

## Requisitos

- **Python 3.7** ou superior instalado na máquina.

## Como Executar

1. **Clone ou faça o download do repositório**:
   ```bash
   git clone https://github.com/cesarvaz-filho/agenda-contato.git
   cd agenda-contato
   ```

2. **Verifique se você tem o Python instalado**:
   - Execute `python --version` ou `python3 --version` para verificar a versão instalada.
   - Caso não tenha o Python instalado, [faça o download aqui](https://www.python.org/downloads/).

3. **Execute o programa**:
   - No terminal, execute:
     ```bash
     python main.py
     ```
   - Ou, dependendo da configuração do seu sistema:
     ```bash
     python3 main.py
     ```
   - Caso esteja usando o VSCode pode clicar no botão 'Run' no canto superior direito.

4. **Interaja com o menu**:
   - O programa exibirá um menu com as opções:
     ```
     Agenda de Contatos
     1. Criar Contato
     2. Listar Contatos
     3. Atualizar Contato
     4. Deletar Contato
     5. Sair
     ```

5. **Saída do arquivo**:
   - Os contatos serão salvos automaticamente em um arquivo chamado `contacts.csv` no mesmo diretório do programa.

## Estrutura do Projeto

```plaintext
agenda-contato/
├── main.py         # Código principal do projeto
├── contacts.csv    # Arquivo gerado para salvar os dados
└── README.md       # Instruções e detalhes do projeto
```

## Observações

- O arquivo `contacts.csv` será criado automaticamente na primeira execução, caso ainda não exista.
- Certifique-se de não excluir ou modificar manualmente o arquivo `contacts.csv` para evitar problemas com o programa.

