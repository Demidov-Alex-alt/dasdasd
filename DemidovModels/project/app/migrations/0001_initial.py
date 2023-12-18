from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(default='/static/alabuga2.jpg', upload_to='')),
            ],
        ),
    ]
