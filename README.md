# MarcelTheBot

## Introduction
This guide will walk you through the process of installing and running a Discord bot that can automatically recognize website names in messages and convert them into clickable links. The bot is also equipped with the ability to pause and resume its functionality.

## Prerequisites
Before you begin, make sure you have the following:
- A Discord account.
- Access to a Discord server where you have administrative privileges.
- Python installed on your computer. You can download Python from the [official website](https://www.python.org/downloads/).

## Installation Steps

### Step 1: Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on the "New Application" button.
3. Give your application a name (this will be your bot's name).
4. Click on "Create" to create the application.
5. In the left sidebar, click on "Bot" and then click the "Add Bot" button.
6. Under the "Token" section, click the "Copy" button to copy your bot token. You'll need this token later.

### Step 2: Invite the Bot to Your Server
1. In the left sidebar, click on "OAuth2."
2. In the "OAuth2 URL Generator" section, select the "bot" scope.
3. Scroll down and select the following bot permissions:
   - View Channels
   - Send Messages
   - Read Message History
   - Manage Messages (for deleting and editing messages)
4. Copy the generated URL.
5. Paste the URL into your web browser, select your Discord server, and click "Authorize" to invite the bot to your server.

### Step 3: Configure the Bot
1. Download the Python script from the bot creator or the GitHub repository where it's hosted.
2. Open the script in a text editor or integrated development environment (IDE).

### Step 4: Configure Bot Token
1. In the script, locate the line that says `d_token = 'YOUR_BOT_TOKEN_HERE'`.
2. Replace `'YOUR_BOT_TOKEN_HERE'` with the bot token you copied in Step 1.

### Step 5: Customize Website URLs (Optional)
- If you want to add or modify the list of recognized website names and their corresponding URLs, you can do so by editing the `url_mapping` dictionary in the script. Add or modify entries in the format `'Website Name': 'Website URL'`.

### Step 6: Run the Bot
1. Open a terminal or command prompt.
2. Navigate to the directory where the bot script is located.
3. Run the bot script using the following command: bash```python your-bot-script.py```


Replace `your-bot-script.py` with the actual name of your bot script.

## Using the Bot

Once the bot is running and connected to your server, you can use the following commands:

- `!hello`: Sends a greeting message from the bot.
- `!help`: Provides an explanation of the bot's function.
- `!off`: Pauses the bot, causing it to ignore messages.
- `!on`: Resumes the bot, allowing it to respond to messages again.

The bot will automatically recognize website names in messages and convert them into clickable links. You can also customize the list of recognized websites by editing the `url_mapping` dictionary in the script.

## NOTE

The bot cannot edit messages since Discord does not permit it. Instead, it will duplicate your message, remove the original, and then insert the message with the updated link into a new one.
