from userbot import *


__MODULE__ = "ɪᴘɪɴꜰᴏ"
__HELP__ = f"""
<b>『 bantuan untuk ipinfo 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ipinfo</code> [ip addreꜱ]
  <b>• penjelasan:</b> untuk mendapatkan informasi ip addres 
  """


@CB.UBOT("ipinfo", sudo=False)
async def _(client, message):
    await hacker_lacak_target(client, message)