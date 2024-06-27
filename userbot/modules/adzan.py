import json
import requests
from pyrogram import *
from pyrogram.types import *
from userbot.core.helpers.basic import edit_or_reply
from userbot import *

__MODULE__ = "ᴀᴅᴢᴀɴ"
__HELP__ = f"""
<b>『 bantuan untuk ᴀᴅᴢᴀɴ 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}adzan</code> [nama kota]
  <b>• penjelasan:</b> Untuk mengetahui waktu adzan.
 
"""

@CB.UBOT("adzan", sudo=False)
async def adzan(client, message):
    lok = message.text.split(" ", 1)
    if len(lok) == 1:
        await edit_or_reply(message, "`Mohon sertakan nama kota.`")
        return
    lok = lok[1]
    url = f"http://muslimsalat.com/{lok}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        await edit_or_reply(message, f"Error: {e}")
        return
    result = req.json()
    txt = f"""
**Jadwal Shalat Wilayah <u>{lok}</u>
Tanggal `{result['items'][0]['date_for']}`
Kota `{result['query']} | {result['country']}`

Terbit : `{result['items'][0]['shurooq']}`
Subuh : `{result['items'][0]['fajr']}`
Zuhur :`{result['items'][0]['dhuhr']}`
Ashar : `{result['items'][0]['asr']}`
Maghrib : `{result['items'][0]['maghrib']}`
Isya : `{result['items'][0]['isha']}`**
"""
    await edit_or_reply(message, txt)
