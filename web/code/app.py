from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates

# instance (object) of FastAPI class
fastapiInstance = FastAPI()

# templates = Jinja2Templates(directory='templates/')


# routes
@fastapiInstance.get('/', tags=['index'])
async def index(request: Request):
    return "Hello"
    # return templates.TemplateResponse('home.html', context= {'request': request})


@fastapiInstance.get('/add', tags=['add'])
async def add(request: Request, num1, num2) -> dict:
    print(num1, num2)
    sum_of_numbers = int(num1) + int(num2)

    return {
        'sum': sum_of_numbers
    }
