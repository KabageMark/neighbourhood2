from django.db import models

# Create your models here.

class NeighbourHood(models.Model):
    neigborhood_id = models.AutoField()
    image_name = models.CharField(max_length =30)
    image_location = models.CharField(max_length =30)
    Occupants Count = models.PositiveIntegerField()
    Admin Foreign key = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)

    @classmethod
    def create_neigborhood(cls,self):
        return self.save()
        
    @classmethod
    def delete_neigborhood(cls,self):
        return self.delete()

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
    business_id = models.AutoField()
    email = models.EmailField(max_length=70,null=True)

    @classmethod
    def create_business(cls,self):
        return self.save()

    @classmethod
    def delete_business(cls,self):
        return self.delete()

    @classmethod
    def find_business(cls,business_id):
        business_result = cls.objects.get(id=business_id)
        return business_result

    @classmethod
    def update_business(cls,current_value,new_value):
        fetched_object = Business.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object