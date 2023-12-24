from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Media, CompletedMedia, NotCompletedMedia, Anime, CompletedAnime, NotCompletedAnime, PriorityMedia, PriorityAnime
#from django.contrib import messages
from django.db.models import Q

@login_required
def home(request):
    priority_media_list = PriorityMedia.objects.all()
    priority_anime_list = PriorityAnime.objects.all()
    
    context = {
        'priority_media_list': priority_media_list, 
        'priority_anime_list': priority_anime_list,
    } 
    
    return render(request, 'mylist/home.html', context)

@login_required
def search(request):
    return render(request, 'mylist/search.html')

@login_required
def add_media(request):
    #messages.clear(request)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        poster = request.POST.get('poster')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        
        media_exists = Media.objects.filter(title=title).exists()
        if media_exists:
            #messages.error(request, 'Media already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Media already exists on the list.'})
        
        completed_media_exists = CompletedMedia.objects.filter(comp_title=title).exists()
        if completed_media_exists:
            #messages.error(request, 'Media already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Media already exists on the list.'})
        
        not_completed_media_exists = NotCompletedMedia.objects.filter(notcomp_title=title).exists()
        if not_completed_media_exists:
            #messages.error(request, 'Media already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Media already exists on the list.'})
        
        priority_media_exists = PriorityMedia.objects.filter(priority_title=title).exists()
        if priority_media_exists:
            #messages.error(request, 'Media already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Media already exists on priority list.'})
            
        media = Media(title=title, poster=poster, year=year, genre=genre)
        media.save()

        #messages.success(request, 'Media added to the list.')
        return JsonResponse({'status': 'success', 'message': 'Media added to the list.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def personallist(request):
    #media_list = Media.objects.all()  
    #completed_list = CompletedMedia.objects.all()
    #not_completed_list = NotCompletedMedia.objects.all()
    
    #ontext = {
        #'media_list': media_list, 
        #'completed_list': completed_list,
        #'not_completed_list': not_completed_list
    #} 
    
    #return render(request, 'mylist/personallist.html', context)
    
    genre_filter = request.GET.get('genre', '')  # Get the genre filter value from the request

    media_list = Media.objects.all()

    if genre_filter:
        media_list = media_list.filter(Q(genre__icontains=genre_filter))

    completed_list = CompletedMedia.objects.all()

    if genre_filter:
        completed_list = completed_list.filter(Q(comp_genre__icontains=genre_filter))

    not_completed_list = NotCompletedMedia.objects.all()

    if genre_filter:
        not_completed_list = not_completed_list.filter(Q(notcomp_genre__icontains=genre_filter))
        
    priority_media_list = PriorityMedia.objects.all()

    context = {
        'media_list': media_list,
        'completed_list': completed_list,
        'not_completed_list': not_completed_list,
        'priority_media_list': priority_media_list,
        'genre_filter': genre_filter,  # Pass the genre filter value to the template
    }

    return render(request, 'mylist/personallist.html', context)

@login_required
def remove_media(request, id):
    media = Media.objects.get(id=id)
    media.delete()
    
    return redirect('mylist-personallist')

@login_required
def remove_completed(request, id):
    completed = CompletedMedia.objects.get(id=id)
    completed.delete()
    
    return redirect('mylist-personallist')

@login_required
def remove_notcompleted(request, id):
    notcompleted = NotCompletedMedia.objects.get(id=id)
    notcompleted.delete()
    
    return redirect('mylist-personallist')
    
@login_required
def completed_media(request, id):
    media = Media.objects.get(id=id)
    completed_media = CompletedMedia(
        comp_title=media.title,
        comp_poster=media.poster,
        comp_year=media.year,
        comp_genre=media.genre
    )
    
    completed_media.save()
    media.delete()
    return redirect('mylist-personallist')

@login_required
def not_completed_media(request, id):
    media = Media.objects.get(id=id)
    not_completed_media = NotCompletedMedia(
        notcomp_title=media.title,
        notcomp_poster=media.poster,
        notcomp_year=media.year,
        notcomp_genre=media.genre
    )
    not_completed_media.save()
    media.delete()
    return redirect('mylist-personallist')

@login_required
def not_completed_to_completed(request, id):
    not_completed_media = NotCompletedMedia.objects.get(id=id)
    completed_media = CompletedMedia(
        comp_title=not_completed_media.notcomp_title,
        comp_poster=not_completed_media.notcomp_poster,
        comp_year=not_completed_media.notcomp_year,
        comp_genre=not_completed_media.notcomp_genre
    )
    completed_media.save()
    not_completed_media.delete()
    return redirect('mylist-personallist')

@login_required
def animelist(request):
    #anime_list = Anime.objects.all()  
    #completed_anime_list = CompletedAnime.objects.all()
    #not_completed_anime_list = NotCompletedAnime.objects.all()
    
    #context = {
        #'anime_list': anime_list, 
        #'completed_anime_list': completed_anime_list,
        #'not_completed_anime_list': not_completed_anime_list
    #} 
    
    #return render(request, 'mylist/animelist.html', context)
    
    genre_filter = request.GET.get('genre', '')  # Get the genre filter value from the request

    anime_list = Anime.objects.all()

    if genre_filter:
        anime_list = anime_list.filter(Q(animegenre__icontains=genre_filter))

    completed_anime_list = CompletedAnime.objects.all()

    if genre_filter:
        completed_anime_list = completed_anime_list.filter(Q(comp_anime_genre__icontains=genre_filter))

    not_completed_anime_list = NotCompletedAnime.objects.all()

    if genre_filter:
        not_completed_anime_list = not_completed_anime_list.filter(Q(notcomp_anime_genre__icontains=genre_filter))
        
    priority_anime_list = PriorityAnime.objects.all()

    context = {
        'anime_list': anime_list,
        'completed_anime_list': completed_anime_list,
        'not_completed_anime_list': not_completed_anime_list,
        'priority_anime_list': priority_anime_list,
        'genre_filter': genre_filter,  # Pass the genre filter value to the template
    }

    return render(request, 'mylist/animelist.html', context)

@login_required
def add_anime(request):
    #messages.clear(request)
    
    if request.method == 'POST':
        animetitle = request.POST.get('animetitle')
        animeposter = request.POST.get('animeposter')
        animeyear = request.POST.get('animeyear')
        animegenre = request.POST.get('animegenre')
        
        anime_exists = Anime.objects.filter(animetitle=animetitle).exists()
        if anime_exists:
            #messages.error(request, 'Anime already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Anime already exists on the list.'})
        
        completed_anime_exists = CompletedAnime.objects.filter(comp_anime_title=animetitle).exists()
        if completed_anime_exists:
            #messages.error(request, 'Anime already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Anime already exists on the list.'})
        
        not_completed_anime_exists = NotCompletedAnime.objects.filter(notcomp_anime_title=animetitle).exists()
        if not_completed_anime_exists:
            #messages.error(request, 'Anime already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Anime already exists on the list.'})
        
        priority_anime_exists = PriorityAnime.objects.filter(priority_anime_title=animetitle).exists()
        if priority_anime_exists:
            #messages.error(request, 'Media already exists on the list.')
            return JsonResponse({'status': 'error', 'message': 'Media already exists on priority list.'})
            
        anime = Anime(animetitle=animetitle, animeposter=animeposter, animeyear=animeyear, animegenre=animegenre)
        anime.save()

        #messages.success(request, 'Anime added to the list.')
        return JsonResponse({'status': 'success', 'message': 'Anime added to the list.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@login_required
def remove_anime(request, id):
    anime = Anime.objects.get(id=id)
    anime.delete()
    
    return redirect('mylist-animelist')

@login_required
def remove_completed_anime(request, id):
    completed = CompletedAnime.objects.get(id=id)
    completed.delete()
    
    return redirect('mylist-animelist')

@login_required
def remove_notcompleted_anime(request, id):
    notcompleted = NotCompletedAnime.objects.get(id=id)
    notcompleted.delete()
    
    return redirect('mylist-animelist')

@login_required
def completed_anime(request, id):
    anime = Anime.objects.get(id=id)
    completed_anime = CompletedAnime(
        comp_anime_title=anime.animetitle,
        comp_anime_poster=anime.animeposter,
        comp_anime_year=anime.animeyear,
        comp_anime_genre=anime.animegenre
    )
    completed_anime.save()
    anime.delete()
    return redirect('mylist-animelist')

@login_required
def not_completed_anime(request, id):
    anime = Anime.objects.get(id=id)
    not_completed_anime = NotCompletedAnime(
        notcomp_anime_title=anime.animetitle,
        notcomp_anime_poster=anime.animeposter,
        notcomp_anime_year=anime.animeyear,
        notcomp_anime_genre=anime.animegenre
    )
    not_completed_anime.save()
    anime.delete()
    return redirect('mylist-animelist')

@login_required
def not_completed_to_completed_anime(request, id):
    not_completed_anime = NotCompletedAnime.objects.get(id=id)
    completed_anime = CompletedAnime(
        comp_anime_title=not_completed_anime.notcomp_anime_title,
        comp_anime_poster=not_completed_anime.notcomp_anime_poster,
        comp_anime_year=not_completed_anime.notcomp_anime_year,
        comp_anime_genre=not_completed_anime.notcomp_anime_genre
    )
    completed_anime.save()
    not_completed_anime.delete()
    return redirect('mylist-animelist')

@login_required
def priority_media(request, id):
    not_completed_media = NotCompletedMedia.objects.get(id=id)
    priority_watch_media = PriorityMedia(
        priority_title=not_completed_media.notcomp_title,
        priority_poster=not_completed_media.notcomp_poster,
        priority_year=not_completed_media.notcomp_year,
        priority_genre=not_completed_media.notcomp_genre
    )
    priority_watch_media.save()
    not_completed_media.delete()
    return redirect('mylist-personallist')

@login_required
def priority_anime(request, id):
    not_completed_anime = NotCompletedAnime.objects.get(id=id)
    priority_watch_anime = PriorityAnime(
        priority_anime_title=not_completed_anime.notcomp_anime_title,
        priority_anime_poster=not_completed_anime.notcomp_anime_poster,
        priority_anime_year=not_completed_anime.notcomp_anime_year,
        priority_anime_genre=not_completed_anime.notcomp_anime_genre
    )
    priority_watch_anime.save()
    not_completed_anime.delete()
    return redirect('mylist-animelist')

@login_required
def remove_priority_media(request, id):
    priority = PriorityMedia.objects.get(id=id)
    priority.delete()
    
    return redirect('mylist-home')

@login_required
def remove_priority_anime(request, id):
    priority = PriorityAnime.objects.get(id=id)
    priority.delete()
    
    return redirect('mylist-home')

@login_required
def priority_media_to_completed(request, id):
    priority_media = PriorityMedia.objects.get(id=id)
    completed_media = CompletedMedia(
        comp_title=priority_media.priority_title,
        comp_poster=priority_media.priority_poster,
        comp_year=priority_media.priority_year,
        comp_genre=priority_media.priority_genre
    )
    completed_media.save()
    priority_media.delete()
    return redirect('mylist-home')

@login_required
def priority_anime_to_completed_anime(request, id):
    priority_anime = PriorityAnime.objects.get(id=id)
    completed_anime = CompletedAnime(
        comp_anime_title=priority_anime.priority_anime_title,
        comp_anime_poster=priority_anime.priority_anime_poster,
        comp_anime_year=priority_anime.priority_anime_year,
        comp_anime_genre=priority_anime.priority_anime_genre
    )
    completed_anime.save()
    priority_anime.delete()
    return redirect('mylist-home')
