import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

frases_romanticas = [
    "Eres lo mejor que me ha pasado en la vida. ❤️",
    "Te amo con el alma velita ❤️",
    "Gracias por hacerme el hombre mas feliz de el mundo ❤️",
    "muak muak",
]

@bot.event
async def on_ready():
    print(f"¡{bot.user} está conectado y listo para recordarte lo mucho que te amo!")

@bot.command(name="amor")
async def amor(ctx):
    frase_elegida = random.choice(frases_romanticas)
    embed = discord.Embed(
        title="Mensaje de mi para ti ",
        description=frase_elegida,
        color=0xFF69B4
    )
    await ctx.send(embed=embed)

# El bot toma el token de forma segura desde la nube
bot.run(os.getenv("DISCORD_TOKEN"))