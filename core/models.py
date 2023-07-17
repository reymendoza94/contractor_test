from django.db import models

# Create your models here.
LABEL_TYPE = (
    ('simple','simple'),
    ('attribute_based','attribute based'),
    ('multi_level','multi level')
)

class Label(models.Model):    
    label_name = models.CharField(max_length=200)
    label_type = models.CharField(choices=LABEL_TYPE, max_length=20)
    chield = models.ManyToManyField('Label', through= 'Label')
    assignament = models.BooleanField(),
    exclusibity = models.BooleanField(),

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")

    def __str__(self):
        return self.label_name

    def clean(self):
        if self.label_type == 'simple' and self.chield != None:
            raise ValidationError('This label is Type Simple')
        else:
            if self.label_type == 'attribute_based' and len(self.chield) > 1:
                raise ValidationError(('This label is attribute based'))
                
        return self

class Picture(models.Model):
    picture_name = models.CharField(max_length=200)
    file_picture = models.ImageField()
    
    def __str__(self):
        return self.picture_name