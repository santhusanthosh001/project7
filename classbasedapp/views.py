from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class GetInput(View):
    def get(self, request):
        return render(request, 'getinput.html')


class PostInput(View):
    def get(self, request):
        return render(request, 'postinput.html')


class Add(View):
    def get(self, request):
        i = int(request.GET['t1'])
        j = int(request.GET['t2'])
        k = i + j
        con_dic={'res': k}
        return render(request,'output.html',context=con_dic)

    def post(self, request):
        i = int(request.POST['t1'])
        j = int(request.POST['t2'])
        k = i + j
        con_dic = {'res': k}
        return render(request,'output.html',context=con_dic)




# Create your views here.
