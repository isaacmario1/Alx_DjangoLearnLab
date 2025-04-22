# Django Security Enhancements

## ✅ HTTPS & Secure Headers
- Enforced HTTPS via `SECURE_SSL_REDIRECT`
- Added HSTS settings to force HTTPS access
- Secure cookies enabled (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
- Added X-Frame, XSS, and Content-Type header protections

---

## ⚙️ Deployment Notes

### 🔐 Nginx HTTPS Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;  # Redirect to HTTPS
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/ssl/certs/your_cert.crt;
    ssl_certificate_key /etc/ssl/private/your_key.key;

    # Other SSL options...
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
}
