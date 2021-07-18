from django.shortcuts import render, redirect
from django.http import HttpResponse
from cj_app.models import CjCategory, CjPost
from cj_app.forms import CjCategoryForm, CjPostForm

def index(request):
    return render(request, "pages/home.html")

#category
def categories(request):
    
    data = {
        "categories": CjCategory.objects.all()
    }
    return render(request, "pages/categories/category_list.html", data)

def category_new(request):
    form = CjCategoryForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cj:category_list")
        except:
            return HttpResponse("Error creating new category!")

    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, "pages/categories/category_form.html", data)

def category_detail(request, category_id):
    try:
        category = CjCategory.objects.get(pk=category_id)
    except:
        print("error")
        return HttpResponse("That category doesn't exist!")
    
    data = {
        "category": category
    }
    return render(request, "pages/categories/category_detail.html", data)

def category_edit(request, category_id):
    try:
        category = CjCategory.objects.get(pk=category_id)
    except:
        print("error")
        return HttpResponse("That category doesn't exist!")
    
    form = CjCategoryForm(request.POST or None, instance=category)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cj:category_detail", category_id=category_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error updating new category!")

    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "pages/categories/category_form.html", data)

def category_delete(request, category_id):
    try:
        category = CjCategory.objects.get(pk=category_id)
        category.delete()
    except:
        return HttpResponse(f"A category with id {category_id} doesn't exist!")

    return redirect("cj:category_list")

#posts
def posts(request, category_id):
    try:
        category = CjCategory.objects.get(pk=category_id)
    except:
        print("error")
        return HttpResponse("That category doesn't exist!")
    
    data = {
        "category": category
    }
    return render(request, "pages/posts/post_list.html", data)

def post_new(request, category_id):
    try:
        category = CjCategory.objects.get(pk=category_id)
    except:
        print("error")
        return HttpResponse("That category doesn't exist!")

    form = CjPostForm(request.POST or None, initial={"category": category})

    if request.method == "POST":
        try:
            form.save()
            return redirect("cj:post_list", category_id=form.instance.category.id)
        except Exception as e:
            print(e)
            return HttpResponse("Error adding new post") 

    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, "pages/posts/post_form.html", data)

def post_detail(request, category_id, post_id):
    try:
        post = CjPost.objects.get(pk=post_id)
    except:
        print("error")
        return HttpResponse("That post doesn't exist!")
    
    data = {
        "post": post
    }
    return render(request, "pages/posts/post_detail.html", data)

def post_edit(request, category_id, post_id):
    try:
        post = CjPost.objects.get(pk=post_id)
    except:
        print("error")
        return HttpResponse("That post doesn't exist!")

    form = CjPostForm(request.POST or None, instance=post)

    if request.method == "POST":
        try:
            form.save()
            return redirect("cj:post_detail", category_id=category_id, post_id=post_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error editing post") 

    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "pages/posts/post_form.html", data)


def post_delete(request, category_id, post_id):
    try:
        post = CjPost.objects.get(pk=post_id)
        post.delete()
    except:
        return HttpResponse(f"A post with id {post_id} doesn't exist!")

    return redirect("cj:post_list", category_id = category_id)
