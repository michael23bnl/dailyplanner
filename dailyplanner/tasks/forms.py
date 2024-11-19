from django import forms
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'planned_date']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'planned_date': 'Дата выполнения',
        }
        widgets = {
            'planned_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['planned_date'].required = False
