from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder, ContextTypes
from datetime import *
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}, если ты хочешь чтобы я тебе помог с расчётами нажми /help')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Выбери с какими числами ты хочешь работать, простыми или вещественными:\n/simple\n/real')

async def simple_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Вот список операций доступных с простыми числами:\n/sum - Суммирование\n/sub - Вычитание\n/mult - Умножение\n/div - Деление\n/deg - Возведение в степень\n/root - Корень квадратный\n\nДля того, чтобы я правильно рассчитал, введи:\n/название_операции число1 число2')

async def real_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Вот список операций доступных с вещественными числами:\n/Sum - Суммирование\n')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Равно: {x} + {y} = {x + y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Равно: {x} - {y} = {x - y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Равно: {x} * {y} = {x * y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Равно: {x} / {y} = {x / y}')

async def deg_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Равно: {x}^({y}) = {x ** y}')

async def root_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    await update.message.reply_text(f'Равно: {x ** (0.5)}')

async def Sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'Равно: {x} + {y} = {x + y}')