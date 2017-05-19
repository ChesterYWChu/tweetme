from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tweet

# Create your views here.

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	# return Tweet.objects.get(id=pk)
	# 	return get_object_or_404(Tweet, pk=pk)

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context
	

def tweet_detail_view(request, pk=None):
	# obj = Tweet.objects.get(pk=pk)
	obj = get_object_or_404(Tweet, pk=pk)
	print(obj)
	context = {
		"object": obj
	}
	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request, id=1):
# 	queryset = Tweet.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj.content)
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "tweets/list_view.html", context)