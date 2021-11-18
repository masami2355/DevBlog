from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .filters import TitleFilter

#from .models import Contact

# Create your views here.
#def index(request):
#    return render(request, 'app/index.html')

#class FormView(View):
#    def get(self, request, *args, **kargs):
#        post_data = Post.objects.oder_by('-id')
#        return render(request, 'app/form.html', {
#            'post_data': post_data
#        })

        
class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kargs):
        form = PostForm(request.POST or None)
        return render(request, 'app/form.html', {
            'form': form
        })
    
    #form.htmlのボタンが押されたら下記の関数を発動    
    def post(self, request, *args, **kargs):
        form = PostForm(request.POST or None)
        
        if form.is_valid():
            post_data = Post()
            #post_data.author = request.user
            post_data.categoly = form.cleaned_data['categoly']
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save() #この関数でデータベースに保存する
            return redirect('detail', post_data.id)
        
        return render(request, 'app/form.html', {
            'form': form
        })



#class HomeView(ListView):
#    model = Post
#    template_name = 'app/index.html'

class IndexView(ListView):
    #template_name = 'app/index.html'
    model = Post     
    #paginate_by = 2
       
    def get(self, request, *args, **kargs):
    #def listing(request):    
        post_data = Post.objects.order_by('-id')
        #post_data = Post.objects.all()
        paginator = Paginator(post_data, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        #検索フォームテスト中
        #rqset = Post.objects.all.filter(title__exact='')
        rqset = post_data
        myFilter = TitleFilter(request.GET, queryset=rqset)
        post_data = myFilter.qs

        return render(request, 'app/post_list.html', {
            'post_data': post_data,
            'page_obj': page_obj,
            'myFilter': myFilter
        })
        
 
    
     
#    def paginate_queryset(request, queryset, count):
#        """Pageオブジェクトを返す。
#
#        ページングしたい場合に利用してください。
#
#        countは、1ページに表示する件数です。
#        返却するPgaeオブジェクトは、以下のような感じで使えます。
#
#            {% if page_obj.has_previous %}
#            <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
#            {% endif %}
#
#        また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。
#
#        """
#        paginator = Paginator(queryset, count)
#        page = request.GET.get('page')
#        try:
#            page_obj = paginator.page(page)
#        except PageNotAnInteger:
#            page_obj = paginator.page(1)
#        except EmptyPage:
#            page_obj = paginator.page(paginator.num_pages)
#        return page_obj


#    def post_index(request):
#        #model = Post
#        #paginate_by = 2
#        post_list = Post.objects.all()
#        page_obj = paginate_queryset(request, post_list, 1)
#        context = {
#            'post_list': page_obj.object_list,
#            'page_obj': page_obj,
#        }
#        return render(request, 'app/index.html', context)
    
   
class BlogDetailView(DetailView):
    def get(self, request, *args, **kargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'post_data': post_data
        })    
    
class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'content': post_data.content
            }
        )
        return render(request, 'app/form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kargs):
        form = PostForm(request.POST or None)
        
        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save() #この関数でデータベースに保存する
            return redirect('detail', self.kwargs['pk'])
        
        return render(request, 'app/form.html', {
            'form': form
        })

        
        
    
class PostDeleteView(LoginRequiredMixin, View):    
    def get(self, request, *args, **kargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/delete.html', {
            'post_data': post_data
        })    
        
        
    def post(self, request, *args, **kargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        
        return redirect('home')
        
