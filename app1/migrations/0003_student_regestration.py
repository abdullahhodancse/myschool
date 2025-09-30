from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_teacher'),  # আগের মাইগ্রেশন ফাইল
    ]

    operations = [
        
        migrations.AddField(
            model_name='student',
            name='regestration',
            field=models.IntegerField(default=0),
        ),
        
        
    ]