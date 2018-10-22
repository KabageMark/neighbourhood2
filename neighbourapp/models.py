from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile-pics')
    bio = models.TextField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    @classmethod
    def get_all(cls):
        all_objects = Profile.objects.all()
        return all_objects
     
    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__name__icontains=search_term)
        return profile

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

class NeighbourHood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    Occupants_count = models.PositiveIntegerField()
   
    def create_neigborhood(self):
        return self.save()

    def delete_neigborhood(self):
        return self.delete()

    @classmethod
    def get_all(cls):
        all_objects = NeighbourHood.objects.all()
        return all_objects    

    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        neigborhood_result = cls.objects.get(id = neigborhood_id)
        return neigborhood_result

    @classmethod    
    def update_neighborhood(cls,current_value,new_value):
        fetched_object = cls.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def update_occupants(cls,current_value,new_value):
        fetched_object = cls.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

class Business(models.Model):
    user = models.ForeignKey(User,null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70,null=True)
    
    @classmethod
    def get_all(cls):
        all_objects = Business.objects.all()
        return all_objects
    
    def create_business(self):
        return self.save()

    def delete_business(self):
        return self.delete()

    @classmethod
    def find_business(cls,business_id):
        business_result = cls.objects.get(id=business_id)
        return business_result

    @classmethod
    def update_business(cls,current_value,new_value):
        fetched_object = cls.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = cls.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

class Post(models.Model):
    image = models.ImageField(upload_to='post_pics')
    description = models.TextField()
    title = models.CharField(max_length=30)

    @classmethod
    def get_all(cls):
        all_objects = Post.objects.all()
        return all_objects