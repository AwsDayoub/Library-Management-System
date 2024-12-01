{
    'name': 'Library Management System',
    'version': '1.0',
    'summary': 'Manage library books, authors, and categories',
    'description': 'A module for managing a library system including books, authors, and categories.',
    'author': 'Aws Dayoub',
    'category': 'Library',
<<<<<<< HEAD
    'depends': ['base', 'mail', 'sale'],
=======
    'depends': ['base', 'mail'],
>>>>>>> d7ee5d7d75a7e9cc232429838aaef6d127c0b4d1
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/books_views.xml',
        'views/books_authors_views.xml',
        'views/books_categories_views.xml',
        #'views/sale_order_views.xml',
<<<<<<< HEAD
        'wizards/add_book_wizard_views.xml',
        'views/menu_items.xml',  
=======
        'views/menu_items.xml',
        'wizards/add_book_wizard_views.xml',
>>>>>>> d7ee5d7d75a7e9cc232429838aaef6d127c0b4d1
    ],
    'installable': True,
    'application': True,
}
