from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("App is working")

def chat(request):
    return render(request, 'chat/index.html')

@csrf_exempt
def apis(request, type):
    if request.method == 'POST':
        print(request.POST) 
        try:
            
            key = request.POST['key']
            user = User.objects.filter(key=key)
            if len(user) < 1:
                return JsonResponse({'msg':'invalid key'})
        except:
            pass
        if type == 'read':
            page_num, group = 1, 'main'
            if 'page' in request.POST:
                page_num = int(request.POST['page'])
            if 'group' in request.POST:
                group = request.POST['group']
                group_list = [i['name'] for i in Group.objects.values('name')]
                if group not in group_list:
                    return JsonResponse({'msg': 'invalid group'})
                
            posts = Post.objects.filter()
            posts = posts.order_by("-date").all()
            
            posts_obj = Paginator(posts, 50)
            posts = posts_obj.page(page_num)
            postData = []
            for post in posts:
                postData.append(post.dispatch())
            return JsonResponse({'data':postData, 'page':page_num, 'count':20, 'msg':'success'}, safe=False)
        
        elif type == 'create':
            if 'content' not in request.POST:
                return JsonResponse({'msg':'Please send content'})
            content = request.POST['content']
            group = 'main'
            if 'group' in request.POST:
                group = request.POST['group']
            post = Post(content = content, group = group, user = user)
            post.save()
            return JsonResponse({'msg':'Post Created successfully'})
        
        elif type == 'groups':
            group_list = [i['name'] for i in Group.objects.values('name')]
            data = {'msg': 'success', 'data':group_list}
            print(data)
            return JsonResponse(data)
        return JsonResponse({'msg':'Invalid Request Type'})
    
    return JsonResponse({'msg':'Please use POST Method'})