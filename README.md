# SamAI

An everything AI for Discord.

## URLs

* [Production Join URL](https://discord.com/oauth2/authorize?client_id=1167261104846680195&scope=bot&permissions=395137108992)
* [Development Join URL](https://discord.com/oauth2/authorize?client_id=1167330015193608202&scope=bot&permissions=395137108992)

## TODO

* [x] When a user sends a message with a YouTube link, the bot should add a reaction to it. That message should be watched for 24 hours. If any user also reacts to the same reaction, it will provide the summary of the video. If no one has reacted in 24 hours, the bot should remove the reaction and not provide the summary. The bot should only summarize the video if the user reacts to it.
* [ ] Restrict so that only the user who created the thread can message in it unless they explicitly allow one (or all) other users. This should be done with another slash command.
