# Digital-Media-Bot

This branch contains a CLI protottype of the bot that is present in main branch. This one runs locally in a terminal window. You will need a database of your media files, I've made mine using a script I wrote in python that is also availabe at https://github.com/bumblePrime/Digital-Media-Organizer that outputs a sqlite database. Once you have your own database,copy that file into the current directory and go to `creds.py` file and place the name of database and the name of table inside the database to be searched. 

Open termianl/command promt in the same directory and run the python script
  ```
  python Bot.py
  ```
  The bot is now active and you can search the database. To stop the bot type 'bye' or 'thank you' and it will stop execution.
