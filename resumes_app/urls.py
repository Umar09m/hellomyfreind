from .views import *
from django.urls import path

urlpatterns = [
    path('partners/', PartnerViewSet.as_view({'get': 'list'})),
    path('categories/', CategoriesViewSet.as_view({'get': 'list'})),
    path('resumes/', ResumeReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('resumes/<int:pk>/', ResumeReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('wishlist/', WishlistModelViewSet.as_view({'get': 'list'})),
    path('wishlist/<int:pk>/', WishlistModelViewSet.as_view({'get': 'retrieve'})),
    path('wishlist/create/<int:pk>/', WishlistModelViewSet.as_view({'post': 'create'})),
    path('wishlist/delete/<int:pk>/', WishlistModelViewSet.as_view({'delete': 'destroy'}))
]