import discord
from discord.ext import commands
import random

# Initialize bot with command prefix
bot = commands.Bot(command_prefix="!")

# Dictionary of modifier scores
modifier_values = {
    "P5": 5,
    "USA": 1,
    "Five Eyes": 1,
    "Israel in MENA": 5,
    "Germany in Europe": 3,
    "Russia in Eastern Europe, Central Asia, Caucuses": 2,
    "Brazil in SA": 2,
    "Cuba in LA and USA": 4,
    "DPRK in ROK and Japan": 5,
    "ROK in DPRK": 5,
    "PRC in SEA": 2,
    "Taiwan in PRC": 5,
    "Japan in East Asia": 4,
    "Pakistan in the Subcontinent": 5,
    "India in the Subcontinent": 3,
    "Iran in MENA": 3,
    "Saudi Arabia in MENA": 3,
    "Qatar in MENA": 2,
    "UAE in MENA": 2,
    "South Africa in Sub-Saharan Africa": 3,
    "Cell established": 5,
    "Disco-roll in own country": 3
}

def calculate_modifier_score(modifiers):
    total_score = 0
    for modifier in modifiers:
        if modifier in modifier_values:
            total_score += modifier_values[modifier]
    return total_score

def calculate_total_score(modifier_score):
    random_number = random.randint(0, 100)
    total_score = (random_number / 2) + 50 * (modifier_score / 10)
    return total_score

def determine_result(total_score):
    if total_score <= 30:
        return "Mission objective failed, secrecy not maintained"
    elif total_score <= 50:
        return "Mission objective failed, secrecy maintained"
    elif total_score <= 80:
        return "Mission objective successful, secrecy not maintained"
    elif total_score <= 100:
        return "Mission objective successful, secrecy maintained"
    else:
        return "Mission objective successful, secrecy maintained, and bonuses"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def submit(ctx, claim, target, operation_type, *modifiers):
    modifier_list = list(modifiers)
    modifier_score = calculate_modifier_score(modifier_list)
    total_score = calculate_total_score(modifier_score)
    result = determine_result(total_score)

    # Send result back to the user
    embed = discord.Embed(title="Operation Result", color=0x00ff00)
    embed.add_field(name="Claim", value=claim, inline=False)
    embed.add_field(name="Target", value=target, inline=False)
    embed.add_field(name="Type of Operation", value=operation_type, inline=False)
    embed.add_field(name="Modifiers", value=', '.join(modifier_list), inline=False)
    embed.add_field(name="Result", value=result, inline=False)
    await ctx.send(embed=embed)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTI0Nzg3NjI3NTQ5NDg1MDY4NA.GPvSxm.BZNudoTYTaASNAGfe0vqfuM12XnAhMnYR5DATg')
