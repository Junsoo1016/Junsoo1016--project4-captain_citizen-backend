from django.db import models

# Create your models here.
class User(models.Model):
   first_name = models.CharField(max_length=50, default = 'Please input first name')
   last_name = models.CharField(max_length=50, default = 'Please input last name')
   age = models.IntegerField(blank=True, null=True)
   user_id = models.CharField(max_length=50, default = 'Please input user name')
   password = models.CharField(max_length=250)
   email = models.EmailField(max_length=250)
   nationality = models.CharField(max_length=100, default = 'please input nationality')
   photo_url = models.ImageField(upload_to='profile', default = 'please upload your profile image')
   address = models.CharField(max_length=250)
   lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
   lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
   login = False 
   request = False
   created_at = models.DateTimeField(auto_now_add=True)
   my_requests = []
 
class HelpRequest(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="help_requests")
   description = models.TextField(default = "Emergency! I'm in danger now, please help me!")
   created_at = models.DateTimeField(auto_now_add=True)
   will_come_help = []
   completed = False
