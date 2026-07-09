from telethon import TelegramClient
import os

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
phone = os.getenv("TG_PHONE")

if not all([api_id, api_hash, phone]):
    print("Set env vars: TG_API_ID, TG_API_HASH, and TG_PHONE")
    exit(1)

client = TelegramClient("session", int(api_id), api_hash)

async def main():
    await client.start(phone)
    me = await client.get_me()
    print(f"Connected as: {me.first_name} {me.last_name or ''} (@{me.username or 'no username'})")
    dialogs = await client.get_dialogs()
    print(f"You have {len(dialogs)} dialogs.")
    print("Top 5 dialogs:")
    for d in dialogs[:5]:
        print(f"  - {d.name}")

with client:
    client.loop.run_until_complete(main())
