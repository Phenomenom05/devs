from django.forms import ModelForm
from .models import Project, Skill, Profile, Message, Comment
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "featured_image", "demo_link", "source_code", "vote_ratio", "vote_count",
                  "tags"]

        widgets = {
            "tags": forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "username", "email", "password1"]

        labels = {
            "first_name": "Name"
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["title", "name", "email", "username", "headline", "bio", "location", "profile_image", "social_github",
                  "social_linkedin", "social_website", "social_x"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})




class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "subject", "body"]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "input input--textarea"})










