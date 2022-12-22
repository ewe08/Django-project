from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form: FeedbackForm):
        data = form.cleaned_data
        Feedback(user=self.request.user, text=data['text']).save()
        send_mail("We have reviewed your feedback!",
                  data['text'],
                  )
        return redirect(reverse('homepage:home'))
