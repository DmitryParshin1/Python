# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)

# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))


# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,4,1,8]
# plt.plot(list)


# plt.show()  

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5936523433:AAGM2jLCun2M0hPcXzIaycAi0U1i01oNFo8").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')

app.run_polling()