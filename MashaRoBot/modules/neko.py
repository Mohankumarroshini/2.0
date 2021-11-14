import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import MashaRoBot.modules.nekostrings as nekostrings
from MashaRoBot import dispatcher
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from MashaRoBot.modules.helper_funcs.chat_status import (is_user_admin)
from MashaRoBot.modules.helper_funcs.extraction import extract_user



@run_async
def nyaa(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        neko_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    nyaa_type = random.choice(("Text", "Gif"))
    if nyaa_type == "Gif":
        try:
            temp = random.choice(nekostrings.NEKO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Gif"

    if nyaa_type == "Gif":
        temp = random.choice(nekostrings.NEKO_GIFS)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)




@run_async
def meow(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        meow_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    meow_type = random.choice(("Text", "Gif"))
    if meow_type == "Gif":
        try:
            temp = random.choice(nekostrings.CATTO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Gif"

    if meow_type == "Gif":
        temp = random.choice(nekostrings.CATTO_GIFS)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

__help__ = """
 • `/nyaa`*:* Use this to get cute Anime Neko Gifs!
 • `/meow`*:* Use this to get cute Real Cat Gifs!
"""


NYAA_HANDLER = DisableAbleCommandHandler("nyaa", nyaa)
MEOW_HANDLER = DisableAbleCommandHandler("meow", meow)


dispatcher.add_handler(NYAA_HANDLER)
dispatcher.add_handler(MEOW_HANDLER)

__mod_name__ = "ɴᴇᴋᴏ🐾"

__command_list__ = [
       "nyaa", "meow"
]
__handlers__ = [
       NYAA_HANDLER, MEOW_HANDLER
]
