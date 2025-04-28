# Hyperion : Django + HTMX SaaS Boilerplate

<div align="center">
  <img src="https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django 5.0"/>
  <img src="https://img.shields.io/badge/HTMX-Latest-2D79C7?style=for-the-badge&logo=html5&logoColor=white" alt="HTMX"/>
  <img src="https://img.shields.io/badge/Tailwind-3.x-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"/>
  <img src="https://img.shields.io/badge/Alpine.js-3.x-77C1D2?style=for-the-badge&logo=alpine.js&logoColor=white" alt="Alpine.js"/>
  <img src="https://img.shields.io/badge/Stripe-Integration-6772E5?style=for-the-badge&logo=stripe&logoColor=white" alt="Stripe"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License: MIT"/>
</div>

A modern, production-ready Django boilerplate for building SaaS applications with HTMX, Tailwind CSS, and Alpine.js. This template provides everything you need to kickstart your next SaaS project with best practices and modern tooling.



## 🌟 Features

- 🚀 **Django 5.0** with modern best practices and security features
- 🎨 **Tailwind CSS** for beautiful, responsive designs
- ⚡ **HTMX** for dynamic interactions without complex JavaScript
- 🎯 **Alpine.js** for lightweight JavaScript functionality
- 🔐 **User Authentication** with django-allauth
- ✉️ **Email Verification** system
- 📱 **Responsive Landing Page** with modern design
- 👑 **Django Admin Panel** customization
- 💳 **Subscription System** with Stripe integration
- 📊 **User Dashboard** with analytics
- 🔒 **Role-based Access Control**
- 🎨 **Modern UI Components**
- 📈 **SEO Optimization**
- 🔍 **Search Functionality**
- 📱 **Mobile-First Approach**

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/eriktaveras/django-saas-boilerplate.git
cd django-saas-boilerplate
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

6. **Run the development server:**
```bash
python manage.py runserver
```

Visit http://localhost:8000 to see your application!

## 📁 Project Structure

```
├── core/                 # Main Django project
│   ├── settings/        # Django settings
│   ├── urls.py         # URL configuration
│   └── wsgi.py         # WSGI configuration
├── apps/                # Django applications
│   ├── accounts/       # User authentication
│   ├── landing/        # Landing page
│   ├── dashboard/      # User dashboard
│   └── subscriptions/  # Subscription management
├── static/             # Static files
│   ├── css/           # CSS files
│   ├── js/            # JavaScript files
│   └── images/        # Image assets
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── components/    # Reusable components
│   └── pages/         # Page templates
└── manage.py          # Django management script
```

## 🛠️ Technology Stack

- **Backend:** Django 5.0
- **Frontend:** HTMX, Alpine.js
- **Styling:** Tailwind CSS
- **Database:** PostgreSQL (recommended)
- **Authentication:** django-allauth
- **Payments:** Stripe
- **Email:** SendGrid (recommended)


## 🤝 Contributing

We love your input! We want to make contributing to Django SaaS Boilerplate as easy and transparent as possible. Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Maintainer

<div align="center">
  <img src="https://github.com/eriktaveras.png" width="100px" style="border-radius: 50%;" alt="Erik Taveras">
</div>

**Erik Taveras** - Full Stack Solutions Developer

- 🌐 Website: [www.eriktaveras.com](https://www.eriktaveras.com)
- 📧 Email: [hello@eriktaveras.com](mailto:hello@eriktaveras.com)
- 💻 GitHub: [@eriktaveras](https://github.com/eriktaveras)
- 🔗 LinkedIn: [Erik Taveras](https://linkedin.com/in/eriktaveras)

Specialized in Python, Django, and building scalable web applications and API solutions for businesses and startups.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [HTMX](https://htmx.org/)
- [Alpine.js](https://alpinejs.dev/)
- [Stripe](https://stripe.com/)
- [Font Awesome](https://fontawesome.com/)
- [Space Grotesk Font](https://fonts.google.com/specimen/Space+Grotesk)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=eriktaveras/django-saas-boilerplate&type=Date)](https://www.star-history.com/#eriktaveras/django-saas-boilerplate&Date)

## 📫 Contact & Support

If you have any questions or suggestions, please:

- 📝 Open an issue
- 📧 Reach out at [hello@eriktaveras.com](mailto:hello@eriktaveras.com)
- 🐦 Follow [@eriktaveras](https://twitter.com/eriktaveras) on Twitter

<div align="center">
  <p>Built with ❤️ by <a href="https://www.eriktaveras.com">Erik Taveras</a></p>
</div> 
