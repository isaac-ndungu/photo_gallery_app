from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Photo, Tag
from .forms import PhotoForm

def index_view(request):
    photos = Photo.objects.select_related('owner').prefetch_related('tags').all()
    tags = Tag.objects.all()
    
    # Check if a tag filter is active
    tag_slug = request.GET.get('tag')
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        photos = photos.filter(tags=tag)
        active_tag = tag
    else:
        active_tag = None

    context = {
        'photos': photos,
        'tags': tags,
        'active_tag': active_tag
    }
    return render(request, 'gallery/index.html', context)


def photo_detail_view(request, pk):
    photo = get_object_or_404(Photo.objects.select_related('owner').prefetch_related('tags'), pk=pk)
    context = {
        'photo': photo
    }
    return render(request, 'gallery/photo_detail.html', context)


@login_required
def photo_upload_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.save()
            form.save_m2m() # Save Many-to-Many tags relationships!
            messages.success(request, "Your photo has been uploaded successfully!")
            return redirect('photo_detail', pk=photo.pk)
        else:
            messages.error(request, "Failed to upload photo. Please check the errors below.")
    else:
        form = PhotoForm()

    context = {
        'form': form,
        'title': 'Upload Photo'
    }
    return render(request, 'gallery/photo_form.html', context)


@login_required
def photo_edit_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    
    # Ownership authorization check
    if photo.owner != request.user:
        messages.error(request, "You are not authorized to edit this photo.")
        return redirect('photo_detail', pk=pk)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Your photo details have been updated successfully!")
            return redirect('photo_detail', pk=pk)
        else:
            messages.error(request, "Failed to update photo. Please check the errors below.")
    else:
        form = PhotoForm(instance=photo)

    context = {
        'form': form,
        'photo': photo,
        'title': 'Edit Photo'
    }
    return render(request, 'gallery/photo_form.html', context)


@login_required
def photo_delete_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    
    # Ownership authorization check
    if photo.owner != request.user:
        messages.error(request, "You are not authorized to delete this photo.")
        return redirect('photo_detail', pk=pk)

    if request.method == 'POST':
        photo.delete()
        messages.success(request, "Your photo was successfully deleted.")
        return redirect('index')
        
    context = {
        'photo': photo
    }
    return render(request, 'gallery/photo_confirm_delete.html', context)
