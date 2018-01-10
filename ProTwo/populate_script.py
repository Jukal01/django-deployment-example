import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


from faker import Faker
from AppTwo.models import User

fake = Faker()

def populate(N=5):
    
    for n in range(N):

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_mail = fake.email()

        user = User.objects.get_or_create(First_Name=fake_first_name,Last_Name=fake_last_name,Email=fake_mail)[0]

if __name__ == '__main__':
    print('populating script')
    populate(10)
    print('populating complete')
