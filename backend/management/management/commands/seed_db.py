import random
import os

from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
from faker import Faker

from ...models import Department, Employee



class Command(BaseCommand):
    help = 'Populate the database with departments and employees'

    def handle(self, *args, **kwargs):
        fake = Faker()

        root_departments = []
        for _ in range(5):
            root_department = Department.objects.create(name=fake.company())
            root_departments.append(root_department)

        def create_child_departments(parent, level):
            if level < 5:
                for _ in range(random.randint(0, 5)):
                    child_department = Department.objects.create(name=fake.company(), parent=parent)
                    create_child_departments(child_department, level + 1)

        for root_department in root_departments:
            create_child_departments(root_department, 1)

        all_departments = Department.objects.all()
        for _ in range(50000):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                date_of_employment=fake.date_this_decade(),
                salary=random.randint(30000, 150000),
                department=random.choice(all_departments)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))