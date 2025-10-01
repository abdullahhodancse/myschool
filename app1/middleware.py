from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.utils import timezone
from .models import Subscription


    





class SubscriptionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            
            subscription = Subscription.objects.filter(
                user=request.user, is_active=True
            ).latest('end_date')

            
            if subscription.type == 'free':
                if subscription.end_date < timezone.now():
                    return redirect('/no-subscription/')  

            
            if  subscription.end_date < timezone.now():
                return redirect('/no-subscription/')

        except Subscription.DoesNotExist:
            
            return redirect('/no-subscription/')

        return None
