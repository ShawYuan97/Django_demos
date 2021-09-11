import os.path

from django.conf import settings
from django.http import HttpResponse, StreamingHttpResponse, Http404
from django.shortcuts import render
from django.utils.encoding import escape_uri_path
from login.models import User

from . import forms
from . import models


# Create your views here.
def affair_index_view(request):
    return render(request, 'affair/index.html', locals())


def submit_View(request):
    message = ''
    if request.method == 'POST':
        form = forms.submitfileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            file = form.cleaned_data.get('file')
            try:
                user = User.objects.get(username=request.session['user_name'])
            except Exception as e:
                print(f'get user error {e}')
                message = '获取用户失败！请重试'
                return render(request, 'affair/submit_file.html', locals())
            instance = models.Submit_File_Model()
            instance.title = title
            instance.file = file
            instance.file_user = user
            instance.save()
            message = '提交成功！'
            # return HttpResponse(request,'/affair/submit_file',locals())
    else:
        form = forms.submitfileForm()
    return render(request, 'affair/submit_file.html', locals())


def downfile_View(request):
    all_files = models.Submit_File_Model.objects.all()
    return render(request, 'affair/filedown.html', locals())


def downonefile(request, id):
    try:
        file_instance = models.Submit_File_Model.objects.get(id=id)
    except Exception as e:
        print(f'down file error {e}')
        return HttpResponse('下载失败！请重试')
    # print(str(file_instance.file))
    try:
        filepath = str(settings.BASE_DIR)
        filepath += os.path.join(settings.MEDIA_URL, str(file_instance.file))
        filename = filepath.split('/')[-1].encode('utf8')
        print(filename)
        file = open(filepath, 'rb')
        response = StreamingHttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        ## 文件下载一定要加上 escape_uri_path
        response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path(filename))
    except Exception:
        raise Http404
    return response
