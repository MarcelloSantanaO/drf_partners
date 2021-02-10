# Generated by Django 3.1.6 on 2021-02-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210210_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='cnpj',
            field=models.CharField(default='05/29/2015 05:50:06', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='cnpj_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='uf',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
