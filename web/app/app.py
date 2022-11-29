from fastapi import FastAPI

from app.data import get_data

# instance (object) of FastAPI class
app = FastAPI()

# routes
@app.get('/', tags=['index'])
async def index() -> dict:
    return {'Hello': 'world'}


@app.get('/about', tags=['about'])
async def about() -> dict:
    msg = 'Hi, I am V. I am a web developer.'
    profilePic = 'https://images.pexels.com/photos/1677107/pexels-photo-1677107.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260'  # noqa: E501

    return {
        'msg': msg,
        'profile_picture': profilePic
    }


@app.get('/todos', tags=['todos'])
async def todos() -> list:

    todos = get_data(filename='./app/data.json')
    print(todos)

    return todos


