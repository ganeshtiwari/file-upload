from django.shortcuts import render
from django.conf import settings
from .models import FileModel
from .forms import FileForm


# Create your views here.
def index(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print('validated')
            form.save()
    return render(request, 'index.html', {'form': form})


def files(request):
    image_ext = ['png', 'jpeg', 'jpg', 'gif']
    image_obj = []
    other_obj = []
    media_url = 'http://localhost:8000' + settings.MEDIA_URL
    objects = FileModel.objects.all()
    for obj in objects:
        if str(obj.file).split('.')[-1] in image_ext:
            image_obj.append(media_url + str(obj.file))
        else:
            other_obj.append(media_url + str(obj.file))

    return render(request, 'files.html', {'image_obj': image_obj, 'other_obj': other_obj})
