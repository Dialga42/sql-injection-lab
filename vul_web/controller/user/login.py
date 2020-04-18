from django.http import HttpResponse
import model.user.login as entity

def login(request):
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        n, pwd = entity.login(name, password)
        if n is None:
            return HttpResponse("Unknown User Name")
        print('name %s password %s' % (n, pwd))
    return HttpResponse("Hello %s!" % (n))

def login_sec(request):
    return HttpResponse("Sign up")