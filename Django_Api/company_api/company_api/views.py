from django.http import HttpResponse, JsonResponse

def home_page(request): 
    print("Home page requested")
    friends = [
        'Ankit', 
        'ravi',
        'uttam'
    ]
    # return HttpResponse ("<h1>This is home page </h1>")
    return JsonResponse (friends,safe=False)  # trying to sent json response direct 