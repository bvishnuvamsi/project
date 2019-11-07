from django.shortcuts import render

from .models import Post
# Create your views here.
def view(request):
    posts = Post.objects
    data_list = list(posts.values())
    print(data_list)
    new_list = sorted(data_list, key=lambda i: i['id'], reverse=1)
    print(new_list)
    dict = new_list[0]
    return render(request, 'post/view.html', {'user': dict['user'], 'imageurl': dict['image'], 'text': dict['text'], 'time': dict['time']})


