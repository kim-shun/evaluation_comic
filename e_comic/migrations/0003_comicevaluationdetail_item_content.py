# Generated by Django 4.0.4 on 2022-05-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_comic', '0002_alter_evaluationitemcontents_parent_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='comicevaluationdetail',
            name='item_content',
            field=models.CharField(max_length=50, null=True, verbose_name='評価項目内容'),
        ),
    ]