from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    owner = models.ForeignKey(
        Profile,null= True,blank=True,on_delete=models.CASCADE
        )
    title = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True) ##blank tells django wether to Allow blank on the formas for this filed
    featured_image =  models.ImageField(null=True, blank=True, 
                                        default="https://res.cloudinary.com/dw32qih2n/image/upload/v1733065323/default_da6aid.jpg"
                                        # default="default.jpg"
                                        
                                        )
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)  ##'' around the tag referenece is required because the Tag model is below in The .py file
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        # ordering = ['created'] # "-" orders by descending
        ordering = ['-vote_ratio','-vote_total','created']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
            # url = "https://res.cloudinary.com/dw32qih2n/image/upload/v1733065323/default_da6aid.jpg"
        except:
            # url='project_default.jpg'
            # url = 'https://res.cloudinary.com/dw32qih2n/image/upload/v1733065323/default_da6aid.jpg'
            url = ''
        return url
    
    @property
    def reviewers(self):
        queryset  = self.review_set.all().values_list('owner__id',flat=True)
        return queryset


    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (int(upVotes) / int(totalVotes)) * 100

        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

        
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),

    )
    owner = models.ForeignKey (Profile, on_delete=models.CASCADE, null = True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE) # if the Project is deleted it will delete all the reviews
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    ####ONLY ALLOW ONE REVIEW PER PROJECT PER USER

    class Meta:
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value
    
