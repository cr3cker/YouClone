from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .services import open_file
from .forms import RegisrationForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_list_video(request):
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "video_hosting/video.html", {"video": _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
    

def add_comment(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    if request.method == 'POST':
        _video.comment_set.create(text=request.POST['text'])
        return redirect('video', pk=pk)
    else:
        return render(request, 'video_hosting/video.html', {'video': _video, 'comments': _video.comment_set.all()})


def register(request):
    if request.method == 'POST':
        form = RegisrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
    else:
        form = RegisrationForm()
    return render(request, 'registration/register.html', {'form': form})


def post_comment(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            _video.comments.create(text=form.cleaned_data['text'], video=_video)
            return redirect('video', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'video_hosting/video.html', {'video': _video, 'form': form})