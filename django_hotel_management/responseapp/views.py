
from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            favorite_room = myForm.cleaned_data['favorite_room']
            checkin_date= myForm.cleaned_data['checkin_date']
            checkout_date= myForm.cleaned_data['checkout_date']
            feedback = myForm.cleaned_data['feedback']


            context = {
            'name': name,
            'email': email,
            'favorite_room': favorite_room,
	    'checkin_date': checkin_date,
	    'checkout_date': checkout_date,
            'feedback': feedback,
            }

            template = loader.get_template('thankyou.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'responseform.html', {'form':form});

