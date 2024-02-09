from django import forms


class createNewTask(forms.Form):
    title = forms.CharField(label='titulo de la tarea', max_length=100)
    description = forms.CharField(widget=forms.Textarea())


class createNewProject(forms.Form):
    name = forms.CharField(label='nombre de la proyecto', max_length=100)
