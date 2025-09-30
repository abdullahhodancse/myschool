from django.core.management.base import BaseCommand
from app1.models import Student

class Command(BaseCommand):
   

    def handle(self,*args,**kwargs):
        students = Student.objects.all()
        for s in students:
            s.age = 10+s.id
            s.save()
        self.stdout.write(self.style.SUCCESS("updated"))
