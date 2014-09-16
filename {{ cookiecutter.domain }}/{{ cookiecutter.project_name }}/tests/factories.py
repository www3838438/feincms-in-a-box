import factory

from feincms.module.medialibrary.models import MediaFile
from feincms.module.page.models import Page


class MediaFileFactory(factory.DjangoModelFactory):
    file = factory.django.FileField(data='hello!', filename='hello.txt')

    class Meta:
        model = MediaFile


class PageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Page
