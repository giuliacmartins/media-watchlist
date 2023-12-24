from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField()
    year = models.CharField(max_length=9)
    genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.title

class CompletedMedia(models.Model):
    comp_title = models.CharField(max_length=255)
    comp_poster = models.URLField()
    comp_year = models.CharField(max_length=9)
    comp_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.comp_title
    
class NotCompletedMedia(models.Model):
    notcomp_title = models.CharField(max_length=255)
    notcomp_poster = models.URLField()
    notcomp_year = models.CharField(max_length=9)
    notcomp_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.notcomp_title

class Anime(models.Model):
    animetitle = models.CharField(max_length=255)
    animeposter = models.URLField()
    animeyear = models.CharField(max_length=9)
    animegenre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.title
    
class CompletedAnime(models.Model):
    comp_anime_title = models.CharField(max_length=255)
    comp_anime_poster = models.URLField()
    comp_anime_year = models.CharField(max_length=9)
    comp_anime_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.comp_anime_title
    
class NotCompletedAnime(models.Model):
    notcomp_anime_title = models.CharField(max_length=255)
    notcomp_anime_poster = models.URLField()
    notcomp_anime_year = models.CharField(max_length=9)
    notcomp_anime_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.notcomp_anime_title
    
class PriorityMedia(models.Model):
    priority_title = models.CharField(max_length=255)
    priority_poster = models.URLField()
    priority_year = models.CharField(max_length=9)
    priority_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.priority_title
    
class PriorityAnime(models.Model):
    priority_anime_title = models.CharField(max_length=255)
    priority_anime_poster = models.URLField()
    priority_anime_year = models.CharField(max_length=9)
    priority_anime_genre = models.CharField(max_length=255, default='None')
    
    def __str__(self):
        return self.priority_anime_title