import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1053665970264219680 # Replace with your text channel ID
VC_ID = 1080539142804475984  # Replace with your voice channel ID

member_messages = {
    742076828721610815: [
        "Yo! Aagaya yeh banda, chalo roll karte hain aur chill karte hain!",
        "Koi epic gyaan dene wala aagaya hai. 🌿",
        "Bong le lo, party shuru hone wali hai!",
        "Ek blunt roz, bad vibes ko door bhaga do. 🍁",
        "Roll karne ke liye taiyaar? Master aagaya hai!",
        "Fat one pack karo; abhi time hai lit hone ka! 🔥"
    ],
    885008600135770122: [
        "Arey nahi, yeh phir se! Stash chhupa lo! 😱",
        "Unexpected cheezon ke liye prepare ho jao; yeh banda style mein aata hai!",
        "Papers pass karo, roll karne ka time hai!",
        "Joint roller aagaya. Ready ho jao! 💨",
        "Jaldi se spark karo, warna yeh le lega sab kuch! 😎",
        "Roll up aur chill karo, session ab aur bhi accha ho gaya."
    ],
    786451968469368853: [
        "Party ab shuru hui! Lighter kis ke paas hai? 🔥",
        "Clouds se bhi upar chalte hain! ☁️",
        "Good vibes rollin', boss ki taraf se!",
        "Lit hone ka time hai! Real G aagaya. 🍁",
        "Moon pe trip ke liye taiyaar? Yeh joint tumhare liye hai! 🚀",
        "Spark karo, hum ek journey par nikalne wale hain!"
    ],
}


@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready to roll!')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == VC_ID and before.channel != after.channel:
        if member.id in member_messages:
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                await channel.send(f"{member.mention} {random.choice(member_messages[member.id])}")

@bot.command(name="chakna")
async def chakna(ctx):
    snacks = [
        "🍕 Pizza aane wali hai!",
        "🍪 Cookies, koi?",
        "🍿 Popcorn high times ke liye.",
        "🍫 Chocolate – ultimate chakna!",
        "🍔 Burgers – kyun nahi?",
        "🍟 Fries bhi honi chahiye."
    ]
    await ctx.send(f"Chakna? {random.choice(snacks)}")

@bot.command(name="nashe")
async def nashe(ctx):
    trip_thoughts = [
        "Kya agar universe ek bada joint hai jo abhi tak spark nahi hua? 🌌",
        "Reality ek high hai jisse hum kabhi utarte nahi? 🤔",
        "Kya hum sab sirf stardust hain jo roll kar rahe hain? ✨",
        "Jaise jaise tum high hote ho, tum zyada dekhte ho. Tum kya dekh rahe ho? 👁️",
        "Reality ek illusion hai jo weed ki kami se create hota hai. 😜",
        "Kya hum bas kisi aur ke psychedelic sapne ke characters hain? 💭"
    ]
    await ctx.send(random.choice(trip_thoughts))

@bot.command(name="gyan")
async def gyan(ctx):
    wisdom_quotes = [
        "Ek blunt roz, stress door ho jata hai.",
        "Shant raho aur roll karte raho.",
        "High spirits, higher thoughts.",
        "Jaise jaise tum high hote ho, tum zyada dekhte ho.",
        "Smoke 'em if you got 'em."
    ]
    await ctx.send(random.choice(wisdom_quotes))

@bot.command(name="maal")
async def maal(ctx):
    stash_items = [
        "🍁 Sabse fresh bag of greens.",
        "💨 Ek pre-rolled joint, sirf tumhare liye.",
        "🚬 Classic cigarette purani yaadon ke liye.",
        "🍄 Magic mushrooms ka ek haath... adventurous ke liye.",
        "🔥 Ek lighter – kyunki tumhe zaroorat padegi.",
        "🌿 Herbal delights ka ek bouquet."
    ]
    await ctx.send(f"Ganja Bot apni maal ko kholta hai aur paata hai: {random.choice(stash_items)}")

@bot.command(name="roll")
async def roll(ctx):
    number = random.randint(1, 100)
    await ctx.send(f"🎲 Ganja Bot ne {number} roll kiya! Isse beat karo!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Arre! Kuch gadbad ho gaya: {str(error)}")
    print(f"Error: {str(error)}")

bot.run('BOT_TOKEN')
