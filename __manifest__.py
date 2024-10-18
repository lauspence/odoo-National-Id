{
    'name': 'National ID',
    'version': '1.0',
    'depends': ['base'],  # Add other dependencies as needed
    'data': [
        'views/national_id_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',  # Specify your desired license here
    'author': 'Lawrence',  # Optional: Specify the author
    'description': 'Module to manage National ID information.',  # Optional: Add a short description
}
