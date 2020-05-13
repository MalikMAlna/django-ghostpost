from django import forms


class AddPost(forms.Form):
    b_or_r = forms.BooleanField()
    content = forms.CharField(max_length=280)
    up_vote = forms.IntegerField(default=0)
    down_vote = forms.IntegerField(default=0)
    created = forms.DateTimeField()


"""
class Post(models.Model):
    b_or_r = models.BooleanField()
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created = models.DateTimeField()

"""
