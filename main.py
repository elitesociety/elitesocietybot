import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from keep_alive import keep_alive


TOKEN = os.getenv("BOT_TOKEN")


# Welcome message
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
        photo=open("Welcome.jpg", "rb"),
        reply_markup=reply_markup
    )



# Mission button
async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.data == "mission1":

        await query.message.reply_video(
            video=open("mission1.mp4", "rb"),
            caption='🎯 MISSION #001\n\nHint : "A familiar mask. A familiar secret."\n\nPASSWORD : <a href="https://forms.gle/BrY71x59TjJB5btt9">Tell us</a>',
            parse_mode="HTML"
        )



def main():

    # Start web server for UptimeRobot
    keep_alive()


    # Create bot
    app = Application.builder().token(TOKEN).build()


    # /start command
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    # Button handler
    app.add_handler(
        CallbackQueryHandler(
            mission
        )
    )


    print("Elite Society Bot Started")


    # Run bot
    app.run_polling()



if __name__ == "__main__":
    main()