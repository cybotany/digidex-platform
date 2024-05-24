from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers.tokens import UserTokenObtainPairSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
