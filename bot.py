import asyncio
from telethon import TelegramClient, events

# BURAYI KENDİ BİLGİLERİNLE DOLDUR (3 satır) -----------------
api_id =7972292056
api_hash = '0123456789abcdef0123456789abcdef'   # my.telegram.org'dan aldığın api_hash
bot_token = '7439128749:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # @BotFather'dan aldığın token
# ------------------------------------------------------------

# Botu başlat
client = TelegramClient('ruyakapisi_session', api_id, api_hash).start(bot_token=bot_token)

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

print("🌙 Rüya Kapısı botu çalışıyor... 7/24 online!")
client.run_until_disconnected()
