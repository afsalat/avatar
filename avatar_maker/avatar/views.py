from django.shortcuts import render, redirect
import requests
from .models import Avatar_pic
from .cartooner import Cartoonizer
import os, cv2
from .forms import AvatarForm
import avatar_maker.settings as settings


def upload_image(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save()
            avatar_path = avatar.image.path


            # the below comment code using with DeepAI

            # url = 'https://api.deepai.org/api/toonify'
            # headers = {'api-key': '1c2f425c-b8f6-42ae-b1c4-15791608429a'}
            # files = {'image': open(avatar_path, 'rb')}
            
            # response = requests.post(url, files=files, headers=headers)
            # # return response.json()

            # # Save the generated 3D model
            # if response.status_code == 200:
            #     print(response.content)
            #     with open(avatar_path, "wb") as file:
            #         file.write(response.content)
            #         avatar.cartoon_img.name = f"avatars/cartoon/cartoon_{os.path.basename(avatar.image.name)}"
            #         avatar.save()
            #         # return redirect('view_avatar', avatar_id=avatar.id)
            # else:
            #     print("Error:", response.status_code, response.text)
            #     # return redirect('view_avatar', avatar_id=avatar.id)




            # Apply cartoon effect
            cartoonizer = Cartoonizer()
            cartoon_result = cartoonizer.render(avatar_path)

            cartoon_path = os.path.join(settings.MEDIA_ROOT, 'avatars/cartoon', f"cartoon_{os.path.basename(avatar.image.name)}")
            cv2.imwrite(cartoon_path, cartoon_result)

            # Update the avatar object with the correct cartoon image path
            avatar.cartoon_img.name = f"avatars/cartoon/cartoon_{os.path.basename(avatar.image.name)}"
            avatar.save()

            return redirect('view_avatar', avatar_id=avatar.id)

    else:
        form = AvatarForm()

    return render(request, 'uploads_image.html', {'form': form})

def view_avatar(request, avatar_id):
    avatar = Avatar_pic.objects.get(id=avatar_id)
    return render(request, 'view_avatar.html', {'avatar': avatar})
