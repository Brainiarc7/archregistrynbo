from django.views.generic import ListView

from archregistry.models import ArchUser


class ArchUserListView(ListView):

    model = ArchUser
