import os
import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")
ADMINS = [540105210, 1029379671]

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
        )
        logger = logging.getLogger(__name__)


        async def edited_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
            msg = update.edited_channel_post
                if not msg:
                        return

                            message_id = msg.message_id
                                caption = msg.caption or "(no caption)"

                                    logger.info(f"Edited post detected: ID={message_id}")

                                        # PHOTO
                                            if msg.photo:
                                                    file_id = msg.photo[-1].file_id
                                                            for admin in ADMINS:
                                                                        await context.bot.send_photo(
                                                                                        chat_id=admin,
                                                                                                        photo=file_id,
                                                                                                                        caption=f"Edited post #{message_id}\n\n{caption}"
                                                                                                                                    )
                                                                                                                                            return

                                                                                                                                                # VIDEO
                                                                                                                                                    if msg.video:
                                                                                                                                                            file_id = msg.video.file_id
                                                                                                                                                                    for admin in ADMINS:
                                                                                                                                                                                await context.bot.send_video(
                                                                                                                                                                                                chat_id=admin,
                                                                                                                                                                                                                video=file_id,
                                                                                                                                                                                                                                caption=f"Edited post #{message_id}\n\n{caption}"
                                                                                                                                                                                                                                            )
                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                        # DOCUMENT
                                                                                                                                                                                                                                                            if msg.document:
                                                                                                                                                                                                                                                                    file_id = msg.document.file_id
                                                                                                                                                                                                                                                                            for admin in ADMINS:
                                                                                                                                                                                                                                                                                        await context.bot.send_document(
                                                                                                                                                                                                                                                                                                        chat_id=admin,
                                                                                                                                                                                                                                                                                                                        document=file_id,
                                                                                                                                                                                                                                                                                                                                        caption=f"Edited post #{message_id}\n\n{caption}"
                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                            return

                                                                                                                                                                                                                                                                                                                                                                # TEXT ONLY
                                                                                                                                                                                                                                                                                                                                                                    for admin in ADMINS:
                                                                                                                                                                                                                                                                                                                                                                            await context.bot.send_message(
                                                                                                                                                                                                                                                                                                                                                                                        chat_id=admin,
                                                                                                                                                                                                                                                                                                                                                                                                    text=f"Edited post #{message_id}\n\n{caption}"
                                                                                                                                                                                                                                                                                                                                                                                                            )


                                                                                                                                                                                                                                                                                                                                                                                                            app = Application.builder().token(TOKEN).build()
                                                                                                                                                                                                                                                                                                                                                                                                            app.add_handler(MessageHandler(filters.UpdateType.EDITED_CHANNEL_POST, edited_post))

                                                                                                                                                                                                                                                                                                                                                                                                            logger.info("Bot starting with webhook...")

                                                                                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                app.run_webhook(
                                                                                                                                                                                                                                                                                                                                                                                                                        listen="0.0.0.0",
                                                                                                                                                                                                                                                                                                                                                                                                                                port=int(os.getenv("PORT", 8080)),
                                                                                                                                                                                                                                                                                                                                                                                                                                        webhook_url=os.getenv("WEBHOOK_URL")
                                                                                                                                                                                                                                                                                                                                                                                                                                            )