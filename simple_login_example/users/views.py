from django.shortcuts import render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def login(request):
    user_data = {
        'username': 'python',
        'password': 'django'
    }

    if (request.method == 'GET'):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username is None:
            return HttpResponse('유저 아이디를 입력해주세요')
        if password is None:
            return HttpResponse('유저 비밀번호를 입력해주세요')

        if (username != user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')

        if (password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
        
        return render(request, 'users/login.html')
    
    return HttpResponse()

def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')
