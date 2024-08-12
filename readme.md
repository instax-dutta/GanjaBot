# Ganja Bot

Ganja Bot is a fun Discord bot that responds with hilarious and Indian-themed messages when specific users join a voice channel. It also includes some playful commands to entertain your friends.

## Features

- **Custom Messages**: Sends messages in a specified text channel when specific users join a common voice channel.
  - **Rate Limiting**: Messages are sent only once per hour per monitored user to prevent flooding. Each user is limited to 8 messages per 24 hours.
- **Gender-Based Nickname Assignment**: Automatically changes the nickname of users who join the specified voice channel to a Ganja and Nashedi-themed nickname based on their gender. Users with the "female" role are assigned feminine nicknames, while others receive masculine ones.
- **Fun Commands**:
  - `!chakna`: Suggests different types of snacks.
  - `!nashe`: Shares funny trip-related thoughts.
  - `!gyan`: Provides some stoner wisdom.
  - `!maal`: Displays items related to the stoner experience.
  - `!roll`: Rolls a random number between 1 and 100.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/instax-dutta/GanjaBot.git
   cd GanjaBot
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Bot**:
   - Replace `YOUR_BOT_TOKEN` in `main.py` with your Discord bot token.
   - Replace `CHANNEL_ID` and `VC_ID` with the IDs of your text and voice channels.
   - Set `FEMALE_ROLE_NAME` to the name of the role used to identify female users on your server.

4. **Run the Bot**:

   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- `discord.py` library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
