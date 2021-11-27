# MemeBot
A telegram bot that sends a meme a day, from reddit's top meme of the day

You can use the bot either with an external scheduler (ex: pythonanywhere) or by running it all the time and using the built-in scheduler

### How does it work
The bot, via feedparser, extracts the top of the day from r / memes and subsequently the resources are extracted via json, which can be images, gifs or videos; they are then directly sent to the chat.
