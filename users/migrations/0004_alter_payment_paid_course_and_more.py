# Generated by Django 5.1.3 on 2024-11-26 19:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0006_subscription"),
        ("users", "0003_payment_link_payment_session_id_payment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="paid_course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.courses",
                verbose_name="Оплаченный курс",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_amount",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Сумма оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateField(blank=True, null=True, verbose_name="Дата оплаты"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                blank=True,
                choices=[("cash", "Наличные"), ("transfer", "Перевод на счет")],
                max_length=20,
                null=True,
                verbose_name="Способ оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="separately_paid_lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lessons",
                verbose_name="Отдельно оплаченный урок",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
