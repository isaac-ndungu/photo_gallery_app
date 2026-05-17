from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

UserModel = get_user_model()

class CustomEmailBackend(ModelBackend):
    """Backend to authenticate using either email or username."""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None
            
        try:
            if '@' in username:
                user = UserModel.objects.get(email=username)
            else:
                user = UserModel.objects.get(username=username)
        except ObjectDoesNotExist:
            # Run password hasher once to reduce timing difference
            UserModel().set_password(password)
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None