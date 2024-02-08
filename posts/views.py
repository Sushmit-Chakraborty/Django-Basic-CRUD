from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from django.http import HttpResponse
from .models import Post

# Create your views here.
def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form was saved")
    else:
        form = PostForm()
    
    return render(request,"addPost.html",{"form":form})

def viewPost(request):
    fetchPosts = Post.objects.all()
    for post in fetchPosts:
        print("Post id is - "+str(post.pk)+"\n"+"Post title is - "+post.postTitle+"\n"+"Post content is - "+post.postContent)
    return render(request,"viewPost.html",{"dataset":fetchPosts})

def updatePost(request,id):
    fetchPost = get_object_or_404(Post,pk=id)
    print(fetchPost.postTitle)
    form = PostForm(request.POST,instance=fetchPost)
    if form.is_valid():
        form.save()
        return HttpResponse("Record updated successfully")
    return render(request,"updateForm.html",{"form":form})

def deletePost(request,id):
    fetchPost = get_object_or_404(Post,pk=id)
    fetchPost.delete()
    return HttpResponse("Record deleted successfully")
