from django.shortcuts import render, HttpResponse, redirect
from .models import Email

def index(request):
	print "got first part done!"
	if id not in request.session:
		request.session['id'] = 0  
	return render(request, 'validation/index.html')

def process(request):
	print "proccessing"
	validation_status = Email.emailManager.validate(**request.POST)

	if validation_status['valid']:
		validated = Email.emailManager.create(email=request.POST['email'])
		request.session['id'] = validated.id
		return redirect('/success')
	else:
		print "error"

		request.session['error_msg'] = validation_status['error_msg']
		return redirect('/')

def success(request):
	print "successful"
	context = {
		'newEmail': Email.emailManager.get(id=request.session['id']),
		'emails': Email.emailManager.all()
	}
	return render(request, 'validation/success.html', context)