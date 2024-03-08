# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LeadAgataBusinessLine(models.Model):
    _name = 'crm.lead.business.line'
    _description = 'campo parametrizable linea de negocio para los lead'

    name = fields.Char(
        string='Linea de Negocio',
        size=255,
        help='''Liena de negocio agata para los lead''',
    )

class LeadAgatatypeSolution(models.Model):
    _name = 'crm.lead.type.solution'
    _description = 'campo parametrizable tipo de solucion  para los lead'

    name = fields.Char(
        string='Tipo de Solución',
        size=255,
        help='''Tipo de solucion agata para los lead''',
    )

class LeadAgataAlly(models.Model):
    _name = 'crm.lead.ally'
    _description = 'campo parametrizable aliado para los lead'

    name = fields.Char(
        string='Aliado',
        size=255,
        help='''aliado agata para los lead''',
    )

class LeadAgataStrategy(models.Model):
    _name = 'crm.lead.strategy'
    _description = 'campo parametrizable estrategia para los lead'

    name = fields.Char(
        string='Estrategia',
        size=255,
        help='''Estrategia agata para los lead''',
    )

class LeadAgataBudget(models.Model):
    _name = 'crm.lead.budget'
    _description = 'campo parametrizable presupuesto para los lead'

    name = fields.Char(
        string='Presupuesto',
        size=255,
        help='''Presupesto agata para los lead''',
    )