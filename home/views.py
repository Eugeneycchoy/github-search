from django.shortcuts import render
from .service import GitHubService

# Create your views here.
def home(request):
    username = request.GET.get('username', '').strip()  # Strip whitespace
    github_service = GitHubService()
    context = {'username': username}

    if username:
        if not username.isalnum():  # Validate username
            context['error'] = "Invalid username. Please use only letters and numbers."
        else:
            user_data = github_service.get_user(username)
            if user_data:
                context['user_data'] = user_data
            else:
                context['error'] = "User not found or API error occurred."
    else:
        context['error'] = "Please enter a username."

    return render(request, 'index.html', context)