from django.db import models

class CustomUser(models.Model):
    name = models.charField(max_length = 200)
    joined_group = models.charField(max_length = 5)





    pass

class Group(models.Model):
    group_name = models.charField(max_length = 50)



    pass


class Message(models.Model):
    group = models.ForeignKey(Question, on_delete = models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_lenght = 50)
    #time_stamp = models.TimeField()



    pass
