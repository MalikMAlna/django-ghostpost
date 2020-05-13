from django import forms


class AddPost(forms.Form):
    boast_or_Roast = forms.BooleanField(
        help_text="Checked is Boast, Unchecked is Roast")
    content = forms.CharField(max_length=280)


"""
class Post(models.Model):
    b_or_r = models.BooleanField()
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created = models.DateTimeField()

"""
