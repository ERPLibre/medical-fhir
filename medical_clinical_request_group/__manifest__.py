# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Clinical Request Group",
    "summary": "Medical request group",
    "version": "12.0.1.0.0",
    "author": "Creu Blanca, Eficent, Odoo Community Association (OCA)",
    "category": "Medical",
    "website": "https://github.com/OCA/vertical-medical",
    "license": "LGPL-3",
    "depends": ["medical_clinical", "medical_workflow"],
    "data": [
        "data/ir_sequence_data.xml",
        "data/medical_workflow.xml",
        "security/medical_security.xml",
        "security/ir.model.access.csv",
        "views/medical_request_view.xml",
        "views/medical_request_group_view.xml",
    ],
    "demo": ["demo/medical_demo.xml"],
    "application": False,
    "installable": True,
    "auto_install": False,
}
