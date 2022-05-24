from django.db import models


# class APIData(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#     #cat = models.Foreignkey('Category', on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name


class APIWEB(models.Model):
    name_api = models.CharField(max_length=100)
    web_api = models.CharField(max_length=255)
    title_api = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default=' ')
    X_RapidAPI_Host = models.CharField(max_length=255, default=' ')
    X_RapidAPI_Key = models.CharField(max_length=255, default=' ')
    def __str__(self):
        return self.name_api

class Parameters(models.Model):
    id_api=models.ForeignKey('APIWEB', on_delete=models.CASCADE)
    #id_api = models.Foreignkey('APIWEB', on_delete=models.CASCADE)
    parameter_api = models.CharField(max_length=255)
    title_parameter = models.CharField(max_length=100, default='')
    type_parameter = models.CharField(max_length=100)
    description_parameter=models.CharField(max_length=255, default=' ')
    def __str__(self):
        return self.parameter_api