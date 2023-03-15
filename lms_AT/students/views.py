from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentCreateForm
from .forms import StudentFilterForm
from .forms import StudentUpdateForm
from .models import Student


def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(request, 'students/list.html', {'filter_form': filter_form})


def detail_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create_students(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


def update_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    form = StudentUpdateForm(instance=student)
    return render(request, 'students/update.html', {'form': form, 'student': student})


def delete_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
