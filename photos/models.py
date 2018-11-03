from django.db import models

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


    def save_category(self):
        self.save()

class Location(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Image(models.Model):
    image=models.ImageField(upload_to ='images/')
    name=models.CharField(max_length =30)
    description=models.TextField()
    category=models.ForeignKey(Category)
    location=models.ForeignKey(Location)

    def __str__(self):
        return self.name

    # class Meta:
        # ordering = ('name')

    def save_image(self):
        self.save()
#     # def delete_image(self):
#     #     Image.objects.filter(id=2).delete()
#     #
#     # def update_image:
#     #     Image.objects.filter(id=2).update(description='sth')
#     #
#     # @classmethod
#     # def get_image_by_id(cls,id):
#     #     image=Image.objects.filter(id=)
#     # def search_image():
#     #
#     # @classmethod
#     # def get_image_by_id(cls,id):
#     #
#     # @classmethod
#     # def filter_by_location
#
    @classmethod
    def get_photos(cls):

        photos=cls.objects.all()
        return photos
    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter(category__icontains=search_term)
        return photos

    # @classmethod
    # def filter_by_location(cls,location):
    #     photos=cls.objects.get(nairobi=location)
    #     return photos
