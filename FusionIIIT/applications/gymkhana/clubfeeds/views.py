from django.shortcuts import render , HttpResponse , get_object_or_404 ,redirect
from django.http import  HttpResponseRedirect,JsonResponse
from .models import Post , Comment
from applications.gymkhana.models import Club_info
from django.views.decorators.http import require_GET
# Create your views here.
def addPost(request):
    if request.method == 'POST':
        print("request.POST:", request.POST)
        print("request.FILES:", request.FILES)
        video = request.FILES.get('reel')
        image = request.FILES.get('image')
        text = request.POST.get('desc')
        club_name = request.POST.get('club')

        print(club_name)
        file_type = ""
        club = Club_info.objects.get(club_name=club_name)
        print(club)

        print("video variable:", video)
        print("image variable:", image)
        print("text variable:", text)


        post = Post(
            user=request.user,
            club=club,
            filetype=file_type,
            description=text
        )
        if video:
            post.file.save(video.name, video)
            post.file_type = "video"
        elif image:
            post.file.save(image.name, image)
            post.file_type = "image"

        # debug statements
        print("file saved:", post.file.name)

        # check if the image file was uploaded and saved to the file attribute
        post.save()
    return HttpResponseRedirect('/gymkhana/')

def like(request , post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like(request.user)
    return HttpResponseRedirect('/gymkhana/')


# def add_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         comment = Comment(user=request.user, post=post, text=text)
#         comment.save()
#         return HttpResponseRedirect('/gymkhana/')
    

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # comments = post.comments.order_by('-date')

    if request.method == 'POST':
        comment_content = request.POST['comment']
        comment = Comment.objects.create(post=post,author = request.user ,text=comment_content)
        comment.save()
        return HttpResponseRedirect('/gymkhana/')

    return HttpResponseRedirect('/gymkhana/')