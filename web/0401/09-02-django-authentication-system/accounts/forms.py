from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User : 장고는 user 클래스 직접 참조 대신 get_user_model()사용권장

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 장고 프로젝트에 활성화된 user 객체 반환 함수 
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 회원정보수정시 몇개의 필드는 안보이게하기
        fields = ('first_name','last_name','email',)