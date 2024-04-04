from django.db import models

# Create your models here.
# class Skills(models.Model):
#     name = models.CharField(max_length=16)
#     # project = models.ForeignKey('Projects', on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f'{self.name}'
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, null=True, default="default description  -  jkfhbsvliughflkjwshbkuifgbvlsghglifvbksuyhrglbwelsuihgbliuhwliuhgri")
    date_created = models.DateField(blank=True, null=True, default="2023-10-23")
    git_link = models.URLField(max_length=200, default="https://www.google.com/", blank=True, null=True)
    image = models.ImageField(upload_to="static/", blank=True, null=True)
     
    def __str__(self):
        return f'{self.title}'
    
class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    blog_number = models.CharField(max_length=3)
    summary = models.TextField(max_length=100, blank=True, null=True, default="default description  -  jkfhbsvliughflkjwshbkuifgbvlsghglifvbksuyhrglbwelsuihgbliuhwliuhgri")
    date_created = models.DateField(blank=True, null=True, auto_now_add=True)
    content = models.TextField(default="test content")
    slug = models.SlugField(max_length=100, unique=True, default="default-slug")
    blog_image = models.ImageField(upload_to="static/", null=True, blank=True)

    def __str__(self):
        return f'{self.title}  |  #{self.blog_number}'
    
class About(models.Model):
    creator = models.CharField(max_length=50)
    about_creator = models.TextField()
    

    
