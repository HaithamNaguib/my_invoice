# -*- coding: utf-8 -*-

import pytz
from lxml import etree
from odoo import models, fields, api, _

class SkillsEntry(models.Model):
    _name = 'skills.entry'
    _description = 'Skills'
    _rec_name = 'skill'

    skill = fields.Char(string='Skill', required=True,  track_visibility="always")
    place = fields.Char(string='Place', required=True,  track_visibility="always")

    # person_id = fields.Many2one('person.entry', string='Person')