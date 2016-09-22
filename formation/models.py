from django.db import models

# Using django with views : https://blog.rescale.com/using-database-views-in-django-orm/


class Site(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=2)
    libelle = models.CharField(max_length=250)
    code = models.CharField(max_length=2)
    code_commune = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'sites'


class Batiment(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=3)
    libelle = models.CharField(max_length=250)
    site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'batiments'


class Composante(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=250)
    site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'composantes'


class Diplome(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=7)
    libelle = models.CharField(max_length=250)

    class Meta:
        # managed = False
        db_table = 'diplomes'


class Individu(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    login = models.CharField(max_length=20)
    civilite = models.CharField(max_length=5)

    class Meta:
        # managed = False
        db_table = 'individus'


class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=250)

    class Meta:
        db_table = 'themes'


class Niveau(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=250)
    grade = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'niveaux'


class Promotion(models.Model):
    anneeuniversitaire = models.IntegerField()
    composante = models.ForeignKey(Composante, on_delete=models.DO_NOTHING)
    diplome = models.ForeignKey(Diplome, on_delete=models.DO_NOTHING)
    niveau = models.ForeignKey(Niveau)
    anneeetude = models.IntegerField()
    effectif = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'promotions'


class Formation(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Individu)
    theme = models.ForeignKey(Theme)
    promotion = models.ForeignKey(Promotion)
    commentaires = models.CharField(max_length=5000)
    anneeuniversitaire = models.IntegerField()
    site = models.ForeignKey(Site)
    composante = models.ForeignKey(Composante)
    niveau = models.ForeignKey(Niveau)
    anneeetude = models.IntegerField()
    diplome = models.ForeignKey(Diplome)

    class Meta:
        db_table = 'formations'


class Salle(models.Model):
    id = models.AutoField(primary_key=True)
    porte = models.CharField(max_length=250)
    etage = models.CharField(max_length=250)
    batiment = models.ForeignKey(Batiment, on_delete=models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'salles'


class Seance(models.Model):
    id = models.AutoField(primary_key=True)
    debut = models.DateTimeField()
    find = models.DateTimeField()
    visiteguidee = models.BooleanField()
    remarques = models.CharField(max_length=5000)
    formation = models.ForeignKey(Formation)
    salle = models.ForeignKey(Salle)
    participants = models.IntegerField()
    manipulations = models.BooleanField()

    class Meta:
        db_table = 'seances'

