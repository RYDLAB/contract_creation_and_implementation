# -*- coding: utf-8 -*-
{
    "name": "Contract creation and implementation",
    "summary": """
        Introduces Contract entity.""",
    "description": """
        Framework Contracts between company and customers, company and vendors. Contracts have annexes for
        sale/purchase orders.
    """,
    "author": "RYDLAB",
    "website": "https://rydlab.ru",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sale/Purchase",
    "version": "16.0.0.5",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["base", "base_setup", "contacts", "portal"],
    # always loaded
    "data": [
        "security/contract_security.xml",
        "security/ir.model.access.csv",
        "wizard/contract_content_wizard_view.xml",
        "wizard/contract_publish_wizard_view.xml",
        "wizard/confirm_delete_wizard.xml",
        "wizard/contract_version_sign_wizard_view.xml",
        "wizard/contract_line_wizard_view.xml",
        "wizard/contract_version_creation_wizard_view.xml",
        "wizard/contract_section_wizard_view.xml",
        "views/contract_annex.xml",
        "views/contract_section_view.xml",
        "views/contract_line_view.xml",
        "views/contract_content_view.xml",
        "views/contract_version_view.xml",
        "views/contract.xml",
        "views/partner.xml",
        "views/res_config_settings.xml",
        "data/mail_template_data.xml",
        "data/schedule_activities_data.xml",
    ],
    "installable": True,
    "application": True,
    "images": ["static/description/banner.png"],
}
