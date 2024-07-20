from odoo import api, fields, models


class Hostel(models.Model):
    _name = "hostel.hostel"
    _description = "Information about hostel"
    _order = "id desc, name"
    _rec_name = "display_name"

    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    zip = fields.Char(string="Zip", change_default=True)
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string="State")
    country_id = fields.Many2one("res.country", string="Country")
    phone = fields.Char(string="Phone", required=True)
    mobile = fields.Char(string="Mobile", required=True)
    email = fields.Char(string="Email")
    display_name = fields.Char(
        string="Display Name", compute="_compute_display_name", store=True
    )

    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary("Hostel Image")
    active = fields.Boolean(
        "Active", default=True, help="Activate/Deactivate hostel record"
    )
    type = fields.Selection(
        [("male", "Boys"), ("female", "Girls"), ("common", "Common")],
        "Type",
        help="Type of Hostel",
        required=True,
        default="common",
    )
    other_info = fields.Text("Other Information", help="Enter more information")
    description = fields.Html("Description")
    hostel_rating = fields.Float("Hostel Average Rating", digits="Rating Value")
    category_id = fields.Many2one("hostel.category")
    ref_doc_id = fields.Reference(
        selection="_referencable_models", string="Reference Document"
    )

    @api.model
    def _referencable_models(self):
        models = self.env["ir.model"].search([("field_id.name", "=", "message_ids")])
        return [(x.model, x.name) for x in models]

    @api.depends("name", "hostel_code")
    def _compute_display_name(self):
        """Compute display_name by combining name and hostel_code."""
        for record in self:
            name = record.name or ""
            if record.hostel_code:
                name = f"{name} ({record.hostel_code})"
            record.display_name = name
