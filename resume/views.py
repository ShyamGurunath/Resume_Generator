from django.shortcuts import render
import pdfkit
import io 
from django.http import HttpResponse
from django.template import loader
from django.utils.crypto import get_random_string
# Create your views here.


def rs(request):
     if request.method == 'POST':
          name = request.POST.get('Name')
          email = request.POST.get('email')
          name2 = request.POST.get('Name2')
          select = request.POST.get('select')
          print(select)
          template = loader.get_template(f"{select}.html")
          html = template.render({
              'name': name,
              'email': email,
              'name2': name2,
              'select':select,
          })
          options = {
          'page-size': 'Letter',
          'encoding': 'UTF-8',
               }
          config = pdfkit.configuration(
              wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
          pdf = pdfkit.from_string(html, False, options, configuration=config)
          response = HttpResponse(pdf, content_type='application/pdf')
          response['Content-Disposition'] = 'attachment'
          id_map = get_random_string(length=8)
          filename = 'res.pdf'
          return response
     return render(request,'rs.html')
          
