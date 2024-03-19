import guidance
from guidance import models, gen, instruction
import os
import openai
from dotenv import load_dotenv
load_dotenv()

# get the api key and set the model.
api_key = os.environ.get('OPENAI_API_KEY')
local_api_url = os.environ.get('LOCAL_API_URL')
openai.api_key = api_key

# check if it should use local text generation.
if os.environ.get("USE_LOCAl_TEXT_GEN") == "False":
    gpt_instruct = models.OpenAI("gpt-3.5-turbo-instruct")
else:
    gpt_instruct = models.OpenAI("gpt-3.5-turbo-instruct", base_url="http://"+local_api_url+":5000/v1")



async def generate_response(messages, scenario, players):
    # this stores the chat messages.
    messages_string = ""
    players_string = ""
    for player in players:
        players_string += player["username"]+"\n"

    for message in messages:
        if message["role"] != "Notification":
            messages_string += message["username"] + ": " + message["message"] + "\n"

    with instruction():
        lm = gpt_instruct + f"""You are a narrator for a text adventure game, do not explain or try to make decisions for the players,
slowly progress the story and make it interesting for the players, keep your responses short and to the point, 1-2 sentances.
Players In Game:
{players_string}
Do not make decisions for these players.
Scenario: {scenario}
Start of chat history.
{messages_string}
End of chat history.
Narrator:
"""
    lm += gen('response', stop="\n", max_tokens=200)

    print(lm)
    return lm["response"]


async def generate_background_image_prompt(messages, scenario, style):
    # this stores the chat messages.
    messages_string = ""

    for message in messages:
        if message["role"] != "Notification":
            messages_string += message["username"] + ": " + message["message"] + "\n"

    with instruction():
        lm = gpt_instruct + f"""You a background image describer, best on the scenario, chat messages, and style, describe an image the fits perfectly, and make sure that the style is properly mentioned, use the latest chat message as reference for the location, seperate everything with commas, do not describe any people or characters in your description, keep your responses short and to the point, 1-2 sentances.
Scenario: {scenario}
Style: {style}
Start of chat history.
{messages_string}
End of chat history.
Image Description:
"""
    lm += gen('response', max_tokens=200)

    print(lm)
    return lm["response"]


# generate_background_image_prompt([{"username": "dave", "message": "I walk forward."}], "trapped in a dark dungeon.", "dark fantasy")
