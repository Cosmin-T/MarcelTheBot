# MarcelTheBot

Introduction

This guide will walk you through the process of installing and running a Discord bot that can automatically recognize website names in messages and convert them into clickable links. The bot is also equipped with the ability to pause and resume its functionality.

Prerequisites

Before you begin, make sure you have the following:

A Discord account.
Access to a Discord server where you have administrative privileges.
Python installed on your computer. You can download Python from the official website.
Installation Steps

Step 1: Create a Discord Bot
Go to the Discord Developer Portal.
Click on the "New Application" button.
Give your application a name (this will be your bot's name).
Click on "Create" to create the application.
In the left sidebar, click on "Bot" and then click the "Add Bot" button.
Under the "Token" section, click the "Copy" button to copy your bot token. You'll need this token later.
Step 2: Invite the Bot to Your Server
In the left sidebar, click on "OAuth2."
In the "OAuth2 URL Generator" section, select the "bot" scope.
Scroll down and select the following bot permissions:
View Channels
Send Messages
Read Message History
Manage Messages (for deleting and editing messages)
Copy the generated URL.
Paste the URL into your web browser, select your Discord server, and click "Authorize" to invite the bot to your server.
Step 3: Configure the Bot
Download the Python script from the bot creator or the GitHub repository where it's hosted.
Open the script in a text editor or integrated development environment (IDE).
Step 4: Configure Bot Token
In the script, locate the line that says d_token = 'YOUR_BOT_TOKEN_HERE'.
Replace 'YOUR_BOT_TOKEN_HERE' with the bot token you copied in Step 1.
Step 5: Customize Website URLs (Optional)
If you want to add or modify the list of recognized website names and their corresponding URLs, you can do so by editing the url_mapping dictionary in the script. Add or modify entries in the format 'Website Name': 'Website URL'.

Step 6: Run the Bot
Open a terminal or command prompt.
Navigate to the directory where the bot script is located.
Run the bot script using the following command:
Copy code
python your-bot-script.py
Replace your-bot-script.py with the actual name of your bot script.

Using the Bot

Once the bot is running and connected to your server, you can use the following commands:

!hello: Sends a greeting message from the bot.
!help: Provides an explanation of the bot's function.
!off: Pauses the bot, causing it to ignore messages.
!on: Resumes the bot, allowing it to respond to messages again.
The bot will automatically recognize website names in messages and convert them into clickable links. You can also customize the list of recognized websites by editing the url_mapping dictionary in the script.

Conclusion

Congratulations! You've successfully installed and configured a Discord bot that can recognize website names and perform automatic link conversion. You can further customize the bot's behavior and add more features as needed. Enjoy using your new Discord bot!
