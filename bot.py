import schedule
import json
import random
import time
import os

from ciscosparkapi import CiscoSparkAPI

DICTIONARY = os.environ.get('JARGON_DICTIONARY_FILE')
DEBUG = False

class Bot:
	def __init__(self):
		self.bot = CiscoSparkAPI(json.load(open('secrets.json'))["BOT_TOKEN"])

	def relax(self):
		print("RELAXED")
		dictionary = json.load(open(DICTIONARY))

		word = random.sample(list(dictionary), 1)[0]
		description = dictionary[word]

		for room in self.bot.rooms.list():
			message = f"""
### {word}

{description}
			"""
			self.bot.messages.create(roomId=room.id, markdown=message)

if __name__ == '__main__':
	if DEBUG:
		Bot().relax()
	else:
		print("Started")
		print(f"Scheduling at: {os.environ.get('DAILY_TIME')}")
		schedule.every().day.at(os.environ.get("DAILY_TIME")).do(Bot().relax)
		# Keep the process open
		while True:
			schedule.run_pending()
			time.sleep(1)