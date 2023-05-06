from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('checksubsciption', views.checksubsciption, name='checksubsciption'),
    path('download_pdf', views.download_pdf, name='download_pdf'),

    #blog content urls
    path('blog',views.blog,name='blog'),
    path('blog/delete_blog<str:pk>',views.delete_blog,name='delete_blog'),
    path('blog/add_blog',views.add_blog,name='add_blog'),
    path('blog/update_blog<str:pk>',views.update_blog,name='update_blog'),
    path('blog/blog_detail<str:pk>', views.blog_detail, name='blog_detail'),


    #Testimonies 
    path('testimonies', views.testimonies, name='testimonies'),
    path('testimonies/add_testimonies', views.add_testimonies, name='add_testimonies'),
    path('testimonies/create_testimony', views.create_testimony, name='create_testimony'),
    path('testimonies/delete_testimony<str:pk>', views.delete_testimony, name='delete_testimony'),
    path('testimonies/update_testimony<str:pk>', views.update_testimony, name='update_testimony'),
    path('testimonies/complete_testimony<str:pk>', views.complete_testimony, name='complete_testimony'),



    path('podcast',views.podcast,name='podcast'),
    path('podcast/create_podcast',views.create_podcast,name='create_podcast'),
    path('podcast/podcast_update<str:pk>',views.podcast_update,name='podcast_update'),
    path('podcast/podcast_delete<str:pk>',views.podcast_delete,name='podcast_delete'),
    path('podcast/podcast_details<str:pk>',views.podcast_details,name='podcast_details'),
   

    path('events',views.events,name='events'),
    path('events/eventForm',views.eventForm,name='eventForm'),
    path('events/event_update<str:pk>',views.event_update,name='event_update'),
    path('events/event_delete<str:pk>',views.event_delete,name='event_delete'),
    path('events/event_details<str:pk>', views.event_detail, name='event_detail'),

    path('about',views.about,name='about'),


    path('youtube',views.youtube,name='youtube'),


    path('courses',views.courses,name='courses'),
    path('courses/create_courses',views.create_courses,name='create_courses'),
    path('courses/course_delete<str:pk>', views.course_delete, name = 'course_delete'),
    path('courses/course_update<str:pk>', views.course_update, name = 'course_update'),
    path('courses/course_details<str:pk>', views.course_details, name = 'course_details'),





    path('productss',views.products,name='products'),
    path('products/product_books',views.product_books,name='product_books'),
    path('products/product_books/product_book_update<str:pk>',views.product_book_update,name='product_book_update'),
    path('products/product_books/product_book_delete<str:pk>',views.product_book_delete,name='product_book_delete'),
    path('products/product_books/create_productbook',views.create_productbook,name='create_productbook'),
    path('products/product_books/productbook_details<str:pk>',views.productbook_details,name='productbook_details'),


    path('products/product_merchandise',views.product_merchandise,name='product_merchandise'),
    path('products/product_merchandise/product_merchandise_update<str:pk>',views.product_merchandise_update,name='product_merchandise_update'),
    path('products/product_merchandise/product_merchandise_delete<str:pk>',views.product_merchandise_delete,name='product_merchandise_delete'),
    path('products/product_merchandise/create_productmerchandise',views.create_productmerchandise,name='create_productmerchandise'),
    path('products/product_merchandise/productmerchandise_details<str:pk>',views.productmerchandise_details,name='productmerchandise_details'),




 


    #user authentification
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),

    path('ebook', views.ebook, name='ebook'),

    path('subscription', views.subscription, name = 'subscription'),
    path('subscriptionform', views.SubscriptionForm, name = 'SubscriptionForm')

]