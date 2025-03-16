from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    services = models.TextField()
    investment = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    message = models.TextField(default='No Message from Customer')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/team/')
    linkedin = models.URLField()

    def __str__(self):
        return self.name
    
class EmailSubmission(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=255, null=True, blank=True)
    project_type = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class ProjectDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='details')
    client_name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    objective = models.TextField()
    secondary_image = models.ImageField(upload_to='projects/', null=True, blank=True)
    design_team = models.CharField(max_length=255, default="Nexlume")
    website_design = models.CharField(max_length=255, null=True, blank=True)
    no_code_development = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Details of {self.project.title}"



