
from telethon import TelegramClient, events
import asyncio   # <-- bunu da ekle, yoksa asyncio.run hata verir

api_id = 36736170
api_hash = '84b57ffb8eaebf77c979870ec46ef617'
bot_token = '7972292056:AAAE9ZXjJIrS5xJsoroJ_LPf6gbTLRMermjk'

client = TelegramClient('ruyakapisi_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply(
        "🌙 Hoş geldin sevgili yolcu...\n"
        "Rüya Kapısı artık seninle!\n\n"
        "Bana rüyanı anlat, hemen yorumlayayım ✨"
    )

@client.on(events.NewMessage)
async def tum_mesajlar(event):
    if event.is_private:  # sadece özel mesajlarda çalışsın
        ruya = event.raw_text.strip()
        if ruya.lower() not in ['/start', '']:
            await event.reply("Rüyanı aldım, bir saniye yorumluyorum... 🌟")
async def main():
    await client.start(bot_token=bot_token)
    print("Rüya Kapısı botu çalışıyor... 7/24 online! ❤️")
    await client.run_until_disconnected()

