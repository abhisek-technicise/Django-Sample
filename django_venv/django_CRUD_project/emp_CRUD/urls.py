from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from emp_CRUD.simple_views import emp_list,emp_create,get_emp_by_id,update_emp_by_id,delete_emp_by_id
from emp_CRUD import class_views
from rest_framework.urlpatterns import format_suffix_patterns

from emp_CRUD.viewset import EmpViewSet
from emp_CRUD.viewset import EmpdetailsViewSet

# URLConf for simple_view
'''
urlpatterns = [ 
	url( r'^show_Employees/$', emp_list ),
	url( r'^create_Employee/$', emp_create ),
	url( r'^show_employee_by_ID/(?P<emp_id>.*)/$', get_emp_by_id ),
	url( r'^update_employee_by_ID/(?P<emp_id>.*)/$',update_emp_by_id ),
	url( r'^delete_employee_by_ID/(?P<emp_id>.*)/$', delete_emp_by_id ),
]
'''
# URLConf for class_view
'''
urlpatterns = [ 
	url( r'^emp_CRUD/$', class_views.EmpList.as_view()),
	url( r'^emp_CRUD/(?P<emp_id>.*)/$', class_views.EmpList_details.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
'''

# URLConf for viewset and Router
'''emp_list = EmpViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

emp_detail = EmpdetailsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    #'patch': 'partial_update',
    'delete': 'destroy'
})'''
router = routers.DefaultRouter()
router.register(r'Employees',EmpViewSet,'emp_list') # showEmployees
router.register(r'Employees-details',EmpdetailsViewSet,'emp_detail') # createEmployee
urlpatterns = router.urls


