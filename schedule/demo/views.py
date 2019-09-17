from django.shortcuts import render,redirect
from demo.models import DemoModel
# Create your views here.
def demo(request):
    all_todo=DemoModel.objects.all()
    false_todo=DemoModel.objects.filter(todo_statu=False)
    true_todo=DemoModel.objects.filter(todo_statu=True)
    print([todo.id for todo in all_todo])
    return render(request,'demo.html',{'falsetodo':false_todo,'truetodo':true_todo})

def check_todo(request):
# http://127.0.0.1:8000/check/id=?
    id=request.GET.get('id')
    print('id:',id)
    todo=DemoModel.objects.filter(id=id).first()

    if todo:
        todo.todo_statu=not todo.todo_statu
        todo.save()
    else:
        pass
    return redirect(to='/')


def delete_(request):
    id = request.GET.get('id')
    print('id:', id)
    todo = DemoModel.objects.filter(id=id).first()

    if todo:
        todo.delete()
    else:
        pass
    return redirect(to='/')

def add_todo(request):
    title=request.POST.get('title')
    todo=DemoModel()
    todo.title=title
    todo.save()
    return redirect('/')

