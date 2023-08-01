from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Label
from .forms import LabelForm, MultiLevelFormSet
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    return HttpResponse("first view")

class EtiquetaListView(ListView):
    model = Label
    template_name = 'label_list.html'
    context_object_name = 'labels'

class labelCreateView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = "label_form.html"
    success_url = '/add_label/'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)

        context['level_form_set'] = MultiLevelFormSet
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        level_form_set = MultiLevelFormSet(self.request.POST)

        if form.is_valid() and level_form_set.is_valid():
            return self.form_valid(form, level_form_set)
        else:
            return self.form_invalid(form, level_form_set)
                
    def form_valid(self, form, level_form_set):
        self.object = form.save(commit=False)
        self.object.save()

        labels = level_form_set.save(commit=False)
        for label in labels:
            label.level = self.object
            label.save()
        return redirect(reverse_lazy("label_form.html"))
    
    def form_invalid(self, form, level_form_set):
        return self.render_to_response(self.get_context_data(form=form, level_form_set= level_form_set))
            


class labelUpdateView(UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "label_form.html"
    success_url = reverse_lazy("label_form.html")


class labelDeleteView(DeleteView):
    model = Label
    template_name = 'etiqueta_confirm_delete.html'
    success_url = '/label_list/'
