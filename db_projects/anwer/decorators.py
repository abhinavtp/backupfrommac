from django.shortcuts import redirect

def  login_check(func):
    def wrap(request,*args,**kwrgs):
        if not (request.session.get('userid')):
            return redirect("lo")
        else:
            return func(request,*args,**kwrgs)
    return wrap
