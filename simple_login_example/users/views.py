from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User

# Create your views here.

def login(request):
    context = {
        'method': request.method,
        'is_valid': True
    }

    if (request.method == 'GET'):
        return render(request, 'users/login.html', context)

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)

            response = redirect('pages:index')
            response.set_cookie('is_login', True)
            response.set_cookie('username', user.username)
            response.set_cookie('password', user.password)

            return response

        except User.DoesNotExist: #유저의 object를 가져올 수 없는 경우 = DB에 값이 저장x,login 불가
            context['is_valid'] = False
        return render(request, 'users/login.html', context)


def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')


def index(request,):
    return render(request, 'index.html')


def logout(request):
    response = redirect('pages:index')
    response.delete_cookie('is_login')
    response.delete_cookie('username')
    response.delete_cookie('password')

    return response



def signup(request):
    context = {
        'blank' : False,
        'exist' : False
    }

    template_name = "users/signup.html"

    if request.method == "GET":
        return render(request, template_name,context)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #빈칸 여부 확인 
        if username == '' or password == '':
           context['blank'] = True
           return render(request, template_name, context)

        #이미 존재하는 아이디인지 확인하고 
        exist = User.objects.filter(username=username).exists()

        if exist:
            context['exist'] = exist
            return render(request, template_name, context)

    
        #성공
        User.objects.create(username=username,password=password)
        return redirect('users:login') #login 화면으로 이동

    