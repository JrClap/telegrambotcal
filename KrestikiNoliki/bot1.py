import logging

from aiogram import Bot, Dispatcher, types

API_TOKEN = 'Bot_Token'

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


is_game_running = False


turn = 'X'

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    global is_game_running
    if is_game_running:
        await message.answer("The game is already running.")
        return

    is_game_running = True
    await message.answer("The game has started! Your turn, X.")

@dp.message_handler(commands=['stop'])
async def cmd_stop(message: types.Message):
    global is_game_running
    if not is_game_running:
        await message.answer("The game is already stopped.")
        return

    is_game_running = False
    await message.answer("The game has stopped.")

@dp.message_handler(commands=['board'])
async def cmd_board(message: types.Message):
    board_msg = "```\n"
    for i in range(3):
        for j in range(3):
            board_msg += board[i][j] + " | "
        board_msg = board_msg[:-3]
        board_msg += "\n---+---+---\n"
    board_msg = board_msg[:-18] + "```"

    await message.answer(board_msg)

@dp.message_handler(lambda message: message.text.startswith('/move'))
async def cmd_move(message: types.Message):
    global turn, board
    content = message.text.split()

    if len(content) != 3:
        await message.answer("Please specify the row and column.")
        return

    row, col = int(content[1]), int(content[2])
    if row < 0 or row > 2 or col < 0 or col > 2:
        await message.answer("Invalid move.")
        return

    if board[row][col] != ' ':
        await message.answer("This cell is occupied.")
        return

    board[row][col] = turn
    await message.answer("Move accepted.")

    if turn == 'X':
        turn = 'O'
        await message.answer("It's O's turn.")
    else:
        turn = 'X'
        await message.answer("It's X's turn.")



if __name__ == '__main__':
    dp.start_polling(dp, skip_updates=True)
