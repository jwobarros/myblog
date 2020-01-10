from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post, Tag, Subscriber
from blog.forms import CommentForm

class HomePageView(ListView):

    template_name = "home.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            objects = self.model.objects.all()
        else:
            objects = self.model.objects.filter(public=True)

        title = self.request.GET.get('title', '')
        tag = self.request.GET.get('tag', '')

        if title:
            objects = objects.filter(title__icontains = title)
        if tag:
            objects = objects.filter(tags__name = tag)
   
        return objects


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.all()
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'tags': tags
                                        })

@csrf_exempt
def subscribe_view(request):
    if request.method == "POST" and request.is_ajax():

        email = request.POST.get('email', None)
        
        if not Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.create(email=email)

            data = { 'registered': True }
        else:
            data = { 'registered': True }

        return JsonResponse(data)
    raise Http404("Página não encontrada.")