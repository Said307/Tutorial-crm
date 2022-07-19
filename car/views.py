from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import DetailView,ListView
# Create your views here.

from .models import *
from .forms import *


class Detail(DetailView):
    model = Car
    template_name ="car/detail.html"

     
class List(ListView):
    model = Car
    template_name ="car/list.html"

     

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        basket =self.request.session["basket"]= {}
        basket["product1"]={}
        basket["product1"]["Price"]=4500
        self.request.session.modified = True

        context["basket"]=basket
        return context





def Create(request):
    if request.method ==  'POST':
        form =  SecondForm(request.POST)
        if form.is_valid():
           
            print("Form is valid !!!!!!!!!!")
            return HttpResponseRedirect('/thanks/')
    else:
        print("Form Not clean ")
        form = SecondForm()
    return render(request,'car/create.html',{"form":form})


