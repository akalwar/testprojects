from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from .forms import UserForm

 # Create your views here.

"""
    def index(request):
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums,})
    
    def detail(request, pk):
        #album = Album.objects.get(pk=pk)
        album = get_object_or_404(Album, pk=pk)
        return render(request, 'music/detail.html', {'album': album,})
    
    def favorite(request, pk):
        album = get_object_or_404(Album, pk=pk)
        try:
            selected_song = album.song_set.get(pk=request.POST['song'])
        except(KeyError, Song.DoesNotExist):
            return render(request, 'music/detail.html', {
                'album': album,
                'error_message': "You did not selected a valid song",
            })
        else:
            selected_song.favorite = True
            selected_song.save()
            return render(request, 'music/detail.html', {'album': album,})
"""

from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genere', 'album_logo',]

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genere', 'album_logo',]

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
    fields = ['artist', 'title', 'genere', 'album_logo',]

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #to display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #cleaning user data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User object if credentials are correct
            user = authenticate(username= username, password= password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})