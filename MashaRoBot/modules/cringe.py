import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import MashaRoBot.modules.cringe_strings as animequotes_strings
from MashaRoBot import dispatcher
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from MashaRoBot.modules.helper_funcs.chat_status import (is_user_admin)
from MashaRoBot.modules.helper_funcs.extraction import extract_user

@run_async
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animequote_strings.QUOTES_IMG))

__help__ = """
 • `/cringe`*:* gives random cringe strickers
 
"""
ANIMEQUOTE_HANDLER = DisableAbleCommandHandler("cringe", animequotes)

dispatcher.add_handler(ANIMEQUOTE_HANDLER)

__mod_name__ = "ᴄʀɪɴɢᴇ🦋"
__command_list__ = [
    "cringe"
]
__handlers__ = [
    ANIMEQUOTE_HANDLER
]
