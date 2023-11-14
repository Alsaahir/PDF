from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import pdfkit


config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


def index(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.html')


def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('resume')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response