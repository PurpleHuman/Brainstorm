### BrainstormPY est. 2018, Went live on: 30th April 2018 ###

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from random import choice
import decimal
import datetime
import time
import traceback

def __init__(self, bot):
        self.bot = bot

bot = commands.Bot(command_prefix='=')
Client = Bot('=')
bot.remove_command('help')
owner = ["329103009600503808"]
verson = "v0.15.4.12"
case_sensive=False
ownername = "Purple Human"
TOKEN = 
discordpy = (discord.__version__)
gametimestatus = [0 or 1]


@bot.event
async def on_ready():

    users = str(len(set(bot.get_all_members())))
    servers = str(len(bot.servers))


    
    embed=discord.Embed(title="Brainstorm is up, Running Verson: {}".format(verson), description="The owner of Brainstorm is {}, and I'm running discord.py version {}".format(ownername, discordpy), color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Currently serving:", value="**{}** users. :heart: ".format(users), inline=False)
    embed.add_field(name="Currently in:", value="**{}** servers. :heart: ".format(servers), inline=False)
    server = bot.get_server("519653819483684875")
    await bot.send_message(server.get_channel("522257168414801923"), embed=embed)

    print(f'#--------------------------------------------------------------#\n'
          f'| Launch process Successful. Brainstorm {verson} is now Live!.\n'
          f'#--------------------------------------------------------------#\n'
          f'| Username:  Brainstorm | =help\n'
          f'| User ID:   436427362414886912\n'
          f'| Owner:     Purple Human#5203\n'
          f'| Discord.PY Version: {discordpy} \n'
          f'| Brainstorm est 2018. First went live on: 30th April 2018...\n'
          f'# -------------------------------------------------------------#\n')
    bot.loop.create_task(status_task())




### STAFF COMMANDS ###

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Say goodbye to {}.".format(user.name))
    await bot.kick(user)
    print ("A user kicked someone.")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await bot.say("The ban hammer has struck on **{}**.".format(user.name))
    await bot.kick(user)
    print ("A user banned someone.")

@bot.command(pass_context=True)
async def settings(ctx):
    if ctx.message.author.id in owner:
        bot.gametimestatus = gametimestatus
        em = discord.Embed(title="Brainstorms Settings:", description="Toggle Gametime, gametime is a unique standout for Brainstorm and it is not found on other bots! By toggling this you can disable / enable gametime. To edit gametime please type **editgame**.")
        await bot.send_message(ctx.message.author, embed=em)
        answer = await bot.wait_for_message(timeout=3000)
        if answer is None:
            await bot.send_message(ctx.message.author, "You did not respond in time. The settings for gametime will stay as is.")
        if ctx.message.author and "editgame" not in answer.content.lower():
            await bot.send_message(ctx.message.author, "You did not respond correctly")
        if ctx.message.author and "editgame" in answer.content.lower():
            emb = discord.Embed(title="Gametimes Settings:", description="Gametime is currenly: **{}** (1 = ON, 0 = OFF), If you wish to disable it please type **Disable**, if you wish to enable it type **Enable**.".format(bot.gametimestatus))
            await bot.send_message(ctx.message.author, embed=emb)
        answer2 = await bot.wait_for_message(timeout=3000)
        if answer2 is None:
            await bot.send_message(ctx.message.author, "You did not respond in time. Gametime settings will stay as is.")
        if ctx.message.author and "Enable" not in answer.content.lower():
            bot.gametimestatus = "0"
            bot.remove_command('gametime')
            await bot.send_message(ctx.message.author, "Gametime has now been set to {}.".format(bot.gametimestatus))
        if ctx.message.author and "Enable" in answer.content.lower():
            bot.gametimestatus = "1"
            bot.add_command('gametime')
            await bot.send_message(ctx.message.author, "Gametime has now been set to {}.".format(bot.gametimestatus))
        await bot.send_message(ctx.message.author, "Gametime current status is now: {}.".format(bot.gametimestatus))

    

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await bot.add_roles(member, role)

@bot.event
async def on_server_join(server):
    bot.task
    server.name = await bot.change_presence(game=discord.Game(name="Brainstorm has joined {} | =help ✌️".format(server.name), type=1))

@bot.command(pass_context=True)
async def report(ctx, *, content):
    embed=discord.Embed(title="**{}** has reported someone!".format(ctx.message.author.name), description="{}".format(content), color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    server = bot.get_server("377702686377771008")
    await bot.send_message(server.get_channel("528432844117245973"), embed=embed)
    await bot.delete_message(ctx.message)

### BOT INFO & SERVER INFO ###

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Brainstorm", description="Brainstorm a Python Discord bot made by @Purple Human#5203. List of commands are:", color=0x00FFFF)
    embed.add_field(name="=help", value="Shows this command.", inline=False)
    embed.add_field(name="=8-ball", value="Do an 8ball to test your luck!", inline=False)
    embed.add_field(name="=gametime (@personname / names)", value="Ask people to play with you!", inline=False)
    embed.add_field(name="=ping", value="Play ping pong with Brainstorm.", inline=False)
    embed.add_field(name="=info @(someone)", value="Get info about someone.", inline=False)
    embed.add_field(name="=kick", value="Kick a member from the server (Requires the **Kick** permission.)", inline=False)
    embed.add_field(name="=ban", value="**BAN** a member from the server (Requires the **BAN** permission.)", inline=False)
    embed.add_field(name="=serverinfo", value="Get info about the server!", inline=False)
    embed.add_field(name="=link", value="Get the bot invite link.", inline=False)
    embed.add_field(name="=add", value="Add two numbers together just **put the one after the other**.", inline=False)
    embed.add_field(name="=minus", value="Minus two numbers from each other just like the last command.", inline=False)
    embed.add_field(name="=multiply", value="Times two numbers.. you get the deal.", inline=False)
    embed.add_field(name="=devide", value="Devide two numbers.. I'm sick of typing you get the deal!", inline=False)
    embed.add_field(name="=test", value="Test that the bot is working.", inline=False)
    embed.add_field(name="=hi", value="Say hi to Brainstorm!.", inline=False)
    embed.add_field(name="=about", value="Get backround info on Brainstorm.", inline=False)
    embed.add_field(name="=dice", value="Role a normal dice.", inline=False)
    embed.add_field(name="=dicem", value="Role a million sided dice. **wOw**", inline=False)
    embed.add_field(name="=say", value="Get the bot to say whatever you want. **30 SECOND COOLDOWN & REQUIRES CHANGE NICKNAME**", inline=False)
    embed.add_field(name="=announce", value="Announce anything you want just make sure it's in the channel you want. **REQUIRES ADMIN**", inline=False)
    embed.add_field(name="=gaytest", value="Take the gay test. :gay_pride_flag: **30 SEC COOLDOWN** ", inline=False)
    embed.add_field(name="=day", value="Ask Brainstorm how it's day has been.**30 SEC COOLDOWN**", inline=False)
    embed.add_field(name="=clear (1-100)", value="Clear messeges quickly! **REQUIRES ADMIN**", inline=False)
    await bot.send_message(ctx.message.author, embed=embed)
    await bot.delete_message(ctx.message)
    print ("A user got the bot command list.")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("This persons status is: {}".format(user.status))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.id))
    await bot.say("The users highest role on the server is: {}".format(user.top_role))
    await bot.say("The user has been here since: {}".format(user.joined_at))
    await bot.send_message(ctx.message.author)
    print ("A user got info on someone.")

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find about this server.", color=0x00FFFF)
    embed.set_author(name="Brainstorm")
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server Owner:", value=ctx.message.server.owner, inline=True)
    embed.add_field(name="Server ID:", value=ctx.message.server.id, inline=True)
    embed.add_field(name="The Server's Role Tally:", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server Members! :heart:  ", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.author, embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def link():
  	await bot.say("OwO <3, http://tiny.cc/3ue51y")

### CALCULATOR ###

@bot.command(pass_context=True)
async def add(ctx, a: int, b:int):
    await bot.say(a+b)

@bot.command(pass_context=True)
async def multiply(ctx, a: int, b:int):
    await bot.say(a*b)

@bot.command(pass_context=True)
async def divide(ctx, a: int, b:int):
    await bot.say(a/b)

@bot.command(pass_context=True)
async def minus(ctx, a: int, b:int):
    await bot.say(a-b)

@bot.command(pass_context=True)
async def quickmaths(ctx):
    await bot.say("2 + 2 = 4 - 1 thats 3 **QUICK MATHS**")

### GAME COMMANDS ###

@bot.command(pass_context=True)
async def bruh(ctx):
    embed = discord.Embed(description="b̴̧̹͓̜͇̱̜̗̼̃͜r̴͍̺̟͑͑̕u̸̺͛̑̆̀̋̀͗̐̈́͝h̷̝̟̲͚͚͉͎̓̐̎̈́̓̌ͅ")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def test(ctx):
    embed = discord.Embed(description="Wait what are we testing again? Sorry I forgot. :sweat_smile: ")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(description="Hi, I was made on the 30th of April 2018 but originally I was designed in September of 2017. My maker and coder for Brainstorm is @Purple Human#5203 he is a programmer that with the help of friends learnt to code in Python. Thats it if you want more info on the bot just go =aboutmore", color=0x00FFFF)
    await bot.say(embed=embed)

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no. ',
        'It is not looking likely. ',
        'Too hard to tell :thinking:. ',
        'It is quite possible. ',
        'Definitely ',
        'I come back to you later.. ',
        'NO!! ',
        'YES!! ',
        'Maybe? My IQ isnt up to date so I cant give you a 100% certin yes or no. ',
        'You wish. ',
        'Go ask a real person. ',
        'You know the answer. ',
        'Thats a yes. ',
        'возможно! ',
        'вы потратили на длительный перевод. ',
        'Yes. ',
        'No. ',
        'Why are you even trying? ',
        'What do you think? ',
        'Maybe. ',
        'Never. ',
        'Yep. ',

    ]
    embed=discord.Embed(title="{} the 8-ball says..".format(context.message.author.name), description="{}".format(random.choice(possible_responses)), color=0x00FFFF)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/2000px-8-Ball_Pool.svg.png")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def aboutmore(ctx):
    embed = discord.Embed(description="Purple Human: I started work on the bot a while back as a concept. Not knowing how to code in python I grabbed a random source code for a bot from the web. That was the first version of 'Brainstorm' but I instantly ditched the idea. Later on, I got discord bot maker, this is where I really started to get into the bot adding it basic chat and game commands. These all moved over to the python version when I wanted to start trying to code python. Version 0.1 of brainstorm featured one command and it took me 4 days to figure out how to make the =helpme command. That's the basic history of the bot, commands and update logs are unavailable and sadly I cannot give a timeline of what commands released when. Anyways thanks for reading I hope you enjoy brainstorm - Purple Human#5203")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def botverson(ctx):
    await bot.say("My current state is {} I'm set for full open source and server adoption during the end of 2018.".format(verson))

@bot.command(pass_context=True)
async def dice(ctx):
    await bot.say("You rolled the number {}! 🎲".format(random.randint(0, 6)))

@bot.command(pass_context=True)
async def dicem(ctx):
    await bot.say("You rolled the magic millions dice and got the number {}! **w0w** 🎲".format(random.randint(0, 1000000)))

@bot.command(pass_context=True)
@commands.cooldown(1, 45, commands.BucketType.user)
async def gaytest(ctx):
    percent = random.randint(10, 10000)/100
    if percent <= 10:
        displaypercent = "█ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​║"
    if percent >= 20:
        displaypercent = "██​ ​ ​ ​ ​ ​ ​ ​ ​ ​║"
    if percent >= 30:
        displaypercent = "██​█​​ ​ ​ ​ ​ ​ ​ ​ ​║"
    if percent >= 40:
        displaypercent = "██​█​█​ ​ ​ ​ ​ ​ ​ ​║"
    if percent >= 50:
        displaypercent = "██​█​█​█​ ​ ​ ​ ​ ​ ​║"
    if percent >= 60:
        displaypercent = "██​​█​█​█​█​​ ​ ​ ​ ​ ​║"
    if percent >= 70:
        displaypercent = "██​█​█​█​█​█​█​​ ​ ​ ​║"
    if percent >= 80:
        displaypercent = "██​█​█​█​█​█​█​█​​​ ​ ​║"
    if percent >= 90:
        displaypercent = "██​█​█​█​█​█​█​█​█​ ​║"
    if percent >= 100:
        displaypercent = "██​█​█​█​█​█​█​█​█​█​​║"
    embed=discord.Embed(title="{} has taken the gay test! 🏳️‍🌈".format(ctx.message.author.name), description="The test says that **they are {} {}% gay! 😁**".format(displaypercent, percent), color=0x00FFFF)
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True, hidden=True)
async def gaytestowner(ctx):
    if ctx.message.author.id in owner:
        embed=discord.Embed(title="The great leader {} has taken the gay test! 🏳️‍🌈".format(ctx.message.author.name), description="The test says that **they are {}% gay! 😓**".format(random.randint(10, 100000000)/100), color=0x00FFFF)
        await bot.say(embed=embed)
    if ctx.message.author.id not in owner:
        await bot.send("This command is only for the ѕυρяємє leader. :)")

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def day(ctx):
    possible_responses = [
        'Really bad. ',
        'Not the best, ',
        'The day has not ended so I can not tell you yet. ',
        'Really good! Thanks for asking <3, ',
        'Good good, how has yours been? ',
        'So so. ',
        'The worst day ever, ',
        'The best!! ',
        'I loved today, ',
        'I worked on making commands, so great! ',
        'I have not had a good day today.. ',
        'My day has been great! ',
        'Today. Has. Been. The. Worst! ',
        'Really great! ',

    ]
    await bot.say(random.choice(possible_responses) + ctx.message.author.name)

@bot.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def funfact(ctx):
    possible_responses = [
        'Cows have diffrent accents for their specfic area. So cows in australia sound diffrent to ones down in *africa*!',
        'Hunting unicorns is legal in Michigan.',
        'There is a technical name for the fear of long words. Hippopotomonstrosesquippedaliophobia.',
        'The sound of E.T walking was made with jelly?!',
        'A group of frogs is called a army!',
        'The statue of libery wears a size 876 sandal.',
        'In 1859, 24 rabbits were released in Australia, 6 year later there were 2 Million.',
        'An average tree produces 8333 sheets of paper.',
        'Cola would be green if coloring wasnt added.',
        'A bolt of lightning has enough energy to toast 160,000 peices of bread.',
        'Zenith used to be called The Hub and featured Bart Simpson as the server icon.',
        'Shrek used to be a romantic action skit that played at local german pubs during 1638.',
        'I have run out of facts.. come back to me later.',
        'A 4 year old asks around 400 questions per day! Wait make that 401.. ',
        'Pepsi was orginally called Brads Drink.',
        'The lolipop was named after a horse.',

    ]
    embed=discord.Embed(title="Brainstorm has chosen a fun fact:", description="{}".format(random.choice(possible_responses)), color=0x00FFFF)
    embed.set_thumbnail(url="https://i.imgur.com/14COhR2.png")
    await bot.say(embed=embed)


### POLL AND TEXT COMMANDS ###

@bot.command(pass_context=True)
@commands.has_permissions(change_nickname=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def say(ctx, *, content):
    embed=discord.Embed(title="**{}** has asked brainstorm to say: ".format(ctx.message.author.name), description="{} ".format(content), color=0x00FFFF)
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def announce(ctx, *, content):
    embed=discord.Embed(title="**{}** has announced! :globe_with_meridians: ".format(ctx.message.author.name), description="@everyone, {}".format(content), color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)   
async def news(ctx):
    embed=discord.Embed(title="Brainstorm News Command 3000!", description="The news command is a Brainstorm exclusive, one of a kind command. It features a updating embedded news tab for all members to view and read. With updating articles and photo's.", color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    embed.set_footer(text="The next two responces will show how the Title and Description look. ❗ Title first then Description please respond with what you would like in the embed ❗ )")
    await bot.send_message(ctx.message.author, embed=embed)
    await bot.delete_message(ctx.message)
    answer = await bot.wait_for_message(timeout=60)
    reply1 = answer.content
    embed2=discord.Embed(title=reply1, color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    message_object=await bot.send_message(ctx.message.author, embed=embed)
    await bot.edit_message(message=message_object, embed=embed2)
    answer = await bot.wait_for_message(timeout=60)
    reply2 = answer.content
    embed2=discord.Embed(title=reply1, description=reply2, color=0x00FFFF, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.message.author)
    message_object=await bot.send_message(ctx.message.author, embed=embed)
    await bot.edit_message(message=message_object, embed=embed2)
    await bot.send_message(ctx.message.author, "Would you like this to be your message? (Respond with 'Yes' to accept or 'No' to restart!)")
    answer = await bot.wait_for_message(timeout=25)
    reply3 = answer.content
    if ctx.message.author and "Yes" in reply3:
        await bot.send_message(ctx.message.author, "The embed has been sent to the original channel! ✅")
        await bot.send_message(ctx.message.channel, embed=embed2)
    if ctx.message.author and "No" in reply3:
        await bot.send_message(ctx.message.author, "Please wait one minute and type =news to try again. 👍 ")                     


### LOOPS & SCHEDULED TASKS ###

async def status_task():
    while True:
            await bot.change_presence(game=discord.Game(name="Follow my Twitch | =help ✌️", url="https://www.twitch.tv/purplehumanlive", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="with {}, it's now LIVE! | =help ✌️".format(verson), type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Half Life 3 | =help ✌️", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="all alone | =help ✌️", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="nothing at all. | =helpme ✌️", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Africa by Toto. | =help ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="with no-one.. | @{}".format(ownername), type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Monsters Inc | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Feel the Way I Do by The Jungle Giants | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="MEME 👏 REVIEW 👏 | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="You.. :) | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="The Clouds Outside | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="grass growing. | =help ✌️", url="https://www.twitch.tv/purplehumanlive", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Mine Diamonds | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Minun Man :) | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="chief tell me, that aint it. | =help ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Despacito by Luis Fonsi | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="to the sound of crows. | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="Quirk by Flume | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="the world burn. | =helpme ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="everything you do... | =helpme ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="to everything you say. | =helpme ✌️", type=2))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="all your data to Facebook. | =help ✌️", url="https://www.twitch.tv/purplehumanlive", type=1))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="you stare at me. | =helpme ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="time go by. | =helpme ✌️", type=3))
            await asyncio.sleep(15)
            await bot.change_presence(game=discord.Game(name="some bangers! | =helpme ✌️", type=2))
            await asyncio.sleep(15)

### TEST COMMANDS ###


### TEST COMMANDS ###

bot.run(TOKEN)
