from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SignInWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field

        user_name = user.text
        password = pwd.text
        info = self.ids.info

        if user_name == '' or password == '':
            info.text = '[color=#FF0000]Username and/or password is required[/color]'
        elif user_name == 'admin' and password == "admin":
            info.text = '[color=#00FF00]Logged in successfully![/color]'
        else:
            info.text = '[color=#FF0000]Invalid username and/ or password! [/color]'


class SignInApp(App):
    def build(self):
        return SignInWindow()


if __name__ == "__main__":
    sa = SignInApp()
    sa.run()
