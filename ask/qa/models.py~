from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
        def new(self):                                                              
                from django.db import connection
        	cursor = connection.cursor()
		return cursor.execute("SELECT title FROM Question ORDER BY added_at")
		
		                                                           
        def popular(self):                                                          
                from django.db import connection
        	cursor = connection.cursor()
		return cursor.execute("SELECT title FROM Question ORDER BY rating")
		

class Question(models.Model):
	objects = QuestionManager() 
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True,auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.OneToOneField(User, default = 'x')
	likes = models.ManyToManyField(User, related_name='question_like_user')
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question,on_delete=models.CASCADE) 
	author = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
