from django.shortcuts import render
from django.views import View
from .models import Topic  # Import your Topic model here

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Topic, Comment
from .forms import *

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Create a login template
    success_url = reverse_lazy('topics_list')  # Specify the success URL
    
    def form_valid(self, form):
        # Perform the login and redirect to the success URL
        response = super().form_valid(form)
        return response
    
class CustomLogoutView(LogoutView):
    pass  # You can customize the logout view if needed

class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'  # Create a template for the user profile

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class TopicsListView(View):
    template_name = 'topics_list.html'  # Replace with your desired template name

    def get(self, request):
        topics = Topic.objects.all()  # Retrieve all topics from the database
        return render(request, self.template_name, {'topics': topics})

class TopicDetailView(View):
    template_name = 'topic_detail.html'  # Create a template for topic detail

    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, pk=topic_id)
        comments = Comment.objects.filter(topic=topic)
        comment_form = CommentForm()
        return render(request, self.template_name, {'topic': topic, 'comments': comments, 'comment_form': comment_form})

@method_decorator(login_required, name='dispatch')
class TopicCreateView(View):
    template_name = 'topic_create.html'
    form_class = TopicForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = self.request.user
            topic.save()
            return redirect('topics_list')
        return render(request, self.template_name, {'form': form})

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, pk=topic_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.topic = topic
            comment.save()
        return redirect('topic_detail', topic_id=topic_id)