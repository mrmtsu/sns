from django.shortcuts import render

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
      username = request.POST['username']
      print(request.POST)
      return render(request, 'signup.html', {'some':100})

    return render(request, 'signup.html', {'some':100})