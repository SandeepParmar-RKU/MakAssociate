from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView,UpdateView
from django.views.generic.base import TemplateView
from .forms import *
from .filters import *
from django.db.models import Count
from django.db.models import Q,F
from formtools.wizard.views import SessionWizardView
from django.http import Http404

class HomePage(TemplateView):
    template_name = "index.html"


class BuyerListView(generic.ListView):
    model = Policy
    context_object_name = 'buyer'
    queryset = Policy.objects.all()
    template_name = 'insurance/buyer_list.html'
    
    
    def get_context_data(self,*args, **kwargs):
        context = super(BuyerListView,self).get_context_data(**kwargs)
        context['buyer']=BuyerFilter(self.request.GET,queryset=Policy.objects.all())
        return context

# class BuyerTotals(generic.ListView):
#     model = Buyer
#     context_object_name = 'buyer'
#     queryset = Buyer.objects.all()
#     template_name = 'insurance/buyertotal.html'

#     def get_context_data(self, **kwargs):
#         id_ = self.kwargs.get('id')
#         context = super(BuyerTotals,self).get_context_data(**kwargs)
#         q = Buyer.objects.filter(policybuyer__buyer_id = id_).annotate(total=Sum('policybuyer__buyeramount',))
 
#         context = { 
#             'object_list':q,
          
#         }
#         return context
    


class SellerListView(generic.ListView):
    model = Policy
    context_object_name = 'seller'
    queryset = Policy.objects.all()
    template_name = 'insurance/seller_list.html'

    def get_context_data(self,*args, **kwargs):
        context = super(SellerListView,self).get_context_data(**kwargs)
        context['seller']=SellerFilter(self.request.GET,queryset=Policy.objects.all())
        return context



class PolicyCreateView(generic.CreateView):
    form_class = PolicyForm
    model = Policy
    success_url = "/buyers"
	
    def form_valid(self,form):
        return super(PolicyCreateView,self).form_valid(form)



class PolicyCreateViewseller(generic.CreateView):
    form_class = PolicyForm
    model = Policy
    success_url = "/buyers"
    template_name = 'insurance/policyseller_form.html'

	
    def form_valid(self,form):
        return super(PolicyCreateView,self).form_valid(form)



class PolicyUpdateView(UpdateView):
    form_class = PolicyForm
    model = Policy
    success_url = "/"
    template_name = 'insurance/policy_form.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Policy,id=id_)


class SellerCreateView(generic.CreateView):
    form_class = SellerForm
    model = Seller
    success_url = "/"
	
    def form_valid(self,form):
        return super(SellerCreateView,self).form_valid(form)

class BuyerCreateView(generic.CreateView):
    form_class = BuyerForm
    model = Buyer
    success_url = "/"
	
    def form_valid(self,form):
        return super(BuyerCreateView,self).form_valid(form)

class CompanyCreateView(generic.CreateView):
    form_class = CompanyForm
    model = Company
    success_url = "/"
	
    def form_valid(self,form):
        return super(CompanyCreateView,self).form_valid(form)



class SellerCollectionCreateView(generic.CreateView):
    form_class = SellerCollection
    model = Policy
    success_url = "/sellers"
	
    def form_valid(self,form):
        return super(SellerCollectionCreateView,self).form_valid(form)

    

    # def get_form_kwargs(self):
    #     kwargs = super(BuyerCollectionCreateView, self).get_form_kwargs()
    #     kwargs['seller'] = self.request.policy.seller
    #     return kwargs


class BuyerCollectionCreateView(generic.CreateView):
    form_class = BuyerColletion
    model = Policy
    success_url = '/buyers'

    def form_valid(self,form):
        return super(BuyerCollectionCreateView,self).form_valid(form)



        
    
    
    # def get_form_kwargs(self):
    #     kwargs = super(BuyerCollectionCreateView, self).get_form_kwargs()
    #     kwargs['buyer'] = self.request.policy.buyer
    #     return kwargs