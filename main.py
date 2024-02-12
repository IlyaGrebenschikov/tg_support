import requests
import uvicorn

from fastapi import FastAPI, Request

from settings import get_settings


app = FastAPI()


def set_whook():
    whook = get_settings().env.WHOOK
    bot_token = get_settings().env.BOT_TOKEN
    try:
        r = requests.get(f'https://api.telegram.org/bot{bot_token}/setWebhook?url=https://{whook}/')
        print(r.json())
    except Exception as ex:
        raise ex
    
    
@app.post('/')
async def first(request: Request) -> dict:
    print(request.json())
    return {
        'hello': "world"
    }


if __name__ == '__main__':
    set_whook()
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
    