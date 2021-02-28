# -*- coding: utf-8 -*-

import pytz
from lxml import etree
from odoo import models, fields, api, _

class ClassesEntry(models.Model):
    _name = 'classes.entry'
    _description = 'Classes'
    _rec_name = 'job'

    person_id = fields.Many2one('person.entry', string='Person')

    job = fields.Char(string='Job', required=True,  track_visibility="always")

    children = fields.Many2many('person.entry', string='Children')

    # class_age = fields.Integer('Age', related='patient_id.patient_age')
