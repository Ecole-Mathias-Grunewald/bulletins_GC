from django.contrib import admin
from bulletins.models import Classe,Eleve,Trimestre,\
    Absence,Discipline,CompetencesConnaissances,Appreciation,\
    CompetencesAppreciations,ListBulletinScolaire,Annee,AvisCollege,Stage,Projet,Bareme,MiseEnPageBulletin,SMTPSettings

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom')

class TrimestreAdmin(admin.ModelAdmin):
    list_display = ('intitule','dateDebut','dateFin','edition','annee')

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('eleve','trimestre','nbRetard','nbAbsenceNonExc','nbAbsenceExc')

class AppreciationAdmin(admin.ModelAdmin):
    list_display = ('eleve','discipline')

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('intitule','show_enseignants','show_classes','dateDebut','dateFin','trimestre','reluPar','relectureActive','correctionsAValider','ordre')
    list_editable = ('ordre',)

class CompetencesConnaissancesAdmin(admin.ModelAdmin):
    list_display = ('id','intitule','discipline')

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom','effectifs','annee','show_tuteur')

class StageAdmin(admin.ModelAdmin):
    list_display = ('eleve','typeStage','trimestre','tuteur')

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('eleve','typeProjet','trimestre','tuteur')

class AvisCollegeAdmin(admin.ModelAdmin):
    list_display = ('eleve','trimestre')

class BaremeAdmin(admin.ModelAdmin):
    list_display = ('intitule',)

class MiseEnPageBulletinAdmin(admin.ModelAdmin):
    list_display = ('intitule',)

class SMTPSettingsAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'from_email', 'is_active')
    fields = ('host', 'port', 'use_tls', 'username', 'password', 'from_email', 'is_active')
    
    def has_add_permission(self, request):
        # Empêcher l'ajout de plusieurs instances
        return not SMTPSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Empêcher la suppression de l'instance unique
        return False

admin.site.register(Classe,ClasseAdmin)
admin.site.register(Annee)
admin.site.register(Absence,AbsenceAdmin)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Trimestre,TrimestreAdmin)
admin.site.register(Discipline,DisciplineAdmin)
admin.site.register(CompetencesConnaissances,CompetencesConnaissancesAdmin)
admin.site.register(Appreciation,AppreciationAdmin)
admin.site.register(CompetencesAppreciations)
admin.site.register(ListBulletinScolaire)
admin.site.register(Stage,StageAdmin)
admin.site.register(Projet,ProjetAdmin)
admin.site.register(Bareme,BaremeAdmin)
admin.site.register(MiseEnPageBulletin,MiseEnPageBulletinAdmin)
admin.site.register(AvisCollege,AvisCollegeAdmin)
admin.site.register(SMTPSettings,SMTPSettingsAdmin)


