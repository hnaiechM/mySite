from django.db import models
from datetime import date

class Categorie(models.Model):
    TYPE_CHOICES=[
        ('Al','Alimentaire'), ('Mb','Meuble'),
        ('Sn','Sanitaire'), ('Vs','Vaisselle'),
        ('Vt','Vêtement'),('Jx','Jouets'),
        ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')
    ]

    name=models.CharField(max_length=50,default='Al')

    def __str__(self):
        return f'{self.name}'



class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return f'{self.nom} - {self.adresse} - {self.email} - {self.telephone}'


class Produit(models.Model):
    libelle= models.CharField(max_length = 100)
    description = models.TextField(default='Non definie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    img=models.ImageField(blank=True)

    TYPE_CHOICES = [
        ('em', 'emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conserve')
    ]
    type = models.CharField(max_length=2, default="em", choices=TYPE_CHOICES)


    categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True) 
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.libelle} - {self.description} - {self.prix} - {self.type}- {self.categorie}'


class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.libelle} - {self.description} - {self.prix} - {self.type}- {self.categorie}- {self.Duree_garantie}'

class ProduitC(Produit):
    def __str__(self):
        return f'{self.libelle} - {self.description} - {self.prix} - {self.type}- {self.categorie}'

class Commande(models.Model):
    dateCde=models.DateField(null=True, default=date.today())
    totalCde=models.DecimalField(max_digits=10, decimal_places=3)
    produit=models.ManyToManyField(Produit)
    def __str__(self):
        return f'{self.totalCde} - {self.dateCde} - {self.produit}'