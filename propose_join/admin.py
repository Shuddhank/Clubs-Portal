from django.contrib import admin
from .models import ExistingClub,ProposedClub,ClubMember

admin.site.register(ExistingClub)
admin.site.register(ProposedClub)
admin.site.register(ClubMember)

