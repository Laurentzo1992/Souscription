from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Souscripteur, Souscription, Projet
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from  django.views.decorators.cache import cache_control 
from  django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'souscription/home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def espace(request):
    return render(request, 'souscription/espace.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def demande(request):
    if request.method == 'POST':
        
        # data from souscription model
        type_personne = request.POST.get('type_personne')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        sexe = request.POST.get('sexe')
        contact = request.POST.get('contact')
        contact2 = request.POST.get('contact2')
        date_naissance = request.POST.get('date_naissance')
        lieu_naissance = request.POST.get('lieu_naissance')
        type_piece = request.POST.get('type_piece')
        reference_piece = request.POST.get('reference_piece')
        date_delivrance = request.POST.get('date_delivrance')
        situation_matrimoniale = request.POST.get('situation_matrimoniale')
        residence = request.POST.get('residence')
        nationalite = request.POST.get('nationalite')
        profession = request.POST.get('profession')
        photo = request.FILES.get('photo')
        
        
        # Save Souscripteur
        souscripteur = Souscripteur.objects.create(
            nom=nom,
            prenom=prenom,
            type_personne=type_personne,
            sexe=sexe,
            contact=contact,
            contact2=contact2,
            date_naissance=date_naissance,
            lieu_naissance=lieu_naissance,
            type_piece=type_piece,
            reference_piece=reference_piece,
            date_delivrance=date_delivrance,
            situation_matrimoniale=situation_matrimoniale,
            residence=residence,
            nationalite=nationalite,
            profession=profession,
            photo=photo
        )
        
        # data from souscription model
        numero_souscription = request.POST.get('numero_souscription')
        projet_a_souscrire_id = request.POST.get('projet_a_souscrire')
        projet_a_souscrire = Projet.objects.get(id=projet_a_souscrire_id)
        date_souscription = request.POST.get('date_souscription')
        nbre_part_souscrit = request.POST.get('nbre_part_souscrit')
        montant_total = request.POST.get('montant_total')
        montant_verse = request.POST.get('montant_verse')
        montant_restant = request.POST.get('montant_restant')
        lieu_souscription = request.POST.get('lieu_souscription')
        moyen_paiement = request.POST.get('moyen_paiement')
        ref_paiement = request.POST.get('ref_paiement')
        mode_souscription = request.POST.get('mode_souscription')
        echeance = request.POST.get('echeance')
        pj1 = request.FILES.get('pj1')
        pj2 = request.FILES.get('pj2')
        pj3 = request.FILES.get('pj3')
        observation = request.POST.get('observation')

        # Save Souscription
        Souscription.objects.create(
            id_souscripteur=souscripteur,
            numero_souscription=numero_souscription,
            projet_a_souscrire=projet_a_souscrire,
            date_souscription=date_souscription,
            nbre_part_souscrit=nbre_part_souscrit,
            montant_total=montant_total,
            montant_verse=montant_verse,
            montant_restant=montant_restant,
            lieu_souscription=lieu_souscription,
            moyen_paiement=moyen_paiement,
            ref_paiement=ref_paiement,
            mode_souscription=mode_souscription,
            echeance=echeance,
            pj1=pj1,
            pj2=pj2,
            pj3=pj3,
            observation=observation
        )

        # Redirect to a success page after saving
        return redirect('espace')  
        
    # On GET request, render the form
    projets = Projet.objects.all()
    return render(request, 'souscription/demande.html', {'projets': projets})






@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            # Vérifier si l'utilisateur existe déjà
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ce nom d\'utilisateur est déjà pris.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà utilisé.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                # Connexion automatique de l'utilisateur
                login(request, user)
                # Redirection vers la page de connexion
                messages.success(request, 'operation reussie!')
                return redirect('demande')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas.')

    return render(request, 'souscription/createuser.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.user == None or request.user =="" or request.user.username == "":
        return render(request, "souscription/connexion.html")
    else:
        return HttpResponseRedirect(reverse('login'))
    
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            messages.info(request, "Connexion reussie !")
            return redirect('demande')
        else:
            messages.error(request, "Veuillez réssayer encore et saisir vos informations de connexion: utilisateur et mot de passe correctement.")
            return HttpResponseRedirect(reverse('login'))

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    #deconnection du user avec la methode logout 
    logout(request)
    return redirect('home')