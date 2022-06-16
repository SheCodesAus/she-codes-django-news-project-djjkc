from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        createstory = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = createstory[:4]
        context['all_stories'] = createstory
        return context

class UserArticlesList(generic.ListView):
    form_class = StoryForm
    context_object_name = 'article_list'
    template_name = 'userArticle.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = NewsStory.objects.all()
        return context

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return NewsStory.objects.filter(author = author_id)


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

