from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserData
from .utils import get_query_results
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['uploaded_file']
        user_data = UserData.objects.create(uploaded_file=uploaded_file)
        return HttpResponseRedirect(reverse('query_file', args=[user_data.pk]))
    return render(request, 'upload_file.html')

def query_file(request, user_data_id):
    user_data = UserData.objects.get(pk=user_data_id)
    if request.method == 'POST':
        query = request.POST.get('query')
        results = get_query_results(user_data.uploaded_file, query)
        return render(request, 'query_results.html', {'results': results})
    return render(request, 'query_file.html', {'user_data': user_data})
