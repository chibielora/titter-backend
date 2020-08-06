import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def home_page(request, *args, **kwargs):
      # return HttpResponse('<h1>Hi<h1/>')
      return render(request, "pages/home.html", context={}, status=200)
    
def post_list_view(request, *args, **kwargs):
    """REST API VIEW return Json data, consume by react"""
    list = Post.objects.all()
    post_list = [{"id": post.id, "content": post.content, "likes": random.randint(0, 14325357)} for post in list]
    data = {
        "isUser": False,
        "response": post_list
    }
    return JsonResponse(data)

def post_detail(request, post_id, *args, **kwargs):
    """REST API VIEW return Json data, consume by react"""
    data = {
        "id": post_id,

    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
      

    return JsonResponse(data, status=status)
  # content_type='application/json'
