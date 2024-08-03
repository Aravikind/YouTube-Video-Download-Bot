# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config._NP2NuJve6Y, 
    api_hash=Config.c4aa993ab2b05f8e93c81d45e2d501c1, 
    bot_token=Config.7488694258:AAGk3o_k6SNCW44xdkUf4aA5FGvqC1N9X-0,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
