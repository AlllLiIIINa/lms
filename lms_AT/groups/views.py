from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from groups.forms import GroupCreateForm
from groups.forms import GroupFilterForm
from groups.forms import GroupUpdateForm
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all()

    filter_form = GroupFilterForm(data=request.GET, queryset=groups)
    return render(request, 'groups/list.html', {'filter_form': filter_form})


def detail_groups(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_groups(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = GroupCreateForm()
    return render(request, 'groups/create.html', {'form': form})


def update_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = GroupUpdateForm(instance=group)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
