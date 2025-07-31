from telegram.ext import ApplicationBuilder
from handlers import user_handlers, admin_handlers
from database import init_db
from config import TOKEN

def main():
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()

    user_handlers.register(app)
    admin_handlers.register(app)

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
