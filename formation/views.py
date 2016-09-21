from django.shortcuts import render



def login_view(request):

    return render(request, 'index.html',
    {

    })


def logout_view(request):

    return render(request, 'index.html',
    {

    })


def index_view(request):

    return render(request, 'index.html',
    {

    })






def formation_view(request, formation=None):

    return render(request, 'formation/index.html',
                  {

                  })


def formationAdd_view(request):

    return render(request, 'formation/add.html',
                  {

                  })






def seance_view(request, seance):

    return render(request, 'seance.html',
                  {

                  })







def stat_view(request):

    return render(request, 'stat.html',
                  {

                  })





def admin_view(request):

    return render(request, 'admin.html',
                  {

                  })

