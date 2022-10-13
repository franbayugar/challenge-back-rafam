from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'api/lessons', views.LessonViewSet )
router.register(r'api/courses', views.CourseViewSet )
router.register(r'api/users', views.UserViewSet, 'users') #name=users-list
router.register(r'api/users-lessons', views.UserLessonsViewSet )
router.register(r'api/users-friends', views.UserFriendsViewSet )

print (router.urls)
urlpatterns = router.urls