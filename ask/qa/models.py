from django.db import models

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
	added_at = models.DateTimeField(blank = True)
	rating = models.IntegerField()
	author = models.OneToOneField(django.contrib.auth.models.User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToMany(django.contrib.auth.models.User, related_name='question_like_user').all()
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question,on_delete=models.CASCADE) 
	author = models.OneToOneField(django.contrib.auth.models.User, null=True, on_delete=models.SET_NULL)
