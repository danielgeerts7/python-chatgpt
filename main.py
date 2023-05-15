# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# make sure to set OPENAI_API_KEY in the env file
import os
from pathlib import Path
import openai

from src.send_prompt import sendPrompt

OPENAI_APIKEY = os.environ['OPENAI_APIKEY']

if (OPENAI_APIKEY):
    print (OPENAI_APIKEY)
else:
    print("OPENAI_APIKEY not found in env")

openai.api_key = OPENAI_APIKEY

print("Start program")

# Generate map with rooms that are connected through North, East, South, West

# Generate items or missions or enemies in those rooms

# Generate characters that have a goal

# Let the user play the text-based-game

sendPrompt()