from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ArticleSerializer, UserSerializer
from .utils import send_mail, decrypt_user_id
from news.models import Article
from accounts.models import User


class ArticleAPIView(generics.ListCreateAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class RetrieveArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pk"


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()   
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serilizer = UserSerializer(data=request.data)
        if serilizer.is_valid():
            data = serilizer.validated_data.copy()
            data.pop("password_confirm")
            password = data.pop("password")
            user: User = User.objects.create(
                **data
            )
            user.set_password(password)
            user.save()

            message = f"Account validation link was sent to {serilizer.validated_data.get('email')}"
            send_mail(user)

            message_response = {
                "data": data,
                "message": message
            }
            return response.Response(data=message_response, status=status.HTTP_201_CREATED)
        return response.Response(data=serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ConfirmUser(views.APIView):

    def get(self, request, code):
        user_id = decrypt_user_id(encrypted_id=code)
        if user_id is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        
        user.is_active = True
        user.save()
        return response.Response({"message": "Confirmed!"}, status=status.HTTP_200_OK)
