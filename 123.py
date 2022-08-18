import requests 

# регистрация
# register = {'username' : 'sed' , 'email' :'sed@bk.ru' , 'password' : '123' }
# response = requests.post('http://127.0.0.1:8000/api/chat/signup/' , data = register)

# авторизация
# login = {'username' : 'sed' , 'email' :'sed@bk.ru' , 'password' : '123' }
# response = requests.post('http://127.0.0.1:8000/auth/token/login/' , data = login)

# получение сообщений
# название комнаты в формате ?room=user1-user2
headers = {'Authorization': "Token " + '6c20142ed91f23c199f82431df52c07b985fc122'}
# response = requests.get("http://127.0.0.1:8000/api/chat/dialog/?room=sdfy-sed" , headers=headers)

# создание диалога
# response = requests.post('http://127.0.0.1:8000/api/chat/room/' , data={
#     'first_user' : 'sdfy' , 
#     'second_user' : 'armeno'
# } , headers=headers)


# загрузка всех диалогов для определнного юзера
response = requests.get('http://127.0.0.1:8000/api/chat/room/?username=sdfy' , headers=headers)


print(response.text)