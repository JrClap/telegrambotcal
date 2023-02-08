import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes

from strings import *


async def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        await True
    await False


async def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == SYMBOL_UNDEF:
            counter += 1
    await counter


async def game(callBackData):
    
    message = ANSW_YOUR_TURN 
    alert = None

    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9:  
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == SYMBOL_UNDEF: 
            charList[buttonNumber] = SYMBOL_X  
            if isWin(charList, SYMBOL_X):  
                message = ANSW_YOU_WIN
            else:  
                if countUndefinedCells(charList) != 0:  
                    isCycleContinue = True
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand] == SYMBOL_UNDEF:  
                            charList[rand] = SYMBOL_O
                            isCycleContinue = False  
                            if isWin(charList, SYMBOL_O):  
                                message = ANSW_BOT_WIN

        else:
            alert = ALERT

        if countUndefinedCells(charList) == 0 and message == ANSW_YOUR_TURN:
            message = ANSW_DRAW

        callBackData = ''
        for c in charList:
            callBackData += c

    if message == ANSW_YOU_WIN or message == ANSW_BOT_WIN or message == ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None 

    await message, callBackData, alert


async def getKeyboard(callBackData):
    keyboard = [[], [], []] 

    if callBackData != None: 
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    await keyboard


async def newGame(update: Update, _):
    data = ' '
    for i in range(0, 9):
        data += SYMBOL_UNDEF

    await update.message.reply_text(ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))

async def button(update, _):
    query = update.callback_query
    callbackData = query.data 

    message, callbackData, alert = game(callbackData)  # игра
    if alert is None: 
        await query.answer()  
        await query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else: 
        await query.answer(text=alert, show_alert=True)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(ANSW_HELP)


if __name__ == '__main__':
    app = ApplicationBuilder().token("6111558891:AAG1pQIQIqWUH20fhu8Euggcbu9iOTvdCKo").build() 

    app.add_handler(CommandHandler('start', newGame))
    app.add_handler(CommandHandler('new_game', newGame))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.Text, help_command))  
    app.add_handler(CallbackQueryHandler(button))  


    print('server start')
    app.run_polling()
    