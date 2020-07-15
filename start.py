# FatDubs
# 7/15/2020
# Guild Bot

import main     # main project file
import getpass  # allows password to be hidden during input

email = input('email: ')
password = getpass.getpass('password: ')
username = input('bot ign: ')

bot = main.thread(email,password,username)
bot.start()
