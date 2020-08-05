# Generated by Django 3.1 on 2020-08-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200805_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='count_upvotes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]