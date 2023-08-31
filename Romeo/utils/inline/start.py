from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Romeo import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/Classics002"),
            InlineKeyboardButton(
                text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 📡", url=f"https://t.me/Classics0012"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/Classics002"),
            InlineKeyboardButton(
                text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 📡", url=f"https://t.me/Classics0012"
            )
        ],
     ]
    return buttons
