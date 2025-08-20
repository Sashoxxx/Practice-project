from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, "todo/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")
    template_name = "todo/create_update_form.html"
    form_type = "Create"
    verbose_name = "Task"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")
    template_name = "todo/create_update_form.html"
    form_type = "Update"
    verbose_name = "Task"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verbose_name"] = self.model._meta.verbose_name.title()
        context["back_url"] = self.request.META.get('HTTP_REFERER')
        return context


def toggle_task_status(request, pk: int):
    task = get_object_or_404(Task, id=pk)

    task.is_done = not task.is_done
    task.save()

    return redirect('todo:index')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tags-list")
    template_name = "todo/create_update_form.html"
    form_type = "Create"
    verbose_name = "Tag"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tags-list")
    template_name = "todo/create_update_form.html"
    form_type = "Update"
    verbose_name = "Tag"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:tags-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verbose_name"] = self.model._meta.verbose_name.title()
        context["back_url"] = self.request.META.get('HTTP_REFERER')
        return context
