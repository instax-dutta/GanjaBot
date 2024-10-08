import discord
from discord.ext import commands, tasks
import random
import datetime
import asyncio


intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Define a list of statuses with only 'listening' and 'watching' activities
statuses = [
    discord.Activity(type=discord.ActivityType.listening, name="Charas Ganja"),
    discord.Activity(type=discord.ActivityType.listening, name="Daru Badnam"),
    discord.Activity(type=discord.ActivityType.listening, name="RACEROP"),
    discord.Activity(type=discord.ActivityType.watching, name="My Bar"),
    discord.Activity(type=discord.ActivityType.watching, name="My Weed Factory")
]

# Function to rotate the status
@tasks.loop(seconds=20)
async def change_status():
    for status in statuses:
        await bot.change_presence(activity=status)
        await asyncio.sleep(20)

import datetime
import random

# Dictionary mapping user IDs to their specific message arrays
user_messages = {
    '885008600135770122': [
        "{mentioned_users}, lagta hai maal aagaya hai! {user} ne VC mein entry maari!",
        "{mentioned_users}, bhai, sambhal jao! {user} apna maal lekar aaya hai!",
        "{mentioned_users}, ab nashe ka waqt shuru! {user} VC mein ghus chuka hai!",
        "{mentioned_users}, chakna tayyar rakhna! {user} VC mein dhamaal machane aa gaya hai!",
        "{mentioned_users}, ab gyaan ka silsila shuru hoga! {user} VC mein padhare hain!",
        "{mentioned_users}, maal ka asli rakhwala {user} ab VC mein hai!",
        "{mentioned_users}, apna nashe ka dose {user} lekar aa gaya hai VC mein!",
        "{mentioned_users}, chakna aur maal ki delivery {user} ne kar di hai VC mein!",
        "{mentioned_users}, gyaan aur nashe ka combo lekar {user} VC mein aa gaya!",
        "{mentioned_users}, maal, chakna aur nashe ki tridev {user} VC mein upastith hai!"
    ],
    '786451968469368853': [
        "{mentioned_users}, bhoolna mat, {user} maal ka boss hai, aur ab VC mein hai!",
        "{mentioned_users}, apna chakna sambhal lo, {user} VC mein ghus chuka hai!",
        "{mentioned_users}, nashe ki lehar lekar {user} aa gaya hai VC mein!",
        "{mentioned_users}, maal aur chakna ka asli source {user} VC mein hai!",
        "{mentioned_users}, gyaan ki kahani shuru hoti hai ab {user} ke saath VC mein!",
        "{mentioned_users}, maal ka asli maalik {user} VC mein padhare hain!",
        "{mentioned_users}, chakna aur nashe ka boss {user} VC mein aa gaya hai!",
        "{mentioned_users}, ab sab dhyan se suno! {user} gyaan dene aaya hai VC mein!",
        "{mentioned_users}, maal, chakna aur gyaan ka triple combo lekar {user} VC mein aa gaya!",
        "{mentioned_users}, sab milke swagat karo! {user} apne maal ke saath VC mein aa gaya!"
    ],
    '742076828721610815': [
        "{mentioned_users}, maal ka naya stock lekar {user} VC mein ghus gaya hai!",
        "{mentioned_users}, apne chakna ko taiyaar rakho! {user} VC mein aa gaya hai!",
        "{mentioned_users}, nashe ka asli maza ab {user} ke saath hoga VC mein!",
        "{mentioned_users}, maal aur chakna lekar {user} VC mein pravesh kar chuka hai!",
        "{mentioned_users}, gyaan aur nashe ka combo lekar {user} VC mein padhare hain!",
        "{mentioned_users}, chakna, maal aur nashe ka asli theka {user} VC mein leke aaya hai!",
        "{mentioned_users}, apna chakna sambhal lo, {user} VC mein aaya hai nashe ke liye!",
        "{mentioned_users}, maal ka asli thekedar {user} VC mein aa chuka hai!",
        "{mentioned_users}, nashe ki raat shuru hoti hai {user} ke saath VC mein!",
        "{mentioned_users}, chakna aur gyaan ka combo lekar {user} VC mein aa gaya!"
    ]
}

CHANNEL_ID = 1053665970264219680 # Replace with your text channel ID
VC_ID = 1080539142804475984  # Replace with your voice channel ID

# Dictionary to store the last time a message was sent for each user
last_message_time = {}

# Dictionary to store message timestamps within the last 24 hours for each user
message_timestamps = {}

# Cooldown period in seconds (1 hour = 3600 seconds)
COOLDOWN_PERIOD = 3600

# Limit of messages per user per 24 hours
DAILY_MESSAGE_LIMIT = 8
TIME_WINDOW = 86400  # 24 hours in seconds

# List of masculine and feminine Ganja and Nashedi-themed nicknames
male_nicknames = [
    "Maal Ka Baadshah", "Nashe Ka Sardar", "Chillam King", "Weed Baba",
    "Hukkah Hero", "Trippy Tantrik", "Charsi Chela", "Nashedi Raja", 
    "Ganja Guru", "Bhaang Ke Maharaj", "Rolling Rishi", "Highness",
    "Blunt Bhai", "Chillum Chacha", "Stoned Saint", "Bhangra Boss",
    "Moksha Master", "Cannabis Captain", "Trip King", "Dank Dealer",
    "Smokey Sadhu", "Weed Wizard", "Herb Hero", "Joint Joker",
    "Puff Daddy", "High Maharaj", "Sativa Sultan", "Kush Kaptain",
    "Bhaang Baba", "Ganja Gandharva", "Nasha Nayak", "Hash Hunk",
    "Blaze Bhai", "Grass Guru", "Stoned Shikari", "Moksha Mama"
]

female_nicknames = [
    "Weed Wali Amma", "Mary Jane Maharani", "Rolling Rani", "Chillum Chachi",
    "Highness Queen", "Cannabis Rani", "Bhaang Ki Rani", "Ganja Ki Devi",
    "Trippy Tripti", "Charsi Chudail", "Blunt Babe", "Stoned Sundari",
    "Nashili Nisha", "Tripti Tantrika", "Moksha Maharani", "Ganja Gudiya",
    "Weed Wali", "Blaze Bhabhi", "Kush Kumari", "Herb Hottie",
    "Sativa Sultana", "Puff Princess", "Chillam Chudi", "Nashe Wali",
    "Dank Devi", "Moksha Mahi", "Hash Heer", "Ganja Gudiya", 
    "Stoned Shakti", "High Hazira", "Nasha Nandini", "Ganja GuruMa"
]

# Dictionary to keep track of when users were last assigned a nickname
nickname_history = {}

# Time limit between nickname changes (in seconds)
NICKNAME_COOLDOWN = 1800  # 30mins

FEMALE_ROLE_NAME = "female"  # Replace with your role name for female users

@bot.event
async def on_voice_state_update(member, before, after):
    # Debug print to see if the event is being triggered
    print(f"Voice state update detected for {member.name} ({member.id})")
    print(f"Before Channel: {before.channel}, After Channel: {after.channel}")
    
    # Check if the member just joined the monitored voice channel
    if before.channel is None and after.channel and after.channel.id == VC_ID:
        print(f"{member.name} joined the monitored voice channel: {after.channel.name}")
        
        # Convert member.id to string to match dictionary keys
        member_id_str = str(member.id)
        
        current_time = datetime.datetime.now()
        
        # Message sending logic
        if member_id_str in user_messages:
            # Check if the user is in the cooldown period
            if member_id_str in last_message_time:
                last_sent_time = last_message_time[member_id_str]
                time_since_last_message = (current_time - last_sent_time).total_seconds()
                
                if time_since_last_message < COOLDOWN_PERIOD:
                    print(f"Cooldown active for {member.name}. Last message sent {time_since_last_message} seconds ago.")
                    return  # Exit the function if still in cooldown period
            
            # Initialize the message timestamps list if not already done
            if member_id_str not in message_timestamps:
                message_timestamps[member_id_str] = []
            
            # Filter out messages that are older than 24 hours
            message_timestamps[member_id_str] = [
                timestamp for timestamp in message_timestamps[member_id_str]
                if (current_time - timestamp).total_seconds() <= TIME_WINDOW
            ]
            
            # Check if the user has reached the daily message limit
            if len(message_timestamps[member_id_str]) >= DAILY_MESSAGE_LIMIT:
                print(f"Daily message limit reached for {member.name}.")
                return  # Exit the function if the daily limit has been reached
            
            # Update the last message time and add the current time to the timestamps list
            last_message_time[member_id_str] = current_time
            message_timestamps[member_id_str].append(current_time)
            
            channel = bot.get_channel(CHANNEL_ID)
            print(f"Text channel identified: {channel.name}")
            
            # Get the list of members already in the voice channel, excluding the joining member
            vc_members = [m for m in after.channel.members if m.id != member.id]
            print(f"VC Members (excluding {member.name}): {[m.name for m in vc_members]}")
            
            mentioned_users = ', '.join([f"<@{m.id}>" for m in vc_members])

            # Handle the case where no one was in the VC before the specified user joined
            if not mentioned_users:
                mentioned_users = "Koi bhi nahi tha"
                print("No members were present in the VC before this user joined.")
            
            # Select a random message from the specified user's message array
            message = random.choice(user_messages[member_id_str])
            print(f"Selected message: {message}")

            # Format the message with the mentioned users and the joining user
            formatted_message = message.format(mentioned_users=mentioned_users, user=f"<@{member.id}>")
            print(f"Formatted message: {formatted_message}")
            
            # Send the message to the specified text channel
            await channel.send(formatted_message)
            print("Message sent to the text channel.")

        else:
            print(f"No custom messages found for {member.name} ({member.id}).")

        # Nickname changing logic
        # Check if the user is in the cooldown period for nickname changes
        if member_id_str in nickname_history:
            last_change_time = nickname_history[member_id_str]
            time_since_last_change = (current_time - last_change_time).total_seconds()
            if time_since_last_change < NICKNAME_COOLDOWN:
                print(f"Nickname change on cooldown for {member.name}.")
                return  # Skip nickname change
        
        # Determine if the user has the "female" role
        has_female_role = any(role.name == FEMALE_ROLE_NAME for role in member.roles)
        
        # Choose a random nickname based on the user's gender
        if has_female_role:
            chosen_nickname = random.choice(female_nicknames)
        else:
            chosen_nickname = random.choice(male_nicknames)
        
        # Update the user's nickname
        try:
            await member.edit(nick=chosen_nickname)
            print(f"Changed nickname of {member.name} to {chosen_nickname}")
            
            # Record the time of this nickname change
            nickname_history[member_id_str] = current_time
        except Exception as e:
            print(f"Failed to change nickname of {member.name}: {e}")

        # Shuffle the appropriate nickname list to avoid frequent repetition
        if has_female_role:
            random.shuffle(female_nicknames)
        else:
            random.shuffle(male_nicknames)
    else:
        print(f"{member.name} didn't join the monitored voice channel or left it.")

@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user} is online and ready to roll!')

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

bot.run('bot_token')
