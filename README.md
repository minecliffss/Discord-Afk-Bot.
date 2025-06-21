## Auto AFK Voice Bot
A simple Discord bot that monitors voice channels and automatically moves self-muted users to an AFK channel after a specified timeout.

# 💡 Features
Detects users who mute themselves while in a voice channel.
Moves muted users to a designated AFK voice channel after 60 seconds.
Ignores bots.
Lightweight and uses discord.py.

# 🛠️ Setup
1. Clone the Repository
git clone https://github.com/your-username/auto-afk-voice-bot.git
cd auto-afk-voice-bot
2. Install Requirements
Make sure you have Python 3.8+ installed.

pip install discord.py
3. Configure the Bot
Replace 'TOKEN' in bot.run('TOKEN') with your actual Discord bot token.

Also make sure your AFK voice channel is named exactly as specified:

┊🇦🇫🇰
Or change the AFK_CHANNEL_NAME variable in the code to match your server’s AFK channel name.

4. Run the Bot
python bot.py

# 📄 Code Overview
AFK_CHANNEL_NAME = "┊🇦🇫🇰"
MUTE_TIMEOUT_SECONDS = 60
The bot listens for on_voice_state_update.

If a member self-mutes, the bot waits 60 seconds.

If they remain muted in the same channel, it moves them to the AFK channel.
