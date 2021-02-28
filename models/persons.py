# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# How to Create New Models : https://www.youtube.com/watch?v=L6MxDR71_1k&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=2
class PersonEntry(models.Model):
    _name = 'person.entry'
    _description = 'Person Entry'
    _rec_name = 'person_name'

    name = fields.Char(string="Contact Number")
    # name_seq = fields.Char(string='Person ID', required=True, copy=False, readonly=True,
    #                        index=True, default=lambda self: _('New'))
    person_name = fields.Char(string='Name', required=True,  track_visibility="always")
    job_id = fields.Many2one('classes.entry', string='Job')
    skill = fields.Many2many('skills.entry', string='Skills')
    person_age = fields.Integer('Age', track_visibility="always", group_operator=False)
    person_email = fields.Char(string="Email")
    person_image = fields.Binary(string="Image", attachment=True)
    person_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'others')], string="Gender")
    blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve')],
                                   string="Blood Group")

    # children = fields.Many2many('person.entry', '' string='Children')
