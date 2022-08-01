import disnake
from disnake.ext import commands
from SimpleQIWI import *
import pyqiwi

token = "токен бота" #discord.com/developers/applications
bot = commands.Bot(command_prefix="ваш префикс")

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов') #сообщение в консоли при запуске бота, можно написать что угодно
    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Game(name="название игры")) #idle можно заменить на online/dnd/offline
    
@bot.command(aliases=["bal", "b"]) #bal и b это "аллиасы" команды, т.е ее можно использовать и командой balance и bal и b
@commands.is_owner() #команда доступна только владельцу бота на discord.com/developers/applications
async def balance(ctx, qtoken): #qtoken это аргумент по которому бот получает токен киви кошелька
    wallet = pyqiwi.Wallet(token=qtoken, number='70000000000') #номер можно не менять
    amount = wallet.balance()
    embed = disnake.Embed(title=f"Баланс по токену {qtoken}", description=f"**`{amount} RUB`**", color=0xFFA500)
    await ctx.send(embed=embed, delete_after=5) #delete_after=5 удаляет сообщение через 5 секунд, можно стереть
    await ctx.message.delete() #удаляет сообщение с командой(!bal <token>)
 
bot.run(token)
