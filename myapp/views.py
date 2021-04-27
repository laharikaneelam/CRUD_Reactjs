from django.http import HttpResponse
def index(request):
    return HttpResponse(" GO to /employee page to view the employee list. ")
