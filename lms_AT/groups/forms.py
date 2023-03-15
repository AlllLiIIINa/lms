from django import forms

from django_filters import FilterSet

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'})
        }


class GroupCreateForm(GroupBaseForm):
    from students.models import Student
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True), required=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(GroupBaseForm.Meta):
        pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'start': ['exact'],
        }

    def clean(self):
        pass

    def clean_name(self):
        value = self.cleaned_data.get('name')

        return value.title()

    def clean_description(self):
        value = self.cleaned_data.get('description')

        return value.title()

    def clean_start(self):
        value = self.cleaned_data.get('start')

        return value
