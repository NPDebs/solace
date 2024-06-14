from django.db import models

# Create model for post category
class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name   

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") # Assign many categories to many posts (Many-to-many relationship)

    def __str__(self):
        return self.title
    
# Create model for comments
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE) # Assign multiple comments to a single post (Many-to-one relationship). Delete comments if post is deleted.


    def __str__(self):
        return f"{self.author} on '{self.post}'"