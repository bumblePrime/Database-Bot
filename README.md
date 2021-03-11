# Digital-Media-Bot

This project is made around a simple bot that at the time of writing, is non-intelligent. All it does is searches a database of media files that are stored on a local machine. While prototyping this idea I implemented the bot in a CLI environment(check branch titled **CLI-Prototype** (https://github.com/bumblePrime/Digital-Media-Bot/tree/CLI-Prototype)) and later integrated the bot with telegram and deployed it on heroku so that it can be used at all times from anywhere.
My own bot has been up since 03 March 2021 9:45 PM IST and I am regularly adding more and more personalised abilities to it.

This repository is like a template that can be used to design your own Media Bot as I like to call it. 
You will need a database of your media files, I've made mine using a script I wrote in python that is also availabe at https://github.com/bumblePrime/Digital-Media-Organizer that outputs a sqlite database. Once you have your own database,copy that file into the current directory and go to `creds.py` file and place the name of database and the name of table inside the database to be searched.


You will also need heroku account and telegram API token. The former can be made by visiting heroku website. 
For the API token
1. Open Telegram and search **@botfather**, be sure to select the verified(blue tick) account.
2. Type /newbot.It will show “Alright, a new bot. How are we going to call it? Please choose a name for your bot.”
3. Type the name of your bot.
4. After, it’ll show “Good. Now let’s choose a username for your bot. It must end in **bot**. Like this, for example: TetrisBot or tetris_bot.”
5. You’ve to give a unique username and it should be ending with bot. We will need this username later.
6. After giving the name it’ll show :-
“Done! Congratulations on your new bot. You will find it at t.me/diNorodobot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you’ve finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.Use this token to access the HTTP API: **TOKEN**
7. Copy the API Token and paste it and the username in the `creds.py` file.

Now to deploy the bot on heroku you need 2 files that are `requirements.txt` and a `Procfile`.
For the sake of convenience I have already added both files in the repo and you can use the same if you wish to.

But if you want to prototype on local machine, make sure you have **gunicorn**,**telegram** and **flask** libraries installed.
   ```
   pip install gunicorn
   pip install flask
   ```

If in future you use other libraries in the bot then you will need to update the requirements file.To do so automatically you use the following command
   ```
   pip freeze > requirements.txt
   ```

For the procfile all you need is make a new file names **Procfile** and enter one line
   ```
    web: gunicorn Bot:app
   ```
Here **Bot** signifies the name of python file that has the main function.


Once you have done this it is time to deploy the bot to heroku. To do so
1. On the heroku dashboard select new and click `Create New App`.
2. Enter name of app and click Create App button.
3. You you will land on the deployment page where you will have 3 ways to deploy the bot.
4. But before that you need one more credential and that is the heroku app URL. To find that go to the settings tab and scroll down to find the domain whcih will be in the format `https://<your app name>.herokuapp.com/`. Copy this URL and paste it in the `creds.py` file.
5. Now go back to the deploy tab and deploy the bot using any way you prefer. While deploying using Heroku CLI, the on screen instructions will guide you(be sure to have git installed on you system), all you need to do is copy paste the commands. When deploying using github select the repo and branch you wish to deploy.
6. Once the bot has been deployed on the cloud, visit the app domain `https://<your app name>.herokuapp.com/` and type start_bot in the url. You will get a message **Bot activated**.
7. Head over to telegrama and start using the bot.


## Future Updates:
At the time of writing I have added just one ability in this bot template that checks if a file exists or not.If you are comfortable with python and MySQL you can add more abilities of your own that suit your personal needs. Will add some more common abilities in fututre iterartions of this repo.
One major upgrade that I have planned though is ability to update the database on the fly since at the moment if your media collection has any new additions, you will have to update the database file manually(or rerunning teh script) and redeploy the bot on heroku for the new entries to reflect. 
Upgrade coming soon.


## References and Acknowledgement:
- The idea for this bot was conceived during a Chatbot Building workshop hosted by Nitesh Jyotishi Sir, my senior at BIT Jaipur, during which I designed the CLI prototype of the bot.
- To integrate the bot with telegram I referenced this article https://www.toptal.com/python/telegram-bot-tutorial-python.
- Many thanks to my friends who helped me test the bot when I deployed it and their much needed feedback along the way.
