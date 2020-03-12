""" Encode any known changes to the database here
to help the matching process
"""

renamed_modules = {
    # Odoo
    'base_vat_autocomplete': 'partner_autocomplete',
    'mrp_repair': 'repair',
    'product_extended': 'mrp_bom_cost',
    # OCA/account-payment
    'account_payment_return_import_sepa_pain': (
        'account_payment_return_import_iso20022'
    ),
    # OCA/community-data-files
    'product_uom_unece': 'uom_unece',
    # OCA/crm > OCA/partner-contact
    'crm_deduplicate_acl': 'partner_deduplicate_acl',
    'crm_deduplicate_by_ref': 'partner_deduplicate_by_ref',
    'crm_deduplicate_by_website': 'partner_deduplicate_by_website',
    'crm_deduplicate_filter': 'partner_deduplicate_filter',
    # OCA/hr
    'hr_employee_seniority': 'hr_employee_service_contract',
    'hr_family': 'hr_employee_relative',
    # OCA/sale-workflow
    'sale_procurement_group_by_requested_date':
        'sale_procurement_group_by_commitment_date',
    # OCA/server-brand
    'res_config_settings_enterprise_remove': 'remove_odoo_enterprise',
    # OCA/stock-logistics-workflow
    'stock_batch_picking': 'stock_picking_batch_extended',
    'stock_pack_operation_auto_fill': 'stock_move_line_auto_fill',
}

merged_modules = {
    # Odoo
    'auth_crypt': 'base',
    'account_cash_basis_base_account': 'account',
    'account_invoicing': 'account',
    'rating_project': 'project',
    'sale_order_dates': 'sale',
    'sale_payment': 'sale',
    'sale_service_rating': 'sale_timesheet',
    'snippet_latest_posts': 'website_blog',
    'web_planner': 'web',
    'website_quote': 'sale_quotation_builder',
    'website_rating_project': 'project',
    'website_sale_options': 'website_sale',
    'website_sale_stock_options': 'website_sale_stock',
    'test_pylint': 'test_lint',
    # OCA/account-analytic
    # although model is defined in "analytic", logic is in "account"
    'account_analytic_distribution': 'account',
    'account_asset_analytic': 'account_asset_management',
    # OCA/account-financial-reporting
    'customer_activity_statement': 'partner_statement',
    'customer_outstanding_statement': 'partner_statement',
    # OCA/account-financial-tools
    'account_asset': 'account_asset_management',
    'account_asset_depr_line_cancel': 'account_asset_management',
    'account_asset_disposal': 'account_asset_management',
    'account_reversal': 'account',
    # OCA/e-commerce
    'website_sale_default_country': 'website_sale',
    # OCA/event
    'event_registration_mass_mailing': 'mass_mailing_event',
    # OCA/hr
    'hr_expense_analytic_tag': 'hr_expense',
    # OCA/manufacture-reporting
    'mrp_bom_structure_html': 'mrp',
    'mrp_bom_structure_report': 'mrp',
    # OCA/partner-contact
    'base_country_state_translatable': 'l10n_multilang',
    'base_partner_merge': 'base',
    # OCA/purchase-workflow
    'product_supplierinfo_discount': 'purchase_discount',
    # OCA/pos
    'pos_config_show_accounting': 'point_of_sale',
    # OCA/server-auth
    'auth_brute_force': 'base',
    # OCA/stock-logistics-warehouse
    'stock_putaway_product': 'stock',
    # OCA/web
    'web_sheet_full_width': 'web_responsive',
    # OCA/website
    'website_form_metadata': 'website_form',

    'hash_search': 'document_quick_access',
    'hash_search_account_invoice': 'document_quick_access_document_qr',
    'hash_search_document_scanner': 'document_quick_access_folder_auto_classification',
    'hash_search_document_scanner_queue_ssh': 'document_quick_access_folder_auto_classification',
    'hash_search_purchase': 'document_quick_access',
    # TODO: Arreglar
    # 'hash_search_remote_printer': 'document_quick_access_remote_printer',
    'hash_search_remote_printer': 'document_quick_access',
    'hr_employee_seniority': 'hr_employee_service_contract',
    'hr_family': 'hr_employee_relative',
    # TODO: Mod 190
    'l10n_es_aeat_mod190': 'l10n_es_aeat',
    'mail_activity_creator': 'mail',
    'speeder_account': 'account',
    'bus_connector_base_location': 'bus_connector_base', # TODO: FIX
    'stock_pack_operation_auto_fill': 'stock_move_line_auto_fill',
    'attachment_preview': 'web_responsive',
    'res_config_settings_enterprise_remove': 'remove_odoo_enterprise',
    'web_qr': 'report_qr',
}

# only used here for openupgrade_records analysis:
renamed_models = {
    # Odoo
    'hr.holidays': 'hr.leave',
    'hr.holidays.status': 'hr.leave.type',
    'mrp.repair': 'repair.order',
    'mrp.repair.cancel': 'repair.cancel',
    'mrp.repair.fee': 'repair.fee',
    'mrp.repair.line': 'repair.line',
    'mrp.repair.make_invoice': 'repair.order.make_invoice',
    'procurement.rule': 'stock.rule',
    'product.attribute.line': 'product.template.attribute.line',
    'product.attribute.price': 'product.template.attribute.value',
    'product.uom': 'uom.uom',
    'product.uom.categ': 'uom.category',
    'sale.quote.line': 'sale.order.template.line',
    'sale.quote.option': 'sale.order.template.option',
    'sale.quote.template': 'sale.order.template',
    'stock.incoterms': 'account.incoterms',
    # OCA/account-financial-tools
    'account.asset.asset': 'account.asset',
    'account.asset.depreciation.line': 'account.asset.line',
    'account.asset.category': 'account.asset.profile',
}

# only used here for openupgrade_records analysis:
merged_models = {
    # Odoo
    'stock.location.path': 'stock.rule',
}
