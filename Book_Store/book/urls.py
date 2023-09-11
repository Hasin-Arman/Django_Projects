from django.urls import path
# from book.views import home,store_book,show_book,edit_book,delete_book
from . import views
urlpatterns = [
    path('',views.TemplateView.as_view(template_name="home.html"),name="homepage"),
    # path('<int:roll>/',views.MyTemplateView.as_view(),{'author':'Arman'},name="homepage"),
    # path('store_books/',views.store_book,name="store"),
    path('store_books/',views.Book_Form_view.as_view(),name="store"),
    path('show_books/',views.BookListView.as_view(),name="show"),
    path('detail_books/<int:serial>',views.BookdetailsView.as_view(),name="details"),
    # path('edit_book/<int:id>',views.edit_book,name="edit"),
    path('edit_book/<int:pk>',views.Book_Update_View.as_view(),name="edit"),
    # path('delete_book/<int:pk>',views.delete_book,name="delete"),
    path('delete_book/<int:pk>',views.Book_Delete_View.as_view(),name="delete"),
    
]
