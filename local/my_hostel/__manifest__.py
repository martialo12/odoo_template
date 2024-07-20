{
    "name": "Hostel Management",
    "summary": "Manage Hostel easily",
    "description": """
                    Manage Hostel
                    ==============
                    Efficiently manage the entire residential facility in the school
    """,
    "author": "Martial Wafo",
    "website": "https://martialo12.github.io/",
    "category": "Tools",
    "version": "17.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_amenities.xml",
        "views/hostel_student.xml",
        "views/hostel_categ.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "web/static/src/xml/**/*"
        ]
    },
    "license": "LGPL-3",
    "installable": True,
}
