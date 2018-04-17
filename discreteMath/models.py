from django.db import models

#should be self-encapsulating, might need to increase text limit
class Question(models.Model):
    question_text = models.CharField(max_length=512)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now(), datetime.timedelta(days=7)

#I'd like to make this a fillable form, but static answers will do for now
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.CharField(max_length=512)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
