# Generated by Django 3.1.1 on 2020-09-25 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200924_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ['dia'], 'verbose_name': 'Agenda', 'verbose_name_plural': 'Agendas'},
        ),
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['data', 'horario'], 'verbose_name': 'Consulta', 'verbose_name_plural': 'Consultas'},
        ),
        migrations.AddField(
            model_name='consulta',
            name='agenda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='core.agenda'),
        ),
        migrations.AlterUniqueTogether(
            name='consulta',
            unique_together={('data', 'horario', 'agenda')},
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='medico',
        ),
    ]
