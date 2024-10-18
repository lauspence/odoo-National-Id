from odoo import models, fields, api
from datetime import datetime

class NationalID(models.Model):
    _name = 'national.id'
    _description = 'National ID'

    # Define your fields here
    name = fields.Char(string='Name')
    user_id = fields.Many2one('res.users', string='User ')
    full_name = fields.Char(string='Full Name')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    nationality = fields.Char(string='Nationality')
    picture = fields.Binary(string='Picture')
    lc_reference_letter = fields.Binary(string='Reference Letter')
    application_date = fields.Datetime(string='Application Date', readonly=True, default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='State', readonly=True, default='draft')

    @api.model
    def action_submit(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'under_review'  # Change state to under_review
                record.message_post(body="Application submitted for review.")

    @api.model
    def action_approve(self):
        for record in self:
            if record.state == 'under_review':
                record.state = 'approved'  # Change state to approved
                record.message_post(body="Application approved.")

    @api.model
    def action_reject(self):
        for record in self:
            if record.state == 'under_review':
                record.state = 'rejected'  # Change state to rejected
                record.message_post(body="Application rejected.")