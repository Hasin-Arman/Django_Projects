from django.shortcuts import render,redirect
from book.forms import Book_Form
from book.models import BookModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#    return render(request,'home.html')

class MyTemplateView(TemplateView):
   template_name='home.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context ={'name':'chayan','age':21} 
      print(context)
      context.update(kwargs)
      return context
   
# def store_book(request):
#    if request.method == 'POST':
#       form = Book_Form(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect('show')
#    else:
#       form = Book_Form()
#    return render(request,'store_book.html',{'form':form})


# class Book_Form_view(FormView):
#    template_name='store_book.html'
#    form_class=Book_Form
#    success_url=reverse_lazy('show')
   
#    def form_valid(self, form):
#       form.save()
#       return redirect('show')
   
class Book_Form_view(CreateView):
   model=BookModel
   template_name='store_book.html'
   form_class=Book_Form
   success_url=reverse_lazy('show')

# def show_book(request):
#    books=BookModel.objects.all()
#    return render(request,'show_book.html',{'books':books})

class BookListView(ListView):
   model=BookModel
   template_name='show_book.html'
   context_object_name='books' 
   # def get_queryset(self):
   #    return BookModel.objects.filter(id=1)
   # def get_context_data(self, **kwargs):
   #    context = super().get_context_data(**kwargs)
   #    context = {'books': BookModel.objects.all().filter(author='chayan')}
   #    return context
   # ordering=['-id']
   # def get_template_names(self):
   #    pass
   
class BookdetailsView(DetailView):
   model=BookModel
   template_name='bookdetails.html'
   context_object_name='book'
   pk_url_kwarg='serial'
   
   

def edit_book(request,id):
   book=BookModel.objects.get(pk=id)
   form = Book_Form(instance=book)
   if request.method == 'POST':
      form = Book_Form(request.POST,instance=book)
      if form.is_valid():
         form.save()
         return redirect('show')
   return render(request,'store_book.html',{'form':form})

class Book_Update_View(UpdateView):
   model=BookModel
   template_name='store_book.html'
   form_class=Book_Form
   success_url=reverse_lazy('show')
   
class Book_Delete_View(DeleteView):
   model=BookModel
   template_name='del_conf.html'
   success_url=reverse_lazy('show')

# def delete_book(request,roll):
#    book = BookModel.objects.get(pk=roll).delete()
#    return redirect('show')
   
   
   