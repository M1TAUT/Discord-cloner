import sys
import time
import asyncio
import platform
from os import system

import discord
import colorama
from colorama import Fore, init, Style
from serverclone import Clone

init()

os_type = platform.system()

mytitle = "Клонер - Developed by SaiDark"
if os_type == "Windows":
    system("title " + mytitle)

if os_type == "Windows":
    system("cls")
else:
    system("clear")

client = discord.Client()
print(f"""{Fore.MAGENTA}

                                    ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                    ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                    ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                                    ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                                    ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                                    ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                              {Fore.CYAN}   Создатель: APEXMIND.{Style.RESET_ALL}
        """)
token = input(f'1. Введите токен аккаунта:\n >>')
guild_s = input('2. Id сервера который нужно скопировать:\n >>')
guild = input('3. Id сервера куда нужно вставить:\n >>')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id

print("  ")
print("  ")


@client.event
async def on_ready():
    extrem_map = {}
    print(f"Вход с аккаунта : {client.user}")
    print("Клонирование началось")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))

    if not guild_from or not guild_to:
        print(
            f"{Fore.RED}[ERROR] Один или оба сервера не найдены. Проверьте ID и убедитесь, что аккаунт находится на обоих серверах.{Style.RESET_ALL}")
        await client.close()
        return

    try:
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Произошла ошибка во время клонирования: {e}{Style.RESET_ALL}")

    print(f"""{Fore.BLUE}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


# Запуск клиента
try:
    asyncio.run(client.start(token))
except discord.LoginFailure:
    print(f"{Fore.RED}[ERROR] Неверный токен аккаунта или в доступе отказано.{Style.RESET_ALL}")
