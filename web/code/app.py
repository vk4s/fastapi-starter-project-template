from fastapi import FastAPI

from code.data import get_data

# import additional code from other modules
from code.database.users import UsersModel


# instance (object) of FastAPI class
fastapiInstance = FastAPI()

# routes
@fastapiInstance.get('/', tags=['index'])
async def index() -> dict:
    return {'Hello': 'world'}


@fastapiInstance.get('/about', tags=['about'])
async def about() -> dict:
    msg = 'Hi, I am V. I am a web developer.'
    profilePic = 'https://images.pexels.com/photos/1677107/pexels-photo-1677107.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260'  # noqa: E501

    return {
        'msg': msg,
        'profile_picture': profilePic
    }


@fastapiInstance.get('/todos', tags=['todos'])
async def todos() -> list:

    todos = get_data(filename='./code/data.json')
    print(todos)

    return todos


