from os import access
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth import authenticate    
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import CustomTokenObtainPairSerializer
from .custom_auth import CustomJWTAuthentication
from .custom_response import CustomResponse
from .error_codes import INVALID_REQUEST,INVALID_AGE,INVALID_PASSWORD,INTERNAL_SERVER_ERROR,USERNAME_EXISTS,EMAIL_EXISTS,INVALID_CREDENTIALS,MISSING_FIELDS,INTERNAL_ERROR,INVALID_KEY,INVALID_TOKEN,INVALID_VALUE,KEY_EXISTS,KEY_NOT_FOUND
from .models import CustomUser
from .serializers import CustomUserSerializer
from .helper import validate_password
from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(exc, AuthenticationFailed):
        response = Response(INVALID_TOKEN, status=status.HTTP_401_UNAUTHORIZED)

    return response
class CustomUserCreate(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        username = request.data.get('username')
        email=request.data.get('email')
        password = request.data.get('password')
        full_name=request.data.get('full_name')
        age=request.data.get('age')
        gender=request.data.get('gender')
            
            
        if (username==None or email==None or password==None or full_name==None) :
            response_data=INVALID_REQUEST
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        if(not validate_password(password)):
            response_data=INVALID_PASSWORD
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        if(age==None or (age!=None and age<=0)):
            response_data=INVALID_AGE
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        if(gender==None or (gender!=None and (gender!='male' and gender!='female' and gender!='non-binary'))):
            response_data=INVALID_AGE
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status": "success",
                "message": "User successfully registered!",
                "data": serializer.validated_data  # Use the validated data from the serializer
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data=INTERNAL_SERVER_ERROR
            try:
                serializer.errors['username']
                response_data=USERNAME_EXISTS
            
            except:
                pass

            try:
                serializer.errors['email']
                response_data=EMAIL_EXISTS

            except:
                pass
        
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if(username==None or password==None):
            response_data=MISSING_FIELDS
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
      
        if user.is_authenticated:
            refresh = RefreshToken.for_user(user)
            access_token=str(refresh.access_token),
            
            response_data={
                "status": "success",
                "message": "Access token generated successfully.",
                "data": {
                    "access_token": access_token,
                    "expires_in": 3600
                    }
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(INVALID_CREDENTIALS, status=status.HTTP_400_BAD_REQUEST)
        


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)





class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        key=request.data.get('key')
        value=request.data.get('value')
        if(key==None):
            return Response(INVALID_KEY, status=status.HTTP_400_BAD_REQUEST)
        if(value==None):
            return Response(INVALID_VALUE, status=status.HTTP_400_BAD_REQUEST)
        item=Item.objects.get(key=key)
        if(item):
            return Response(KEY_EXISTS, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        item_data = serializer.validated_data 
        return CustomResponse(status="success", message="Data stored successfully")

    

class ItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'key'
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response(INVALID_KEY, status=status.HTTP_400_BAD_REQUEST)
       
        serializer = self.get_serializer(instance)
        item_data = serializer.data
       
        return CustomResponse(status="success", data=item_data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
       
        try:
            instance = self.get_object()
        except:
            return Response(INVALID_KEY, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        item_data = serializer.data
        return CustomResponse(status="success", message="Data updated successfully")

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response(INVALID_KEY, status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        return CustomResponse(status="success", message="Data deleted successfully")