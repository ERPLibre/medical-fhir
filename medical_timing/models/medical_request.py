# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MedicalRequest(models.AbstractModel):

    _inherit = "medical.request"

    next_expected_date = fields.Datetime(readonly=True)
    timing_id = fields.Many2one(
        "medical.timing", readonly=True, track_visibility="onchange"
    )
    timing_start_date = fields.Datetime(
        readonly=True, track_visibility="onchange"
    )
    location_id = fields.Many2one(
        "res.partner",
        track_visibility="onchange",
        domain=[("is_location", "=", True)],
    )

    can_generate_next = fields.Boolean(default=True)

    def generate_new_event(self):
        self.ensure_one()
        if self.state == "draft":
            self.draft2active()
        request = self.generate_event()
        if self.timing_id:
            self.next_expected_date = self._next_date()
        else:
            self.active2completed()
        return request

    def _next_date(self):
        return self.timing_id._next_date(
            self.next_expected_date, self.location_id
        )

    def action_change_timing(self):
        self.ensure_one()
        result = self.env.ref(
            "medical_timing.medical_request_set_timing_act_window"
        ).read()[0]
        result["context"] = {
            "default_res_model": self._name,
            "default_res_id": self.id,
            "default_timing_id": self.timing_id.id,
            "default_location_id": self.location_id.id,
        }
        return result