from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone # 현재 시각을 나타내는 패키지
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    # 찾을 수 없다는 예외 처리 가능
    # pk는 관계형 데이터베이스의 식별자 = primary key
    return render(request,'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() #save 안하면 적용 안된다
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete() # delete 메서드
    return redirect('home')