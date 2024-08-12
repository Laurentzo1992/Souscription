from django.db import models


class Souscripteur(models.Model):
    
    type_personne = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    contact2 = models.CharField(max_length=50, blank=True, null=True)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    type_piece = models.CharField(max_length=50)
    reference_piece = models.CharField(max_length=50)
    date_delivrance = models.DateField()
    situation_matrimoniale = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    photo = models.FileField(upload_to="photo_souscripteur", blank=True, null=True)
    date_saisie = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    date_suppr = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Projet(models.Model):
    
    libelle = models.TextField()

    def __str__(self):
        return self.libelle
    

    

class Souscription(models.Model):
    
    id_souscripteur = models.ForeignKey(Souscripteur, on_delete=models.CASCADE)
    numero_souscription = models.CharField(max_length=50)
    projet_a_souscrire = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_souscription = models.DateTimeField()
    nbre_part_souscrit = models.IntegerField()
    montant_total = models.FloatField()
    montant_verse = models.FloatField()
    montant_restant = models.FloatField()
    lieu_souscription = models.CharField(max_length=50)
    moyen_paiement = models.CharField(max_length=50)
    ref_paiement = models.CharField(max_length=50)
    mode_souscription = models.CharField(max_length=50)
    echeance = models.DateField()
    pj1 = models.FileField(upload_to="pieces_jointes", blank=True, null=True, verbose_name="pièce jointe 1")
    pj2 = models.FileField(upload_to="pieces_jointes", blank=True, null=True, verbose_name="pièce jointe 2")
    pj3 = models.FileField(upload_to="pieces_jointes", blank=True, null=True, verbose_name="pièce jointe 3")
    observation = models.CharField(max_length=50, blank=True, null=True)
    date_saisie = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    date_suppr = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.numero_souscription

