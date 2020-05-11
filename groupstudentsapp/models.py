from django.db import models


class GroupOfStudents(models.Model):
    class Meta:
        # managed = True
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'
    
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        blank=False)
    
    def __str__(self):
        return self.name
