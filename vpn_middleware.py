from django.http import HttpResponseRedirect

class VPNMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.vpn_ip_list = [
            # VPN iP Addresses '1.111.111.1'
        ]

    def __call__(self, request):
        if request.path != '/vpn-blocked/':
            vpn_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')).split(',')[0].strip()
            print(f'Информация: Пользователь зашёл на сайт с IP - {vpn_ip}') 
            if vpn_ip in self.vpn_ip_list:
                return HttpResponseRedirect('/vpn-blocked/') 
            
        return self.get_response(request)


# Designed by Ayhan :)
# Instagram: @ayhan_web_developer
# Youtube: @ayhan_web_developer
# Telegram: @ayhan_web_developer