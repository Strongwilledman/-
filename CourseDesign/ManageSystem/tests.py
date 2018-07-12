from django.test import TestCase
from ManageSystem import models
# Create your tests here.
models.Classes.objects.create(caption='软件1班')
models.Classes.objects.create(caption='软件2班')
models.Classes.objects.create(caption='软件3班')
models.Classes.objects.create(caption='软件4班')
models.Administrator.objects.create(username='root',password='root')