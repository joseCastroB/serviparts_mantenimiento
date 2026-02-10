{
    'name': 'Serviparts Mantenimiento',  # Puedes cambiar el nombre si quieres
    'version': '1.0',
    'category': 'Maintenance',
    'summary': 'Extensión para horómetro y tiempos en mantenimiento',
    'depends': ['base', 'maintenance', 'repair'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/maintenance_views.xml',
        'views/equipment_views.xml',
        'views/report_maintenance_jh.xml',
    ],
    'installable': True,
    'application': False,
}