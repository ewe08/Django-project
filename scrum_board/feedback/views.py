from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('homepage:home')

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form: FeedbackForm):
        data = form.cleaned_data
        Feedback(user=self.request.user, text=data['text']).save()
        send_mail('We have reciewed your feedback!',
                  data['text'],
                  settings.DEFAULT_FROM_EMAIL,
                  [self.request.user.email])
        return super().form_valid(form)
