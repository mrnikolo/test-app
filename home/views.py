from django.shortcuts import render, redirect
from django.views import View
from .models import Text
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import TextUpdateForm


# Create your views here.
class HomeView(View):
    def get(self, request):
        text = Text.objects.all()
        return render(request, 'home/home.html', {'text':text})


class DetailView(View):
    def get(self, request, text_id, text_slug):
        text = Text.objects.get(id=text_id, slug=text_slug)
        return render(request, 'home/detail.html', {'text': text})


class DeleteTextView(LoginRequiredMixin, View):
    def get(self, request, text_id):
        text = Text.objects.get(pk=text_id)
        if text.user.id == request.user.id:
            text.delete()
            messages.success(request, 'text deleted successfully ', 'success')
        else:
            messages.error(request, 'you can delete this text', 'warning')
        
        return redirect('home:home')


class UpdateTextView(LoginRequiredMixin, View):
    form_class = TextUpdateForm
    
    def dispatch(self, request, *args, **kwargs):
        text = Text.objects.get(pk=kwargs['text_id'])
        if not text.user.id == request.user.id:
            messages.error(request, 'you can update this Text', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, text_id):
        text = Text.objects.get(pk=text_id)
        form = self.form_class(instance=text)
        return render(request, 'home/update.html', {'form': form})

    def post(self, request, text_id):
        pass



    


