from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import User, Tweet

# Create your views here.
def home(request):
  return HttpResponse("yo")

def tweet(request, tweet_id):
  try:
    tweet = Tweet.objects.get(pk=tweet_id)
  except Tweet.DoesNotExist:
    raise Http404("Tweet does not exist")
  return render(request, 'feed/tweet.html', {'tweet':tweet, 'replies':tweet.replies.all(), 'retweets':tweet.retweets.all()})

