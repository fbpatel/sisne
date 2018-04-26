# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def check_do_vat(self):
        for partner in self:
            # For Dominican Republic only
            if partner.country_id.code == 'DO':
                # For Individual
                if partner.vat and (not partner.is_company):
                    if partner.vat[:2] != 'DO' or len(partner.vat) != 13 or (not partner.vat[2:].isdigit()):
                        raise ValidationError(_('The VAT number [%s] for partner [%s] does not seem to be valid. \nNote: the expected format is DO12345678901') % (partner.vat, partner.name))

                # For Company
                if partner.vat and partner.is_company:
                    if len(partner.vat) != 11 or partner.vat[:2] != 'DO' or (not partner.vat[2:].isdigit()):
                        raise ValidationError(_('The VAT number [%s] for company [%s] does not seem to be valid. \nNote: the expected format is DO123456789') % (partner.vat, partner.name))
