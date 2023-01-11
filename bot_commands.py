from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import rational as rt
import complex as co
import logger as lg

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Для начала введите /start')
    await update.message.reply_text(f'Для расчёта рациональных числе нужно ввести команду:\n /rational a + b;\n')
    await update.message.reply_text(f'Для расчёта комплексных числе нужно ввести команду:\n /complex a + bj + c + dj;\n')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}, это - калькулятор.')
    await update.message.reply_text(f'Выберете тип калькулятора:')
    await update.message.reply_text(f'Для расчёта рациональных числе нужно ввести команду:\n /rational a + b;\n')
    await update.message.reply_text(f'Для расчёта комплексных числе нужно ввести команду:\n /complex a + bj + c + dj;\n')

async def rational_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global one_number
    global two_number
    global oper
    global param 
    one_number = 0
    two_number = 0
    oper = ''
    param = 'rational'
    
    try:
        msg = update.message.text
        items = msg.split()
        one_number = int(f'{items[1]}')
        oper = str(items[2])
        two_number = int(f'{items[3]}')
        result = (f'{one_number}{oper}{two_number} = {rt.operation_rational(oper,  one_number, two_number)}')
        await update.message.reply_text(f'{result}')
        lg.log_info(f'{param}: {result}')
    except:
        await update.message.reply_text(f'Введены неверные данные')    

async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global one_number
    global two_number
    global oper
    global param
    one_number = 0
    two_number = 0
    oper = ''
    param = 'complex'

    try:
        msg = update.message.text
        items = msg.split()
        size = len(items)
        await update.message.reply_text(f'{size}')
        if size == 8:
            one_number = str(f'{items[1]}{items[2]}{items[3]}')
            oper = str(items[4])
            two_number = str(f'{items[5]}{items[6]}{items[7]}')
        else:
            if size == 4:
                one_number = str(f'{items[1]}')
                oper = str(items[2])
                two_number = str(f'{items[3]}')
            else: 
                if size == 6:
                    try:
                        comp = complex(str(f'{items[1]}{items[2]}{items[3]}'))
                        one_number = str(f'{items[1]}{items[2]}{items[3]}')
                        oper = str(items[4])
                        two_number = str(f'{items[5]}')
                    except ValueError:
                        one_number = str(items[1])
                        oper = str(items[2])
                        two_number = str(f'{items[3]}{items[4]}{items[5]}')

        result = (f'{one_number}{oper}{two_number} = {co.operation_complex(oper,  one_number, two_number)}')
        await update.message.reply_text(f'{result}')
        lg.log_info(f'{param}: {result}')        

    except:
        await update.message.reply_text(f'Введены неверные данные') 