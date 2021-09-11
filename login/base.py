from django.shortcuts import redirect


def checkLogin(func):
    # 查看session值,判断用户是否已经登录
    def warpper(request, *args, **kwargs):
        if request.session.get('user_name', False):
            print('已登录！')
            return func(request, *args, *kwargs)
        else:
            print('未登录跳转！')
            return redirect('/index')

    return warpper
