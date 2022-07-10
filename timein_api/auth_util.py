from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.models import User


def get_user(request):
    jwt_object = JWTAuthentication()
    header = jwt_object.get_header(request)
    raw_token = jwt_object.get_raw_token(header)
    validated_token = jwt_object.get_validated_token(raw_token)
    user = jwt_object.get_user(validated_token)
    print('User: ' + str(user))
    authorized_users = User.objects.filter(email=user)
    if not authorized_users:
        return None
    return user
