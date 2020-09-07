from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.


class Index_Profile1(models.Model):
    Pic = models.ImageField(upload_to='pic/')
    Pic_title = models.CharField(max_length = 100)
    pic_desc = models.TextField()

# class Index_Profile2(models.Model):
#     Pic2 = models.ImageField(upload_to='pic/')
#     Pic_title2 = models.CharField(max_length = 100)
#     pic_desc2 = models.TextField()

# class Index_Profile3(models.Model):
#     Pic3 = models.ImageField(upload_to='pic/')
#     Pic_title3 = models.CharField(max_length = 100)
#     pic_desc3 = models.TextField()

# class Index_Profile4(models.Model):
#     Pic4 = models.ImageField(upload_to='pic/')
#     Pic_title4 = models.CharField(max_length = 100)
#     pic_desc4 = models.TextField()

class Contact(models.Model):
    name1 = models.CharField(max_length=122)
    email1 = models.CharField(max_length=122)
    phone1 = models.CharField(max_length=12)
    desc1 = models.TextField()
   

    def __str__(self):
        return self.name1
    

class Admission_details(models.Model):
    name = models.CharField(max_length=122,null=True)
    EmailID = models.EmailField(max_length=122,null=True)
    gender = models.CharField(max_length=122,null=True)
    DoB = models.DateField(blank=True,null=True)
    Permanent_Address = models.CharField(max_length=225,null=True)
    PinCode = models.CharField(max_length=10,null=True)
    Mob_No = models.CharField(max_length=10,null=True)
    Parents_Mob_No = models.CharField(max_length=10,null=True)
    HSSC_Stream = models.CharField(max_length=122,null=True)
    Total_Marks = models.CharField(max_length=122,null=True)
    Marks_Obtained = models.CharField(max_length=122,null=True)
    file = models.FileField()
    file1 = models.FileField(null=True)
    file2 = models.FileField(null=True)

    def __str__(self):
        return self.name    


class Gallery(models.Model):
    Img_title = models.CharField(max_length=100,null=True)
    Image = models.ImageField(upload_to='images/')

class LatestNews_TopImage(models.Model):
    top_Image = models.ImageField(upload_to='images/')


class LatestNews_column(models.Model):
    Thumbnail_Image = models.ImageField(upload_to='images/')
    description = models.TextField()
    

class LatestNews_box1(models.Model):
    bullets = models.CharField(max_length=100)

class LatestNews_box2(models.Model):
    bullet = models.CharField(max_length=100)