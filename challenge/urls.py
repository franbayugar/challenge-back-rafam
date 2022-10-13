from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('api/lessons', views.LessonViewSet )
router.register('api/courses', views.CourseViewSet )
router.register('api/users', views.UserViewSet )
router.register('api/users-lessons', views.UserLessonsViewSet )
router.register('api/users-friends', views.UserFriendsViewSet )


urlpatterns = router.urls