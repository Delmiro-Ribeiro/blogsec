from django.db import models

#from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    imagem = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title  + ' | ' + self.created_at.strftime('%d-%m-%Y')
