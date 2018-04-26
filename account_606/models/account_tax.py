# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    itbis_facturado = fields.Boolean('ITBIS Facturado')
    itbis_retenido = fields.Boolean('ITBIS Retenido')
    itbis_sujeto_troporcionalidad = fields.Boolean('ITBIS Sujeto a Proporcionalidad')
    itbis_llevado = fields.Boolean('ITBIS llevado al Costo')
    monto_retencion_renta = fields.Boolean('Monto Retención Renta')
    impuesto_selectivo_al_consumo = fields.Boolean('Impuesto Selectivo al Consumo')
    otros_impuestos = fields.Boolean('Otros Impuestos / Tasas')
    monto_propina_legal = fields.Boolean('Monto Propina Legal')
    tipo_retencion = fields.Selection([
            ('01','ALQUILERES'),
            ('02','HONORARIOS POR SERVICIO'),
            ('03','OTRAS RENTAS'),
            ('04','OTRAS RENTAS (RENTAS PRESUNTAS)'),
            ('05','INTERESES PAGADOS A PERSONAS JURÍDICAS RESIDENTES'),
            ('06','INTERESES PAGADOS A PERSONAS FÍSICAS RESIDENTES'),
            ('07','RETENCIÓN POR PROVEEDORES DEL ESTADO'),
            ('08','JUGOS TELEFÓNICOS'),
        ], string='Tipo de Retención en ISR')
