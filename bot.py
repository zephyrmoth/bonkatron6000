import discord

#TODO: move to external conf file
#TODO: set up proper logging
#custom emoji keys are obtainable by escaping emoji
TEMP_BONKABLE_LIST = {269310283439144961:{"strings":["bonk me"], "react":"💯"},458362561130397707:{"strings":["uwu", "UwU", "owo", "OwO"], "react":915287209077248030}}
class BonkatronClient(discord.Client):
    async def on_ready(self):
        print("Hewwo Wowld :3! It's me {}".format(self.user))
    
    #Check if user is in "bonkable" list
    async def on_message(self, message):
        print("Message received {} :3".format(message.author.id))
        if message.author.id in TEMP_BONKABLE_LIST.keys():
            print("Bonkable user :3")
            user_id = message.author.id
            bonkable = False
            #This is almost certainly not super efficient but this is entirely a goof
            for string in TEMP_BONKABLE_LIST[user_id]["strings"]:
                if string in message.content:
                    bonkable = True
                    break
            if bonkable:
                print("Bonk :3".format(self.user))
                emoji = None
                if isinstance(TEMP_BONKABLE_LIST[user_id]["react"], str):
                    emoji = TEMP_BONKABLE_LIST[user_id]["react"]
                elif isinstance(TEMP_BONKABLE_LIST[user_id]["react"], int):
                    emoji = self.get_emoji(TEMP_BONKABLE_LIST[user_id]["react"])
                else:
                    print("Oh noes, invalid emoji ;-;")
                    return
                await message.add_reaction(emoji)

if __name__ == '__main__':
    #Read client secret from client.secret
    try:
        discord_keyfile = open("./discord.token", "r")
        DISCORD_TOKEN = discord_keyfile.read().strip()
    except:
        print("Could not find Discord bot token! Exiting...")
        sys.exit(1)
    client = BonkatronClient()
    client.run(DISCORD_TOKEN)