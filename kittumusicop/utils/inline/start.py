from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["✯ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩ ʙᴀʙy ✯"], url=f"https://t.me/Kittu_music_robot?startgroup=true"
            ),
            InlineKeyboardButton(text=_["✯ Owner ✯"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(
                text=_["✯ More ✯"], url=f"https://t.me/qts_dp"
            ),
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["✯ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩ ʙᴀʙy ✯"],
                url=f"https://t.me/Kittu_music_robot?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["Help"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["Owber"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["More"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["information"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["information"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
