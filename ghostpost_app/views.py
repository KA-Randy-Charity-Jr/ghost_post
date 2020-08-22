from django.shortcuts import render
from ghostpost_app.models import Ghostpost
from ghostpost_app.forms import Createghostpost, Upvote
from django.shortcuts import render,HttpResponseRedirect,reverse

# Create your views here.
def index(request):
    ghostposts = Ghostpost.objects.all().order_by("-id")
    return render(request, "index.html", {"ghostposts": ghostposts})
    
def newpost_view(request):
    if request.method == "POST":
        boaststat = False
        form = Createghostpost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get("isboast") == '1':
                boaststat = True
            else:
                bootstat = False    
               
            Ghostpost.objects.create(text=data.get("text"), boasts=boaststat)
            return HttpResponseRedirect(reverse("homepage"))
    form = Createghostpost()
    return render(request, "newpost.html", {"form": form})
    
def upvote(request, post_id):
    if request.method == 'GET':
        post = Ghostpost.objects.get(id=post_id)
        post.upvotes += 1
        post.save()
        return HttpResponseRedirect(reverse("homepage"))
    
def downvote(request, post_id):
    if request.method == 'GET':
        post = Ghostpost.objects.get(id=post_id)
        post.downvotes = post.downvotes-1
        post.save()
        return HttpResponseRedirect(reverse("homepage"))

def boasts_view(request):
    posts = Ghostpost.objects.all().order_by("-id")
    return render(request,"boast.html",{"posts":posts})

def roasts_view(request):
    posts = Ghostpost.objects.all().order_by("-id")
    return render(request,"roast.html",{"posts":posts})

def upvote_view(request):
    posts = Ghostpost.objects.all().order_by("-upvotes")
    return render(request,"upvote.html",{"posts":posts})


def delete_posts(request):
    pass          