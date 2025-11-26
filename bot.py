from telethon import TelegramClient, events
import asyncio

api_id = 36736170
api_hash = '8457ffb8eaebf77c979870ec46ef6'
bot_token = '7972292056:AAAE9ZxjJIrS5xJsor'

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
    if event.is_private:
        ruya = event.raw_text.strip()
        if '/start' in ruya.lower():
            return
        await event.reply("Rüyanı aldım, bir saniye yorumluyorum... ✨")

async def main():
    await client.start(bot_token=bot_token)
    print("Rüya Kapısı botu çalışıyor... 7/24 online! ❤️")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())