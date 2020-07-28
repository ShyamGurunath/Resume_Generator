from django.shortcuts import render
import pdfkit
import io 
from django.http import HttpResponse
from django.template import loader
from django.utils.crypto import get_random_string
from django.conf import settings
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
          config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
          pdf = pdfkit.from_string(html, False, options,confiuration=config)
          response = HttpResponse(pdf, content_type='application/pdf')
          response['Content-Disposition'] = 'attachment'
          id_map = get_random_string(length=8)
          filename = 'res.pdf'
          return response
     return render(request,'rs.html')
          

# pdfkit_config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
# wk_options = {
#     'page-size': 'Letter',
#     'orientation': 'landscape',
#     'title': title,
#     # In order to specify command-line options that are simple toggles
#     # using this dict format, we give the option the value None
#     'no-outline': None,
#     'disable-javascript': None,
#     'encoding': 'UTF-8',
#     'margin-left': '0.1cm',
#     'margin-right': '0.1cm',
#     'margin-top': '0.1cm',
#     'margin-bottom': '0.1cm',
#     'lowquality': None,
# }

# # We can generate the pdf from a url, file or, as shown here, a string
# pdfkit.from_string(
#     # This example uses Django's render_to_string function to return the result of
#     # rendering an HTML template as a string, which we can then pass to pdfkit and on
#     # into wkhtmltopdf
#     input=render_to_string('reportPDF.html', context=params, request=request),
#     # We can output to a variable or a file – in this case, we're outputting to a file
#     output_path=os.path.join('filepath', 'filename'),
#     options=wk_options,
#     configuration=pdfkit_config
# )
