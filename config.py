import os

BOT_TOKEN=os.getenv('BOT_TOKEN')
BOT_OWNER=int(os.getenv('BOT_OWNER'))
CHANNEL_ID=int(os.getenv('CHANNEL_ID'))

#private
IS_POSTING_REQUESTED = False