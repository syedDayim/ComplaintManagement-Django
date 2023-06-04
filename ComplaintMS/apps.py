from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout='vertical'
class ComplaintMSConfig(AppConfig):
    name = 'ComplaintMS'
    
