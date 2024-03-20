![00029-3041689300](https://github.com/jediknight813/TextGenServer/assets/17935336/d6761b03-2721-4299-8467-2bf6355698c3)
# TextGen Server

The server for the TextGen client, it does require a chat-gpt and dreamstudio api to run.

## setup

* rename .env.example -> .env
* put in your api keys
```
OPENAI_API_KEY=
USE_LOCAl_TEXT_GEN=
STABILITY_API_KEY=
LOCAL_API_URL=
```

* install the requirements
```
pip install -r requirements.txt
```
* run the server
```
python scripts/server.py
```
* run the client
https://github.com/jediknight813/TextGenClient
