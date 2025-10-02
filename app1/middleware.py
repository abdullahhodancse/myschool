from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.utils import timezone
from .models import Subscription


class SubscriptionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        if not request.user.is_authenticated:
            return None
        
        if request.path =='/app1/no/':
            return None


        try:
           
            subscription = Subscription.objects.filter(
                user=request.user, is_active=True
            ).latest('end_date')

            
            if subscription.type == 'free':
                if subscription.end_date and subscription.end_date < timezone.now():
                    return redirect('/app1/no/')

            
            
        except Subscription.DoesNotExist:
            
            return redirect('/no_subs/')

        return None
