from django.db import migrations

def increment_age(apps, schema_editor):
    Student = apps.get_model('app1', 'Student')
    for s in Student.objects.all().order_by('id'):  
        s.age += 5
        s.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_student_age'),
    ]

    operations = [
        migrations.RunPython(increment_age),
    ]
