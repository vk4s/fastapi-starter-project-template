import uvicorn


#  main function
if __name__ == '__main__':
    #  'app.app:app'

    #  first app is the folder name, where your code is stored
    #  second app is app.py file inside app folder
    #  third app is the name of fastapi instance: app=FastAPI(0)

    uvicorn.run('app.app:app', host='0.0.0.0', port=8000, reload=True)
