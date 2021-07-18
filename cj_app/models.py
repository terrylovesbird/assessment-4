from django.db import models

class CjCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    def __str__(self):
        return f"category: {self.name}"

class CjPost(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField()
    category = models.ForeignKey(CjCategory, related_name="cj_posts", on_delete=models. CASCADE)

    def __str__(self):
        return f"post: {self.name}, {self.category}"
