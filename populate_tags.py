import os
import django

# 1. Setup Django Environment
# Make sure 'photo_gallery_app.settings' matches your actual settings module.
# You can find the correct string inside your manage.py file!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galleryproject.settings')
django.setup()

# 2. Import your Tag model
# IMPORTANT: Adjust 'gallery' if your app is named differently (e.g., 'photos')
from gallery.models import Tag 

def populate():
    # A list of common tags to populate the DB with
    initial_tags = [
        'Nature', 'Portrait', 'Architecture', 'Animals', 
        'Travel', 'Food', 'Events', 'Sports', 
        'Art', 'Abstract', 'Black & White', 'Wedding',
        'Street Photography', 'Landscape', 'Macro'
    ]

    print("Starting to populate tags...")
    
    for tag_name in initial_tags:
        # get_or_create ensures we don't create duplicates if run multiple times
        tag, created = Tag.objects.get_or_create(name=tag_name)
        if created:
            print(f'✅ Successfully created tag: {tag_name}')
        else:
            print(f'ℹ️ Tag already exists: {tag_name}')

if __name__ == '__main__':
    populate()
    print("Done!")
