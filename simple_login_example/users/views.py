from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    user_data = {
        'username': 'jinhyeok',
        'password': '12345678'
    }

    if (request.method == 'GET'):
        username = request.GET['username']
        if (username != user_data['username']):
            HttpResponse('유저 아이디가 없습니다.')

        password = request.GET['password']
        if (password != user_data['password']):
            HttpResponse('유저 비밀번호가 올바르지 않습니다.')
        
        return HttpResponse('로그인 성공!')
    
    return HttpResponse()

def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')
