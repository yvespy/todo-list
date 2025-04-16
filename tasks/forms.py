from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple(),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
