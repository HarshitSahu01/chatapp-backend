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
        if 'key' not in request.POST:
            return JsonResponse({'msg':'Please provide a key'})
        key = request.POST['key']
        if key not in [i['key'] for i in User.objects.values('key')]:
            return JsonResponse({'msg':'Invalid Key'})
        user = User.objects.get(key=key)
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
            
            size = 20
            posts_obj = Paginator(posts, size)
            posts = posts_obj.get_page(page_num)
            postData = []
            for post in posts:
                postData.append(post.dispatch())
            return JsonResponse({
                'data':postData,
                'page':page_num,
                'total_pages':posts_obj.num_pages,
                'count':size, 
                'msg':'success'
            }, safe=False)
        
        elif type == 'create':
            if 'content' not in request.POST:
                return JsonResponse({'msg':'Please send content'})
            content = request.POST['content']
            if not content.trim():
                return JsonResponse({'msg':'Please send content'})
            group = 'main'
            if 'group' in request.POST:
                group = request.POST['group']
                if group not in [i['name'] for i in Group.objects.values('name')]:
                    return JsonResponse({'msg':'Invalid Group'})
            group = Group.objects.get(name=group)
            post = Post(content = content, group = group, user = user)
            post.save()
            return JsonResponse({'msg':'Post Created successfully'})
        
        elif type == 'groups':
            group_list = [i['name'] for i in Group.objects.values('name')]
            data = {'msg': 'success', 'data':group_list}
            return JsonResponse(data)
        return JsonResponse({'msg':'Invalid Request Type'})
