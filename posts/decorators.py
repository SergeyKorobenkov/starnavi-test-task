import datetime

def user_activity_log(func):
    def wrapper(request, *args, **kwargs):
        print(dir(request))
        if request.user.is_authenticated:
            request.user.last_activity = datetime.datetime.now()
            request.user.save()
            return func(request, *args, **kwargs)
        else:
            return func(request, *args, **kwargs)
    return wrapper