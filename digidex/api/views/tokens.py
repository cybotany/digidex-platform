from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers.tokens import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
