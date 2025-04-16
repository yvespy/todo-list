from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at")

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("home")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("home")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("home")

class TaskToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("home")

class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tag_list")

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tag_list")

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"