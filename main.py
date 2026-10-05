import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def imagem(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./img/{attachment.filename}")
            passaro, porcentagem = get_class(model_path='converted_keras/keras_model.h5',labels_path='converted_keras/labels.txt',image_path=f'./img/{file_name}')
            if passaro == 'Pombos\n':
                await ctx.send(f'Acho que é pombo, tenho {(porcentagem*100):.2f}% de certeza')
            elif passaro == 'Pardais\n':
                await ctx.send(f'Acho que é pardal, tenho {(porcentagem*100):.2f}% de certeza')
            
    else:
        await ctx.send("Você esqueceu de enviar a imagem :(")



bot.run("")