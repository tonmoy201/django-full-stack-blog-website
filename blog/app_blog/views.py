from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy
from django.shortcuts import HttpResponseRedirect

#class based view
from django.views.generic import CreateView,UpdateView, ListView,DetailView,DeleteView
from django.views.generic.base import TemplateView
#model from app_blog
from  app_blog.models import Blog,Comment,Like

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from app_blog.forms import CommentForm
# Create your views here.
class BlogList(ListView):
    model=Blog
    template_name="app_blog/blog_list.html"
    context_object_name='blogs'

class CreateBlog(LoginRequiredMixin,CreateView):
    model=Blog
    template_name="app_blog/create_blog.html"
    fields=('blog_title','blog_content','blog_img',)

    def form_valid(self,form):
        blog_obj=form.save(commit=False)
        blog_obj.author_name=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug=title.replace(' ','-')+"_"+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)

    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:blog_details',kwargs={'slug':slug}))
    diction={"blog":blog,'form':form}
    return render(request,'app_blog/details_blog.html',context=diction)





