from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("Token_Bot").build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('simple', simple_command))
app.add_handler(CommandHandler('real', real_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('sub', sub_command))
app.add_handler(CommandHandler('mult', mult_command))
app.add_handler(CommandHandler('div', div_command))
app.add_handler(CommandHandler('deg', deg_command))
app.add_handler(CommandHandler('root', root_command))
app.add_handler(CommandHandler('Sum', Sum_command))

print('server start')
app.run_polling()
