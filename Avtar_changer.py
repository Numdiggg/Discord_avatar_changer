import discord
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

client = discord.Client()

def get_bot_token():
    while True:
        try:
            token = input(Fore.YELLOW + "Enter your Discord bot token: " + Style.RESET_ALL).strip()
            if not token:
                raise ValueError(Fore.RED + "Token cannot be empty." + Style.RESET_ALL)
            return token
        except ValueError as ve:
            print(ve)

def get_avatar_filename():
    while True:
        try:
            filename = input(Fore.YELLOW + "Enter the name of the avatar file (e.g., avatar.gif): " + Style.RESET_ALL).strip()
            if not filename or not os.path.exists(filename):
                raise ValueError(Fore.RED + "Invalid file name or file does not exist." + Style.RESET_ALL)
            return filename
        except ValueError as ve:
            print(ve)

async def change_avatar(filename):
    try:
        # Change avatar
        with open(filename, 'rb') as avatar_file:
            avatar_image = avatar_file.read()
        await client.user.edit(avatar=avatar_image)
        print(Fore.GREEN + "Avatar changed successfully!" + Style.RESET_ALL)
    except discord.errors.HTTPException as e:
        print(Fore.RED + f"Failed to change avatar: {e}" + Style.RESET_ALL)

@client.event
async def on_ready():
    print(Fore.CYAN + f'We have logged in as {client.user}' + Style.RESET_ALL)
    avatar_filename = get_avatar_filename()
    await change_avatar(avatar_filename)
    await client.close()

# Run the bot
if __name__ == "__main__":
    try:
        token = get_bot_token()
        client.run(token)
    except discord.LoginFailure:
        print(Fore.RED + "Error: Invalid token provided. Please check your token and try again." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)
    finally:
        input(Fore.CYAN + "Press any key to exit..." + Style.RESET_ALL)
