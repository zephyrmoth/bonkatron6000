import discord
import json
import sys

# TODO: set up proper logging
# Custom emoji keys are obtainable by escaping emoji
# Yes the error messages are intentionally cursed
class BonkatronClient(discord.Client):
    # Init and load bonkable list
    def __init__(self, bonkable_list):
        self.bonkable_list = bonkable_list
        super().__init__()

    # Error checking on boot
    async def on_ready(self):
        print("Hewwo Wowld :3! It's me {}".format(self.user))
        print(self.bonkable_list)
    
    #Check if user is in "bonkable" list
    async def on_message(self, message):
        if str(message.author.id) in self.bonkable_list.keys():
            user_id = str(message.author.id)
            bonkable = False
            #This is almost certainly not super efficient but this is entirely a goof
            for string in self.bonkable_list[user_id]["strings"]:
                if string in message.content:
                    bonkable = True
                    break
            if bonkable:
                emoji = None
                if isinstance(self.bonkable_list[user_id]["react"], str):
                    emoji = self.bonkable_list[user_id]["react"]
                elif isinstance(self.bonkable_list[user_id]["react"], int):
                    emoji = self.get_emoji(self.bonkable_list[user_id]["react"])
                    if not emoji:
                        print("Oh noes, invalid emoji ;-;")
                        return
                else:
                    print("Oh noes, invalid emoji format ;-;")
                    return
                print("Bonked {} :3".format(message.author.display_name))
                await message.add_reaction(emoji)
    
def get_bonk_list():
    bonk_file = open("./bonkable.json", "r")
    bonkable_list = json.loads(bonk_file.read().strip())
    return bonkable_list

if __name__ == '__main__':
    # Load external conf file
    bonkable_list = get_bonk_list()
    #Read client secret from client.secret
    try:
        discord_keyfile = open("./discord.token", "r")
        DISCORD_TOKEN = discord_keyfile.read().strip()
    except:
        print("Could not find Discord bot token! Exiting...")
        sys.exit(1)
    client = BonkatronClient(bonkable_list)
    client.run(DISCORD_TOKEN)