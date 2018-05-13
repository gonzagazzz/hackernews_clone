from django.shortcuts import render
from .forms import PostForm
from django.views.generic import View
from posts.models import Article

class PostFormView(View):
    form_class = PostForm
    template_name = 'post_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # authenticate user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
        	form.save()
        	return redirect('../')

        return render(request, self.template_name, {'form': form})

def post(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'post.html', {'article': article})