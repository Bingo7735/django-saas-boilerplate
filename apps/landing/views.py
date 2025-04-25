from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf import settings

@require_http_methods(['GET'])
def home(request):
    features = [
        {
            'title': 'Dashboard Intuitivo',
            'description': 'Panel de control fácil de usar con todas tus métricas importantes.',
            'icon': 'chart-bar'
        },
        {
            'title': 'Autenticación Segura',
            'description': 'Sistema de autenticación robusto con verificación de email.',
            'icon': 'shield-check'
        },
        {
            'title': 'Diseño Responsive',
            'description': 'Interfaz moderna que funciona perfectamente en todos los dispositivos.',
            'icon': 'device-mobile'
        },
        {
            'title': 'Suscripciones Flexibles',
            'description': 'Sistema de pagos seguro con Stripe para gestionar suscripciones.',
            'icon': 'credit-card'
        }
    ]
    
    pricing = {
        'monthly_price': '9.99',
        'features': [
            'Acceso completo al dashboard',
            'Soporte prioritario',
            'Características premium',
            'Actualizaciones ilimitadas',
            'API access',
            'Backups diarios'
        ]
    }
    
    return render(request, 'landing/home.html', {
        'features': features,
        'pricing': pricing,
    })

@require_http_methods(['GET'])
def pricing(request):
    return render(request, 'landing/pricing.html')

@require_http_methods(['GET'])
def features(request):
    return render(request, 'landing/features.html') 