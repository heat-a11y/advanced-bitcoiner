from telethon import TelegramClient, events
import os

api_id = int(os.getenv("TG_API_ID", "0"))
api_hash = os.getenv("TG_API_HASH", "")
bot_token = os.getenv("TG_BOT_TOKEN", "")

if not all([api_id, api_hash, bot_token]):
    print("Missing env vars: TG_API_ID, TG_API_HASH, TG_BOT_TOKEN")
    exit(1)

client = TelegramClient("bot_session", api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    me = await client.get_me()
    print(f"Connected as bot: @{me.username} (ID: {me.id})")
    dialogs = await client.get_dialogs()
    print(f"Bot has {len(dialogs)} dialogs/chats.")
    if dialogs:
        print("Recent chats:")
        for d in dialogs[:5]:
            print(f"  - {d.name} ({d.id})")

with client:
    client.loop.run_until_complete(main())
