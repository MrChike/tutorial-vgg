# Tut 1, Step 3
from django.urls import path
# Tut 1, Step 3
from snippets import views
# Tut 2, Step 2
from rest_framework.urlpatterns import format_suffix_patterns


# Tut 1, Step 3
urlpatterns = [
    # MODEL VIEW
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    # CLASS VIEW
    path('snippets/', views.SnippetList.as_view()),  # Tut 3, Step 1
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),  # Tut 3, Step 1
    path('users/', views.UserList.as_view()),  # Tut 4, Step 2
    path('users/<int:pk>/', views.UserDetail.as_view()),  # Tut 4, Step 2
]

# Tut 2, Step 2
urlpatterns = format_suffix_patterns(urlpatterns)
