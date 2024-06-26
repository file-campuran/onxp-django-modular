# Generated by Django 5.0.6 on 2024-06-01 17:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_dashboard", "0001_create_book_table"),
    ]

    operations = [
        migrations.RunSQL(
            sql = [
                ("""
                CREATE TABLE IF NOT EXISTS pinjam_buku (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID,
                    book_id UUID,
                    start_date DATE,
                    end_date DATE);"""),
            ],
            reverse_sql=[
                ("DROP TABLE IF EXISTS pinjam_buku;"),
                ("DROP EXTENSION pgcrypto;"),
            ],
        )
    ]
