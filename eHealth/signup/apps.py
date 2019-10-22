from django.apps import AppConfig


class SignupConfig(AppConfig):
    name = 'signup'


    def ready(self):
        import  users.signals
