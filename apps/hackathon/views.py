import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import User, Prompt, Solution, Collaboration, Like, Following
from django.db.models import Count

# Create your views here.
def index(request):
    
    list = User.objects.all()
    # for i in list:
    #     print i.email
    return render(request, 'hackathon/index.html')


def register(request):

    if request.method == "POST":
        values = User.objects.register(request.POST)
        if values[0]: 
            request.session['id'] = values[1]
            return redirect("/home")
        else:
            for error in values[1]:
                messages.error(request, error)
            return redirect("/")
    


def login(request):
    if request.method == "POST":
        login = User.objects.login(request.POST)
        # print login
        if login[0]:
            
            request.session['id'] = login[2]
            return redirect('/home')
        else:
            messages.error(request, 'Email or password is incorrect')
            return redirect('/')

def home(request):
    if 'id' in request.session:
        text = "How do you improve an umbrella?"
        
        prompt = Prompt.objects.filter(content = text)
        
        user = User.objects.get(id = request.session['id'])
        content = {
            'first_name': user.first_name,
            'user': user,
            'prompt': prompt
        }
        return render(request, 'hackathon/home.html', content)
    else:
        return redirect('/')

def submit(request, id):
    if request.method == "POST":
        print id
        Solution.objects.createSolution(request.POST, request.session['id'], id)
    return redirect('solutions', id = id)

def solutions(request, id):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        prompt = Prompt.objects.get(id = id)
        solutions = Solution.objects.filter(prompt = prompt).annotate(num_likes = Count('likes')).order_by('-num_likes')
        content = {
            'prompt': prompt,
            'solutions': solutions,
            'user': user
        }
        return render(request, 'hackathon/solutions.html', content)
    else:
        return render('/home')

def like(request, id):
    print "solution " + id
    user = User.objects.get(id = request.session['id'])
    solution = Solution.objects.get(id = id)

    like = Like.objects.create(user = user, solution = solution)
    print 'prompt ' + str(solution.prompt.id)
    return redirect('solutions', id = solution.prompt.id)

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request, id):
    if 'id' in request.session:
        user = User.objects.get(id = id)
        solutions = Solution.objects.filter(user__id = user.id)
        likes = Like.objects.filter(solution__id = 1)
        print likes
        context = {
            "user": user,
            "solutions": solutions,
            "likes": likes
        }

        for i in Solution.objects.all():
            print i.content

    return render(request, 'hackathon/profile.html', context)