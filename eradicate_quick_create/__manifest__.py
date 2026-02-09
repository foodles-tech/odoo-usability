# Copyright 2014-2021 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>

{
    "name": "Eradicate Quick Create",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "license": "AGPL-3",
    "summary": "Disable quick create on all objects",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-financial-tools",
    "depends": ["web_m2x_options"],
    "post_init_hook": "web_m2x_options_create",
    "installable": True,
}
