from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()

    if request.method == "POST":
        new_title = request.POST.get("title")
        Todo.objects.create(title=new_title)
        return redirect("index")

    return render(request, "todo/index.html", {"todos": todos})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("index")
