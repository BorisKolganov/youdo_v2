# coding=utf-8
from django import forms

from works.models import Employee, ServiceType


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['about', 'skills', 'experience']

    types = forms.ModelMultipleChoiceField(queryset=ServiceType.objects.all(), label=u'Виды работ')

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['types'] = [t.pk for t in kwargs['instance'].servicetype_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            instance.servicetype_set.clear()
            for type in self.cleaned_data['types']:
                instance.servicetype_set.add(type)

        self.save_m2m = save_m2m
        if commit:
            instance.save()
            self.save_m2m()

        return instance
