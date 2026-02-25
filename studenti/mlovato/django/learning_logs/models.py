from django.db import models

# Create your models here.
class Topic(models.Model):
    """Una materia che l'utente sta imparando"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """restituisce una rappresentazione in stringa del modello"""
        return self.text
    
class Entry(models.Model):
    """argomento appreso su una materia"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        """restituisce una sstringa che rappresenta la descrizione di cosa si è appreso"""
        return f"{self.text[:50]}..."
    