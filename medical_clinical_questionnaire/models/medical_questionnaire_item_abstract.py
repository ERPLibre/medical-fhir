# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MedicalQuestionnaireItemAbstract(models.AbstractModel):
    _name = "medical.questionnaire.item.abstract"
    _description = "Questionnaire Response item"

    name = fields.Char(related="questionnaire_item_id.name")
    required = fields.Boolean(related="questionnaire_item_id.required")
    question_type = fields.Selection(
        related="questionnaire_item_id.question_type"
    )
    result = fields.Text()
    selection_options = fields.Char(
        related="questionnaire_item_id.selection_options"
    )
    options = fields.Char(related="questionnaire_item_id.options")
    questionnaire_item_id = fields.Many2one(
        "medical.questionnaire.item", readonly=False
    )
    technical_name = fields.Char(
        related="questionnaire_item_id.technical_name"
    )
    readonly = fields.Boolean(related="questionnaire_item_id.readonly")
    readonly_condition = fields.Char(
        related="questionnaire_item_id.readonly_condition"
    )
    is_invisible = fields.Boolean(related="questionnaire_item_id.is_invisible")
    invisible_condition = fields.Char(
        related="questionnaire_item_id.invisible_condition"
    )
    questionnaire_id = fields.Many2one(
        "medical.questionnaire",
        related="questionnaire_item_id.questionnaire_id",
    )

    procedure_request_id = fields.Many2one("medical.procedure.request")

    is_medical_observation = fields.Boolean(
        related="questionnaire_item_id.is_medical_observation"
    )
    medical_observation_code_id = fields.Many2one(
        "medical.observation.code",
        related="questionnaire_item_id.medical_observation_code_id",
    )

    def read(self, fields=None, load="_classic_read"):
        result = super().read(fields=fields, load=load)
        if not self.env.context.get("widget_medical_questionnaire"):
            return result
        for r in result:
            if "result" in r:
                record = self.browse(r["id"])
                r["result"] = record._transform_result(record.result)
        return result

    def _transform_result(self, result):
        if self.question_type == "integer":
            return int(result)
        if self.question_type == "float":
            return float(result)
        if self.question_type == "boolean":
            return bool(result)
        if self.question_type == "date":
            return fields.Datetime.from_string(result)
        return result

    def write(self, vals):
        for rec in self:
            vals.pop("result_%s" % rec.id, False)
        return super().write(vals)