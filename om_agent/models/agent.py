from odoo import fields, models, api


class OmAgent(models.Model):
    _name = "om.agent"
    _description = "Om Agent"

    agent_nid_img = fields.Image(string="Image")
    agent_name = fields.Char(string="Agent name")
    agent_location = fields.Char(string="Agent Location")
    agent_dcs = fields.Text(string='Description')
