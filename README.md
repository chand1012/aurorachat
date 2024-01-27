# AuroraChat

An everything AI for Discord.

## URLs

* [Production Join URL](https://discord.com/oauth2/authorize?client_id=1167261104846680195&scope=bot&permissions=395137108992)
* [Development Join URL](https://discord.com/oauth2/authorize?client_id=1167330015193608202&scope=bot&permissions=395137108992)

## Deployment Configuration

We are going to host Aurora on [Fly](https://fly.io). There will be two instances of Aurora, one for development and one for production. The development one will only be deployed whenever a developer runs `just deploy` on their systems. The production one will automatically deploy from `main` . For development she will be given the minimum spec machine available, and for production she will start with 512MB of RAM and 1 CPU core. If she needs more resources, we will give them to her.

There will also be two separate databases for dev and prod, also hosted on Fly, and with an admin interface. 

## Listings

* [Discord Bot List](https://discord.ly/aurora-9672)
* [Top.gg](https://top.gg/bot/1167261104846680195)
* [Botlist.me](https://botlist.me/bots/1167261104846680195)
* [discord.bots.gg](https://discord.bots.gg/bots/1167261104846680195)

## TODO
