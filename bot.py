import asyncio
import os
from telegram.ext import Application, MessageHandler, filters
from datetime import timedelta

TOKEN = os.getenv("BOT_TOKEN")

ADMINS = os.getenv("ADMINS", "")
ADMINS = [int(x) for x in ADMINS.split(",") if x.strip()]

async def new_post(update, context):
    msg = update.channel_post
    if not msg:
        return

    caption = msg.caption or "(no caption)"
    message_id = msg.message_id
    channel_name = msg.chat.title or "Unknown Channel"

    header = f"📢 New post from {channel_name}\nPost #{message_id}\n\n"
    iran_time = msg.date + timedelta(hours=3, minutes=30)
    footer = f"\n\n🕒 {iran_time}"
    full_caption = header + caption + footer

    if msg.photo:
        file_id = msg.photo[-1].file_id
        for admin in ADMINS:
            await context.bot.send_photo(admin, file_id, caption=full_caption)

    elif msg.video:
        file_id = msg.video.file_id
        for admin in ADMINS:
            await context.bot.send_video(admin, file_id, caption=full_caption)

    elif msg.document:
        file_id = msg.document.file_id
        for admin in ADMINS:
            await context.bot.send_document(admin, file_id, caption=full_caption)

    else:
        for admin in ADMINS:
            await context.bot.send_message(admin, full_caption)


async def edited_post(update, context):
    msg = update.edited_channel_post
    if not msg:
        return

    caption = msg.caption or "(no caption)"
    message_id = msg.message_id
    channel_name = msg.chat.title or "Unknown Channel"

    header = f"✏️ Edited post from {channel_name}\nPost #{message_id}\n\n"
    iran_time = msg.edit_date + timedelta(hours=3, minutes=30)
    footer = f"\n\n🕒 {iran_time}"
    full_caption = header + caption + footer

    if msg.photo:
        file_id = msg.photo[-1].file_id
        for admin in ADMINS:
            await context.bot.send_photo(admin, file_id, caption=full_caption)

    elif msg.video:
        file_id = msg.video.file_id
        for admin in ADMINS:
            await context.bot.send_video(admin, file_id, caption=full_caption)

    elif msg.document:
        file_id = msg.document.file_id
        for admin in ADMINS:
            await context.bot.send_document(admin, file_id, caption=full_caption)

    else:
        for admin in ADMINS:
            await context.bot.send_message(admin, full_caption)


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, new_post))
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_CHANNEL_POST, edited_post))

    print("Bot is running for 60 seconds...")

    # This runs polling AND stops automatically after 60 seconds
    await app.run_polling(stop_after=60)


if __name__ == "__main__":
    asyncio.run(main())
