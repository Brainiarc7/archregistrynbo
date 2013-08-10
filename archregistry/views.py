from django.views.generic import ListView

from archregistry.views import ArchUser


class ArchUserListView(ListView):

    model = ArchUser
