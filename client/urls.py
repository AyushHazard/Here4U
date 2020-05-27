from django.urls import path
from . import views
from django.shortcuts import render, redirect

from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token

# from counsellor.urls import
    
# router = routers.DefaultRouter()

# router.register('api/talk',views.TalkViewSet,'talk-api')

urlpatterns = [
    path('', views.home, name = "client-home"),
    path('about/',views.about, name="client-about"),
    path('talk/',views.talk,name = "talk-to-counsellor"),
    path('signup/',views.signup,name="sign-up"),
    path('update-profile/',views.updateProfile,name="update-profile"),

    path('edit-profile/',views.editProfileClient,name="edit-profile"),
    path('edit-profile-counsellor/',views.editProfileCounsellor,name="edit-profile-counsellor"),

    path('delete-description/<int:pk>/',views.deleteDescription,name="delete-description"),
    path('delete-booking/<int:pk>/',views.deleteBooking,name="delete-booking"),


    path('my-profile/',views.myProfile,name="my-profile"),
    path('counsellor-profile/<int:pk>/',views.counsellorProfile,name="counsellor-profile"),
    # path('accounts/login/',views.login,name='login'),
    # path('accounts/logout/',views.logout,name='log-out'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('pick/',views.pick,name = "pick-clients"),
    path('active/',views.active,name = "active-clients"),
    path('active-sessions/',views.sessions,name="active-sessions"),
    path('update-profile-counsellor',views.updateProfileCounsellor,name="update-profile-counsellor"),
    path('book/<int:pk>/',views.book,name="book-appointment"),
    path('FAQs/',views.faqs,name="faqs"),
    #path('blog/',views.blog,name="blog"),
    path('blog/', views.blogListView, name="blog"),
    path('blog/blog_detail/<int:pk>/',views.blogDetailView,name="blog_detail"),
    path('blog/add_post/',views.createPostView,name="add_post"),
    path('blog/personal-blogs/',views.personalBlogListView,name="personal-blogs"),
    path('blog/delete-blog/<int:pk>/',views.deleteBlog,name="delete-blog"),
    path('blog/update-blog/<int:pk>/',views.updateBlogView,name="update-blog"),

    path('messages/',views.messages,name = "messages"),
    path('messages-detail/<int:pk>/',views.messageDetail,name = "message-detail"),
    path('videocall/',views.videoCall,name = "video-call"),
    path('connect-client/<int:pk>/',views.interfaceClient,name="connect-client"),
    path('connect-counsellor/<int:pk>/',views.interfaceCounsellor,name="connect-counsellor"),
    path('delete-link/<int:pk>/',views.deleteLink,name="delete-link"),

    path('view-description/<int:pk>',views.clientDescription,name='view-description'),
    path('session-notes/<int:pk>',views.sessNotes,name='session-notes'),
    path('view-notes/<int:pk>',views.viewSessNotes,name='view-notes'),
    path('delete-notes/<int:pk>',views.delSessNotes,name='delete-notes'),

    
    # API URLS
    #api auth
    
    path('api/signup/',views.CreateUserView.as_view(),name='signup-api'),
    path('api/create-profile/',views.CreateClientProfileView.as_view(),name="create-profile-api"),
    path('api/create-profile-counsellor/',views.CreateCounsellorProfileView.as_view(),name="create-profile-counsellor-api"),
   
    path('api/create-description/',views.CreateDescriptionView.as_view(),name="create-description-api"),
    path('api/list-description/<int:pk>/',views.GetDescriptionView,name="list-description-api"),
    
    path('api/check/',views.UserTypeCheck,name='check'),
    path('api/list-counsellors/',views.ListCounsellorsView.as_view(),name="list-counsellors"),
    path('api/get-userid/',views.GetUserId,name="get-user-id"),
   
    path('api/get-client/<int:pk>/',views.GetClientView,name="get-client"),
    path('api/get-counsellor/<int:pk>/',views.GetCounsellorView,name="get-counsellor"),
   
    path('api/update-profile-counsellor/',views.UpdateCounserllorProfileView.as_view(),name="update-profile-counsellor-api"),
    path('api/update-profile/',views.UpdateClientProfileView.as_view(),name="update-profile-api"),
   
    path('api/book/',views.CreateBookingView.as_view(),name="book"),
    path('api/active-clients/',views.GetActiveClientsView,name="active-clients-api"),
    path('api/active-counsellors/',views.GetActiveCounsellorsView,name="active-counsellors-api"),

    path('api/logout/',views.LogOutView,name="logout-api"),
    path('api/login/',views.LogInView.as_view(),name="login-api"),

    path('api/token-auth/',obtain_jwt_token),
    path('api/current-user/',views.current_user,name ="current-user")

]

# urlpatterns = urlpatterns+router.urls