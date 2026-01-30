{
    'name': 'Serviparts Mantenimiento',  # Puedes cambiar el nombre si quieres
    'version': '1.0',
    'category': 'Maintenance',
    'summary': 'Extensión para horómetro y tiempos en mantenimiento',
    'depends': ['base', 'maintenance'],
    'data': [
        'views/maintenance_views.xml',
    ],
    'installable': True,
    'application': False,
}