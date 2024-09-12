from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView  # Import TemplateView
from . import views

app_ame = 'djangoapp'
urlpatterns = [
    # Path for displaying the dealers page with the index.html template
    path(route='login', view=views.login_user, name='login'),
    # Path for dealer reviews view
    path('dealer_reviews/<int:dealer_id>/', views.dealer_reviews, name='dealer_reviews'),

path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    # Path for add a review view
    path('get_cars/', views.get_cars, name='get_cars'),
        path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
            path(route='add_review', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
