"""
TuxBot is a Discord Bot developed for the Tuxedo Gang Discord Server,
however, you may use source code of this Bot for your own purposes!
Copyright (c) 2019 Felix Eckert.
This Program is licensed under the 

Version 0.0 2019-11-30_1
"""

import discord
import json

from commands import cmd_echo

# Global Variables here
tuxVersion = "0.0"
tuxRelease = "2019-11-30_1"
client = discord.Client()
config = None
prefix = ""

# Command List
commands = {
	"echo":cmd_echo
}

def main():
	printStartMessages()

	#Load config file
	print("TuxBot is starting...")
	print("Loading config...")
	config = loadConfig()
	prefix = config["prefix"]

	print("\n/////////////////////\n")
	client.run(config["token"]) # Run the Bot


@client.event
async def on_ready():
	print("TuxBot is now logged in as: {0.user}".format(client))
	print("Running on servers: \n")
	[(lambda s: print("  - %s (%s)" % (s.name, s.id)))(s) for s in client.guilds] # List all servers the bot is currently logged in on


@client.event
async def on_message(message):
	if message.author != client.user: # Check if the message was send by the bot or not
		print("*******\nNew message recieved on server: {0}\nAuthor: {1}\nContent: {2}\n*******".format(message.guild, message.author, message.content)) # Print out message and some info

		if message.content.startswith(prefix):
			# Parse Command
			invoke = message.content[len(prefix):].split(" ")[0]
			args = message.content.split(" ")[1:]

			if invoke


def printStartMessages():
	print("/////////////////////")
	print("TuxBot Version: {0}".format(tuxVersion))
	print("TuxBot Release: {0}".format(tuxRelease))
	print("/////////////////////\n")


def loadConfig():
	with open("../res/config.json", "r") as rawConfig:
		return json.load(rawConfig)


if __name__ == "__main__":
	main()
