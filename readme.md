# Bot de Whitelist Discord

Este é um bot Discord personalizado projetado para gerenciar a whitelist de um servidor de GTA V RP. O bot monitora um canal de texto específico e permite que os membros solicitem acesso à whitelist. Ele verifica o número de jogador no banco de dados e atribui um cargo específico se o jogador estiver autorizado.

## Requisitos

- Python 3.x
- discord.py (versão 1.x ou superior)
- Biblioteca mysql.connector
- Token de bot do Discord

## Configuração

1. Clone este repositório.
2. Instale as dependências usando `pip install discord.py mysql-connector-python`.
3. Configure o banco de dados MySQL e atualize as informações de conexão no código.
4. Configure o token do bot do Discord.

## Uso

- Use `!dchat` para definir o canal de texto a ser monitorado pelo bot.
- Use `!dcargo "Nome do Cargo"` para definir o cargo a ser atribuído aos membros autorizados.
- O bot monitorará o canal definido e responderá às mensagens que contêm números válidos.
- Quando um número é recebido, o bot verifica o banco de dados e atribui o cargo, se apropriado.
