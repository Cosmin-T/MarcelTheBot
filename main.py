import discord
from discord import *
import re
from discord.ext import commands
from keep_alive import keep_alive

# Set up Discord intents which dictate what events the bot can track
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.messages = True
intents.message_content = True

# Initialize Discord client with the specified intents
client = discord.Client(intents=intents)

# Token for the bot to authenticate with the Discord API
d_token = 'MTExMzA2MDQ1MjM4MjAxOTY2NQ.GnLjiS.KBgc_CwxZnv2ZVUe4UvNfDY2m6-ZzjbfjNGRVQ'

# Regular expression to recognize website URLs
url_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


# Event to be executed when the bot has connected to the Discord servers
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


# Global flag to control if the bot should respond to messages
should_respond = True


# Event to be executed every time a message is sent in a server the bot is in
@client.event
async def on_message(message):
  global should_respond  # Access the global flag

  # If the message is from the bot itself, do nothing
  if message.author == client.user:
    return

  # If the command to pause the bot is received, change the should_respond flag to False and confirm the action to the user
  if message.content.lower() == '!off':
    should_respond = False
    await message.channel.send("I'm Paused")
    return

  # If the command to resume the bot is received, change the should_respond flag to True and confirm the action to the user
  if message.content.lower() == '!on':
    should_respond = True
    await message.channel.send("I'm Active")
    return

  # If the bot is paused, ignore the message
  if not should_respond:
    return

  # Print the username of the author and the message content
  print(f'User: {message.author} content: "{message.content}"')

  # Array of commands the bot will recognize
  command_list = ["!hello", "!help"]

  # Check if the received message is a recognized command
  for command in command_list:
    if message.content.lower() == command:
      print(f'Command {command} recognized.')
      # If the '!hello' command is recognized, send a greeting to the user
      if command == '!hello':
        await message.channel.send(
          "Hello!, As a Discord bot, my function is to identify website names and automatically transform them into clickable links"
        )
      # If the '!help' command is recognized, send an explanation of the bot's function to the user
      elif command == '!help':
        await message.channel.send(
          "I am a Discord bot designed to effortlessly recognize website names and seamlessly convert them into clickable links. Rest assured, you can rely on me to handle this task without any need for your involvement or concern.\nI can be paused or resumed by typing: **!off** or **!on**"
        )
      return

  # Mapping of website names to URLs
  url_mapping = {
    'google':
    'https://www.google.com',
    'youtube':
    'https://www.youtube.com',
    'facebook':
    'https://www.facebook.com',
    'amazon':
    'https://www.amazon.com',
    'twitter':
    'https://www.twitter.com',
    'instagram':
    'https://www.instagram.com',
    'linkedin':
    'https://www.linkedin.com',
    'wikipedia':
    'https://www.wikipedia.org',
    'yahoo':
    'https://www.yahoo.com',
    'reddit':
    'https://www.reddit.com',
    'pinterest':
    'https://www.pinterest.com',
    'bing':
    'https://www.bing.com',
    'ebay':
    'https://www.ebay.com',
    'netflix':
    'https://www.netflix.com',
    'microsoft':
    'https://www.microsoft.com',
    'apple':
    'https://www.apple.com',
    'whatsapp':
    'https://www.whatsapp.com',
    'wordpress':
    'https://www.wordpress.com',
    'zoom':
    'https://www.zoom.us',
    'adobe':
    'https://www.adobe.com',
    'craigslist':
    'https://www.craigslist.org',
    'quora':
    'https://www.quora.com',
    'shopify':
    'https://www.shopify.com',
    'soundcloud':
    'https://www.soundcloud.com',
    'dropbox':
    'https://www.dropbox.com',
    'bbc':
    'https://www.bbc.co.uk',
    'twitch':
    'https://www.twitch.tv',
    'spotify':
    'https://www.spotify.com',
    'cnn':
    'https://www.cnn.com',
    'slideshare':
    'https://www.slideshare.net',
    'imdb':
    'https://www.imdb.com',
    'hulu':
    'https://www.hulu.com',
    'cnet':
    'https://www.cnet.com',
    'etsy':
    'https://www.etsy.com',
    'indeed':
    'https://www.indeed.com',
    'yahoo':
    'https://www.yahoo.com',
    'zillow':
    'https://www.zillow.com',
    'blogger':
    'https://www.blogger.com',
    'github':
    'https://www.github.com',
    'snapchat':
    'https://www.snapchat.com',
    'vimeo':
    'https://www.vimeo.com',
    'salesforce':
    'https://www.salesforce.com',
    'flipkart':
    'https://www.flipkart.com',
    'stackoverflow':
    'https://www.stackoverflow.com',
    'udemy':
    'https://www.udemy.com',
    'yelp':
    'https://www.yelp.com',
    'walmart':
    'https://www.walmart.com',
    'aliexpress':
    'https://www.aliexpress.com',
    'airbnb':
    'https://www.airbnb.com',
    'live':
    'https://www.live.com',
    'nytimes':
    'https://www.nytimes.com',
    'paypal':
    'https://www.paypal.com',
    'tiktok':
    'https://www.tiktok.com',
    'telegram':
    'https://www.telegram.org',
    'dailymotion':
    'https://www.dailymotion.com',
    'skype':
    'https://www.skype.com',
    'canva':
    'https://www.canva.com',
    'pexels':
    'https://www.pexels.com',
    'steam':
    'https://www.steampowered.com',
    'mozilla':
    'https://www.mozilla.org',
    'office':
    'https://www.office.com',
    'weebly':
    'https://www.weebly.com',
    'slack':
    'https://www.slack.com',
    'flickr':
    'https://www.flickr.com',
    'wayfair':
    'https://www.wayfair.com',
    'homedepot':
    'https://www.homedepot.com',
    'archive':
    'https://www.archive.org',
    'pixabay':
    'https://www.pixabay.com',
    'unsplash':
    'https://www.unsplash.com',
    'asana':
    'https://www.asana.com',
    'eventbrite':
    'https://www.eventbrite.com',
    'theguardian':
    'https://www.theguardian.com',
    'glassdoor':
    'https://www.glassdoor.com',
    'nasa':
    'https://www.nasa.gov',
    'uber':
    'https://www.uber.com',
    'booking':
    'https://www.booking.com',
    'buzzfeed':
    'https://www.buzzfeed.com',
    'expedia':
    'https://www.expedia.com',
    'tripadvisor':
    'https://www.tripadvisor.com',
    'mailchimp':
    'https://www.mailchimp.com',
    'bitly':
    'https://www.bitly.com',
    'godaddy':
    'https://www.godaddy.com',
    'coursera':
    'https://www.coursera.org',
    'khanacademy':
    'https://www.khanacademy.org',
    'trello':
    'https://www.trello.com',
    'ted':
    'https://www.ted.com',
    'linkedin':
    'https://www.linkedin.com',
    'quora':
    'https://www.quora.com',
    'target':
    'https://www.target.com',
    '9gag':
    'https://www.9gag.com',
    'forbes':
    'https://www.forbes.com',
    'doodle':
    'https://www.doodle.com',
    'zendesk':
    'https://www.zendesk.com',
    'zoho':
    'https://www.zoho.com',
    'bandcamp':
    'https://www.bandcamp.com',
    'behance':
    'https://www.behance.net',
    'chase':
    'https://www.chase.com',
    'costco':
    'https://www.costco.com',
    'stackoverflow':
    'https://www.stackoverflow.com',
    'bbc':
    'https://www.bbc.com',
    'foxnews':
    'https://www.foxnews.com',
    'washingtonpost':
    'https://www.washingtonpost.com',
    'alibaba':
    'https://www.alibaba.com',
    'black desert':
    'https://blackdesertonline.fandom.com/wiki/Black_Desert_Online_Wiki'
  }

  # Responding to user post with a new message of the link it recognized, more spam
  # for website_name in url_mapping:
  #   if website_name in message.content.lower():
  #     print(f'Website name "{website_name}" recognized.')
  #     await message.channel.send(f"{url_mapping[website_name]}\nOh? Did I spot a website name? I gotchu bro, here's the link:")
  #     return

  # Deleting user post and posting a new message of what x-user said modified with the link included, less spam
  for website_name in url_mapping:
    pattern = re.compile(r'\b' + re.escape(website_name) + r'\b',
                         re.IGNORECASE)
    if pattern.search(message.content) is not None:
      print(f'Website name "{website_name}" recognized.')
      # Recreating the new message
      new_message = pattern.sub(url_mapping[website_name], message.content)
      new_message = f"{message.author} said: {new_message}"
      # Delete the user's original message
      await message.delete()
      # Send a new message with the website name replaced by its URL
      await message.channel.send(new_message)
      return


# Keep the bot working forever
keep_alive()
# Run the bot
client.run(d_token)
