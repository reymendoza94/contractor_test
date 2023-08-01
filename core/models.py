from django.db import models
from django.core.validators import ValidationError

# Create your models here.
LABEL_TYPE = (
    ('simple','simple'),
    ('attribute_based','attribute based'),
    ('multi_level','multi level')
)

class Label(models.Model):    
    label_name = models.CharField(max_length=200)
    label_type = models.CharField(choices=LABEL_TYPE, max_length=20)
    level = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    assignament = models.BooleanField(default=False)
    exclusibity = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Label")
        verbose_name_plural = ("Labels")

    def __str__(self):
        return self.label_name

    def clean(self):
        super().clean()
        
        if self.label_type == 'simple' and self.level:
            raise ValidationError('This label is type Simple and can not have levels.')
        else: 
            if self.label_type == 'attribute_based' and (not self.level or self.level.level):
                raise ValidationError('This label is type Attribute Based and can only have one level.')
            else:
                if self.label_type == 'multi_level' and (not self.level or self.level == None):
                    raise ValidationError('This label is type Multi Level  and must have more than one level.')

    
        # if self.exclusibity and len(self.level.level) >= 1:
        #     raise ValidationError('This label is exclusive and cannot be assigned.')

      

# class Picture(models.Model):
#     picture_name = models.CharField(max_length=200)
#     file_picture = models.ImageField()
    
#     def __str__(self):
#         return self.picture_name