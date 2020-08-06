from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def home_page(request, *args, **kwargs):
      # return HttpResponse('<h1>Hi<h1/>')
      return render(request, "pages/home.html", context={}, status=200)
    

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
