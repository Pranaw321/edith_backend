from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import *  
from .models import *
from .serializers import *

from apps.userpanel.paginations import SwooshPagination
from rest_framework.generics import GenericAPIView
from django.conf import settings



class AdminRegisterationAPIView(generics.CreateAPIView):
    
    serializer_class = RegisterSerializer
    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                context = {'status': True,'message': 'Successfully Register'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)



class RoleCreateAPIView(generics.ListCreateAPIView):

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    def get_queryset(self):
        queryset = Role.objects.all()
        return queryset




class LoginAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''
Module Permissions Create and list

'''
class CreateModuleAPIView(generics.ListCreateAPIView):

    serializer_class = AppModuleSerializer
    queryset = AppModule.objects.all()
    def get_queryset(self):
        queryset = AppModule.objects.all()
        return queryset

'''
Create Module Permission  and Lists 
'''
class CreateModulePermissionAPIView(generics.ListCreateAPIView):

    serializer_class = AppModulePermissionSerializer
    queryset = AppModulePermission.objects.all()
    def get_queryset(self):
        queryset = AppModulePermission.objects.all()
        return queryset

'''
Module wise Permission list

'''
class CreateModulePermissionListAPIView(generics.ListAPIView):
    pagination_class = SwooshPagination
    serializer_class = AppModuleWisePermissionListSerializer
    queryset = AppModule.objects.all()
    def get_queryset(self):
        queryset = AppModule.objects.all()
        return queryset

'''
Create Module Permission  and Lists 
'''
class CreateUserProfileAPIView(generics.CreateAPIView):

    serializer_class = UserGroupPermissionSerializer
    queryset = BaseGroup.objects.all()
    def get_queryset(self):
        queryset = BaseGroup.objects.all()
        return queryset

class UserProfileListAPIView(generics.ListAPIView):

    serializer_class = UserProfileListSerializer
    queryset = BaseGroupPermissions.objects.all()
    def get_queryset(self):
        queryset = BaseGroupPermissions.objects.all()
        return queryset