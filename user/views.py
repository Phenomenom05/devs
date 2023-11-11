from django.shortcuts import render, redirect
from .models import Project, Profile, Tag, Comment
from .forms import ProjectForm, RegisterForm, SkillForm, ProfileForm, MessageForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import Search_project, Search_profile, Paginate_project, Paginate_profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# render all projects
def project(request):
    project, searchQuery = Search_project(request)
    result = 3
    project, custom_range = Paginate_project(request, project, result)


    context = {'projects': project, 'searchQuery': searchQuery, 'custom_range': custom_range}
    return render(request, "user/project.html", context)


# Crud: Create for project
@login_required(login_url="login/")
def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user.profile
            user.save()
            return redirect("projects")
    context = {"forms": form}
    return render(request, 'user/projectform.html', context)


# Crud: Update for project
@login_required(login_url="login/")
def update_project(request, pk):
    project = request.user.profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {'forms': form}
    return render(request, 'user/projectform.html', context)


# Crud: Delete for project
@login_required(login_url="login/")
def delete_project(request, pk):
    project = request.user.profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("account")
    context = {"project": project}
    return render(request, "user/projectdelete.html", context)


# single project
def single_project(request, pk):
    sproject = Project.objects.get(id=pk)
    all_comment = sproject.comment_set.all()
    form = CommentForm()
    context = {"project": sproject, 'comments': all_comment, 'form': form}
    return render(request, "user/single-project.html", context)


# Crud: Create for skill
@login_required(login_url="login/")
def create_skill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            return redirect("account")
    context = {"forms": form}
    return render(request, "user/skillform.html", context)


# Crud: Update for skill
@login_required(login_url="login/")
def update_skill(request, pk):
    skill = request.user.profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {"forms": form}
    return render(request, "user/skillform.html", context)


# Crud: Delete for skill
@login_required(login_url="login/")
def delete_skill(request, pk):
    skill = request.user.profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect("account")
    context = {'skill': skill}
    return render(request, 'user/skilldelete.html', context)


def profile(request):
    profile, searchQuery = Search_profile(request)
    result = 3
    profile, custom_range = Paginate_profile(request, profile, result)
    context = {"profiles": profile, 'searchQuery': searchQuery, 'custom_range': custom_range}
    return render(request, "user/profiles.html", context)


# Single project
def single_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkill = profile.skill_set.exclude(description__exact="")
    otherSkill = profile.skill_set.filter(description="")
    projects = profile.project_set.all()
    context = {'profile': profile, 'topSkill': topSkill, 'otherSkill': otherSkill, 'projects': projects}
    return render(request, "user/single-profile.html", context)




# User login

def login_page(request):
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is not correct")


    return render(request, 'user/login.html')


# Register user
def register_page(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect("account")
        else:
            messages.error(request, "An error occurred please try again")

    context = {'form': form}
    return render(request, 'user/signup.html', context)


# User logout
@login_required(login_url="login/")
def logout_page(request):
    logout(request)
    return redirect("login")


# User account
@login_required(login_url="login/")
def Account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'user/account.html', context)

# Edit account
@login_required(login_url="login/")
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {"forms": form}

    return render(request, 'user/profileform.html', context)


@login_required(login_url="login/")
def delete_account(request):
    profile = request.user.profile
    if request.method == "POST":
        profile.delete()
        return redirect('profiles')
    context = {"profile": profile}
    return render(request, 'user/accountdelete.html', context)



# Inbox
@login_required(login_url="login/")
def Inbox(request):
    profile = request.user.profile
    messageRequest = profile.messages.all()
    is_read = messageRequest.filter(is_read=False).count()

    context = {'messageRequest': messageRequest, 'is_read': is_read}

    return render(request, 'user/inbox.html', context)


def single_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {"message": message}

    return render(request, 'user/message.html', context)


def send_message(request, pk):
    form = MessageForm()
    recipient = Profile.objects.get(id=pk)
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.username
                print(message)
                message.save()
            else:
                message.save()
            return redirect("single-profile", recipient.id)

    context = {"form": form, "recipient": recipient}
    return render(request, 'user/messageform.html', context)

@login_required(login_url="login/")
def delete_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    message.delete()
    return redirect("inbox")


# Comment section
@login_required(login_url="login")
def Comments(request, pk):
    sender = request.user.profile
    recipient = Project.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.sender = sender
            comment.recipient = recipient
            comment.save()
            return redirect("single-project", recipient.id)

        context = {"form": form}


        return render(request, 'user/single-project.html', context)


@login_required(login_url="login/")
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    sender = request.user.profile
    comment_selected = sender.comment_set.get(id=pk)
    comment_selected.delete()
    return redirect("single-project", comment.recipient.id)







