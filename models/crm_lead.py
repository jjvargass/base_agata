# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lead(models.Model):
    _name = "crm.lead"
    _inherit = "crm.lead"

    linea_negocio_id = fields.Many2one(
        string='Linea de Negocio',
        comodel_name='crm.lead.business.line',
        help='''Linea de Negocio Agata''',
    )
    tipo_solucion_id = fields.Many2one(
        string='Tipo de Solucion',
        comodel_name='crm.lead.type.solution',
        help='''Tipo de Solucion Agata''',
    )
    aliado_id = fields.Many2one(
        string='Aliado',
        comodel_name='crm.lead.ally',
        help='''Aliado Agata''',
    )
    estrategia_id = fields.Many2one(
        string='Estrategia',
        comodel_name='crm.lead.strategy',
        help='''Estrategia Agata''',
    )
    presupuesto_id = fields.Many2one(
        string='Presupuesto',
        comodel_name='crm.lead.budget',
        help='''Presupuesto Agata''',
    )