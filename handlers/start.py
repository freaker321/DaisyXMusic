# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
<i>I am a Group Music Play Bot!</i>  
<i>I am specially designed for voice chats in groups.</i>
Press /help for detailed instructions about using me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ BOT OWNER", url="https://t.me/xmysteriousx"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "JOIN OUR GROUP", url="https://t.me/Rezoth_tm"
                    ),
                    InlineKeyboardButton(
                        "JOIN OUR CHANNEL", url="https://t.me/Rezoth"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        """<b>How to use me:-</b>
💠 First you should add me <i>(@Mystry_Music_Player_bot)</i> to your group and give me admin permissions.
        
💠 Then you should add my assistant music player account - <i>@Mystry_Music_Player to your groups.</i>
(This account will play music in your groups.)
         
💠Then start a voice chat in your group.
💠Then send a youtube link and reply /play to it.
<i>(You can press /yts to search songs and after sending the link to the group you can reply /play to it.)</i>
💠 If you want to play an audio file send the audio to the group and reply /play to it.
<b>Note</b> :- Queue option has been fixed.
Use /skip for move to the next song.
Use /end for ending the stream.
        
<b>Important rules you should follow.</b>
        
1. You can play youtube links and audio files using me.
2. Do not send song links longer than 10 minutes.
3. Do not send youtube playlists.
That's it.
Hope you enjoy me.🙂
<b><i>Created with ❤️ by @xmysteriousx</i></b>"""
    )
    
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/rezoth_tm")
                ]
            ]
        )
   )

