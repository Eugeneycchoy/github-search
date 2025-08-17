import requests
from datetime import datetime

class GitHubService:
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        # You can add GitHub token here for higher rate limits
        # self.token = "your_github_token_here"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Search-App'
        }
    
    def get_user(self, username):
        """
        Fetch GitHub user data by username
        Returns user data or None if not found
        """
        try:
            url = f"{self.BASE_URL}/users/{username}"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                user_data = response.json()
                return self._format_user_data(user_data)
            elif response.status_code == 404:
                return None
            else:
                # Handle other errors (rate limit, server errors, etc.)
                print(f"GitHub API error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
    
    def _format_user_data(self, raw_data):
        """
        Format the raw GitHub API response into a clean structure
        """
        # Format join date
        created_at = datetime.strptime(raw_data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        formatted_date = created_at.strftime('%d %b %Y')
        
        return {
            'name': raw_data.get('name') or raw_data['login'],
            'login': raw_data['login'],
            'avatar_url': raw_data['avatar_url'],
            'bio': raw_data.get('bio') or 'This profile has no bio',
            'public_repos': raw_data['public_repos'],
            'followers': raw_data['followers'],
            'following': raw_data['following'],
            'location': raw_data.get('location') or 'Not Available',
            'blog': raw_data.get('blog') or 'Not Available',
            'twitter_username': raw_data.get('twitter_username') or 'Not Available',
            'company': raw_data.get('company') or 'Not Available',
            'created_at': formatted_date,
            'html_url': raw_data['html_url']
        }