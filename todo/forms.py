from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "is_done", "tags", "deadline"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})}
