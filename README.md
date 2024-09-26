# VPNMiddleware for Django

This project implements middleware for Django that blocks access from users with IP addresses associated with VPN services. If a user's IP address matches any in the `vpn_ip_list`, they are redirected to the `/vpn-blocked/` page.

## How It Works

1. **Middleware Initialization:**
   - The `VPNMiddleware` class takes a `get_response` function during initialization, which is called after the IP address check.

2. **IP Address List:**
   - Inside the class, a list of VPN-associated IP addresses (`vpn_ip_list`) is defined, which will be blocked.

3. **IP Address Check:**
   - The `__call__` method checks the user's IP address. If the IP address is found in the `vpn_ip_list`, the user is redirected to the `/vpn-blocked/` page.

## Usage

To use this middleware in your Django project:

1. Save the code to a file, such as `vpn_middleware.py`, in your project directory.

2. Register the middleware in your Django settings (`settings.py`):

   ```python
   MIDDLEWARE = [
       # ... other middleware
       'your_project.vpn_middleware.VPNMiddleware',
       # ... other middleware
   ]
   ```


## Contact

* Instagram: @ayhan_web_developer
* Youtube: @ayhan_web_developer
* Telegram: @ayhan_web_developer