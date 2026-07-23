import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from keep_alive import keep_alive


TOKEN = os.getenv("BOT_TOKEN")


# Welcome Image
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎯 START MISSION",
                callback_data="mission1"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)


    await update.message.reply_photo(
        photo=open("welcome.jpg", "rb"),

        caption="""
🕵️ Welcome to Elite Society

Your journey begins now.

Are you ready to uncover the truth?
        """,

        reply_markup=reply_markup
    )



# Mission button
async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.data == "mission1":

        await query.message.reply_video(
            video=open("mission1.mp4", "rb"),

            caption="""
🎯 MISSION #001

Your first mission has started.

Watch carefully.
Every detail matters.

Good luck.
            """
        )



def main():

    keep_alive()


    app = Application.builder().token(TOKEN).build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            mission
        )
    )


    print("Elite Society Bot Started")


    app.run_polling()



if __name__ == "__main__":
    main()