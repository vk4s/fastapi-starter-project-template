from fastapi import FastAPI
# from fastapi.templating import Jinja2Templates

# instance (object) of FastAPI class
fastapiInstance = FastAPI()

# templates = Jinja2Templates(directory='templates/')


# routes
@fastapiInstance.get('/')
async def index():
    return "Hello"
    # return templates.TemplateResponse('home.html', context= {'request': request})


@fastapiInstance.get('/add')
async def add(num1, num2):
    sum_of_numbers = int(num1) + int(num2)
    return sum_of_numbers
