# Generated by Django 4.2.23 on 2025-07-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Digite aqui o texto da pergunta.', verbose_name='Pergunta')),
                ('answer', models.TextField(help_text='Digite aqui o texto da resposta.', verbose_name='Resposta')),
            ],
        ),
    ]
