from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 부모에서 하는건 그대로 상속받아서 그대로 사용 가능하고 거기에 더 기능을 덧붙일 수 있다

        self.fields['username'].disabled = True
        # 아이디를 입력하는 필드에 disabled 속성 True로 설정