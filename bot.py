import discord
from discord.ext import commands
import mysql.connector

# Configuração do bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# Substitua 'TOKEN_DO_SEU_BOT' pelo token real do seu bot Discord
TOKEN = 'TOKEN_DO_SEU_BOT'

# Configuração da conexão com o banco de dados MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vrp"
)

cursor = db_connection.cursor()


@bot.event
async def on_ready():
    print(f'Bot está conectado como {bot.user.name}')


cursor.execute('SELECT * FROM discord_config WHERE id = 0', )
config = cursor.fetchone()

cargo_definido = config[1]
chat_monitorado = config[2]


@bot.command()
async def dchat(ctx):
    global chat_monitorado

    chat_monitorado = ctx.message.channel

    await ctx.send(f'Chat monitorado definido para: {chat_monitorado.mention}')

    # Obtém o ID do canal
    chat_id = ctx.message.channel.id

    # Atualiza o valor no banco de dados
    cursor.execute('UPDATE discord_config SET chat = %s WHERE id = 0', (chat_id,))
    db_connection.commit()


@bot.command()
async def dcargo(ctx, *, cargo_nome: str):
    global cargo_definido

    # Procura o cargo pelo nome no servidor
    cargo_definido = discord.utils.get(ctx.guild.roles, name=cargo_nome)

    if cargo_definido:
        await ctx.send(f'Cargo definido para: {cargo_definido.mention}')

        # Obtém o ID do cargo
        cargo_definido = cargo_definido.id

        # Atualiza o valor no banco de dados
        cursor.execute('UPDATE discord_config SET cargo = %s WHERE id = 0', (cargo_definido,))
        db_connection.commit()
    else:
        cargo_definido = None
        await ctx.send(f'O cargo "{cargo_nome}" não foi encontrado no servidor.')


@bot.event
async def on_message(message):
    global chat_monitorado, cargo_definido

    cargo = message.guild.get_role(int(cargo_definido))
    chat = message.guild.get_channel(int(chat_monitorado))

    if chat and cargo:
        if message.channel == chat and message.content.isdigit():
            numero = int(message.content)

            # Executa a consulta e obtém os resultados
            cursor.execute('SELECT * FROM vrp_users WHERE id = %s', (numero,))
            jogador = cursor.fetchone()

            if jogador:
                whitelisted = jogador[3]
                if whitelisted == 0:
                    cursor.execute('UPDATE vrp_users SET whitelisted = 1 WHERE id = %s', (numero,))
                    db_connection.commit()
                    await message.author.add_roles(cargo)
                    await message.channel.send(f"{message.author.mention}, seu passaporte foi ativado.")
                else:
                    await message.channel.send(f"{message.author.mention}, seu passaporte já está ativado.")
            else:
                await message.channel.send(f"{message.author.mention}, você precisa tentar acessar a cidade uma vez para receber um passaporte.")

    await bot.process_commands(message)

bot.run(token=TOKEN)
