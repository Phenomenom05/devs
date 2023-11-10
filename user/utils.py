from .models import Project, Profile, Tag, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def Search_project(request):
    searchQuery = ""
    if request.GET.get("searchQuery"):
        searchQuery = request.GET.get("searchQuery")
    tag = Tag.objects.filter(name__icontains=searchQuery)
    project = Project.objects.distinct().filter(
        Q(title__icontains=searchQuery) | Q(description__icontains=searchQuery) | Q(owner__name__icontains=searchQuery)
        | Q(tags__in=tag))


    return project, searchQuery



def Search_profile(request):
    searchQuery = ""
    if request.GET.get("searchQuery"):
        searchQuery = request.GET.get("searchQuery")
    skill = Skill.objects.filter(name__icontains=searchQuery)
    profile = Profile.objects.distinct().filter(
        Q(name__icontains=searchQuery) | Q(username__icontains=searchQuery) | Q(title__icontains=searchQuery) | Q(location__icontains=searchQuery)
        | Q(skill__in=skill))


    return profile, searchQuery


def Paginate_project(request, project, result):
    page = request.GET.get("page")
    paginator = Paginator(project, result)
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        project = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        project = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index)


    return project, custom_range





def Paginate_profile(request, profile, result):
    page = request.GET.get("page")
    paginator = Paginator(profile, result)
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profile = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profile = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)


    return profile, custom_range