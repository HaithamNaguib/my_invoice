# # -*- coding: utf-8 -*-
#
# from odoo import models, fields , api , _
# from odoo.exceptions import ValidationError
#
# # ## inherit of Settings
# # class InvoiceSettings(models.TransientModel):
# #     _inherit = 'res.config.settings'
# #     note = fields.Integer(default=0)
# #     # responsible_id = fields.Many2one('res.users',
# #     #                                  ondelete='set null', string="Responsible", index=True)
# #     def set_values(self):
# #         super(InvoiceSettings, self).set_values()
# #         self.env['ir.config_parameter'].set_param('my_invoice.note', self.note)
# #
# #     def get_values(self):
# #         res = super(InvoiceSettings, self).get_values()
# #         note = self.env['ir.config_parameter'].get_param('my_invoice.note')
# #         res.update({
# #             'note': note,
# #         })
# #         return res
#
# ## Inherit of invoicing
# class AccountMoveInherit(models.Model):
#     _inherit = 'account.move.line'
#
#     # partner_id = fields.Many2one('res.partner', string='desc', required=True)
#     # description1 = fields.Char(string='description1')
#     # description2 = fields.Char(string='description2')
#     # description3 = fields.Char(string='description3')
#     # descmobile = fields.Char(string='descmobile', related='partner_id.mobile')
#     # descemail = fields.Char(string='descemail', related='partner_id.email')
#     invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice lines')
#     # lines = fields.many2one('account.move', 'invoice_line_ids' , string='Invoice lines')
#     @api.constrains('invoice_line_ids')
#     def _check_invoice_line_ids(self):
#         for r in self:
#             if len(r.invoice_line_ids) > 3:
#                 raise ValidationError("A session's instructor can't be an attendee")
#
#     # def lines_count(self):
#     #     for r in self:
#     #         r.lines_count = len(r.invoice_line_ids)
#     #         if r.lines_count > 3:
#     #             return {
#     #                 'warning': {
#     #                     'title': "Too many attendees",
#     #                     'message': "Increase seats or remove excess attendees",
#     #                 },
#     #             }
#         #
#         # @api.onchange('seats', 'attendee_ids')
#     # def _verify_valid_seats(self):
#     #     if self.seats < 0:
#     #         return {
#     #             'warning': {
#     #                 'title': "Incorrect 'seats' value",
#     #                 'message': "The number of available seats may not be negative",
#     #             },
#     #         }
#     #     if self.seats < len(self.attendee_ids):
#     #         return {
#     #             'warning': {
#     #                 'title': "Too many attendees",
#     #                 'message': "Increase seats or remove excess attendees",
#     #             },
#     #         }
#     #
#     # @api.constrains('instructor_id', 'attendee_ids')
#     # def _check_instructor_not_in_attendees(self):
#     #     for r in self:
#     #         if r.instructor_id and r.instructor_id in r.attendee_ids:
#     #             raise exceptions.ValidationError("A session's instructor can't be an attendee")
#
#
#     # @api.depends('seats', 'attendee_ids')
#     # def _taken_seats(self):
#     #     for r in self:
#     #         if not r.seats:
#     #             r.taken_seats = 0.0
#     #         else:
#     #             r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
#
#     # line_ids = fields.One2many('account.move.line', 'move_id', string='Journal Items', copy=True, readonly=True,
#     #     states={'draft': [('readonly', False)]})
#     #
#     # invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice lines',
#     #     copy=False, readonly=True,
#     #     domain=[('exclude_from_invoice_tab', '=', False)],
#     #     states={'draft': [('readonly', False)]})