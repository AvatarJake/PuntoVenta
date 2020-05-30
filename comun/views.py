from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone

from producto.models import Producto
from compra.models import Compra, CompraDetalle
from venta.models import Venta, VentaDetalle
from django.views import generic
from django.urls import reverse_lazy

class Home(LoginRequiredMixin, generic.TemplateView):
	template_name = 'base/home.html'
	login_url='/admin/login'
	logout_url='/admin/logout'

class Informes(LoginRequiredMixin, generic.TemplateView):
	template_name = 'base/informes.html'
	login_url='/admin/login'
	logout_url='/admin/logout'

   
    #para el pdf
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_pdf(url_template, contexto={}):
	'''
	Renderiza un template a un documeto PDF'''

	template=get_template(url_template)
	html= template.render(contexto)
	result = BytesIO()
	pdf= pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')

	
class Informe_Productos(generic.TemplateView):

	def get(self, request, *args, **kwrgs):

		producto=Producto.objects.all()
		fecha = timezone.now()
		contexto = {'producto':producto,'fecha':fecha}
		
		
		#return render(request, 'principal/mi_pdf.html', contexto)

		pdf = render_pdf("base/imprimir_productos.html", {"producto":producto,"fecha":fecha})
		#return render(request, 'principal/mi_pdf.html', contexto)

		return HttpResponse(pdf, content_type='application/pdf')	

class Informe_Compras(generic.TemplateView):

	def get(self, request, *args, **kwrgs):

		compra=Compra.objects.all()
		fecha = timezone.now()
		contexto = {'compra':compra,'fecha':fecha}
		
		
		#return render(request, 'principal/mi_pdf.html', contexto)

		pdf = render_pdf("base/imprimir_compras.html", {"compra":compra,"fecha":fecha})
		#return render(request, 'principal/mi_pdf.html', contexto)

		return HttpResponse(pdf, content_type='application/pdf')

class Informe_Ventas(generic.TemplateView):

	def get(self, request, *args, **kwrgs):

		venta=Venta.objects.all()
		fecha = timezone.now()
		contexto = {'venta':venta,'fecha':fecha}
		
		
		#return render(request, 'principal/mi_pdf.html', contexto)

		pdf = render_pdf("base/imprimir_ventas.html", {"venta":venta,"fecha":fecha})
		#return render(request, 'principal/mi_pdf.html', contexto)

		return HttpResponse(pdf, content_type='application/pdf')


