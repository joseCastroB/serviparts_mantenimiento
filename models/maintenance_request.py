from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    # Campos de Horómetro
    work_hours_start = fields.Float(string="Horas Trabajo Inicio", help="Lectura del horómetro al iniciar")
    work_hours_end = fields.Float(string="Horas Trabajo Fin", help="Lectura del horómetro al finalizar")

    # Campos de Fechas Específicas de ejecución
    execution_start_date = fields.Datetime(string="Fecha Inicio Real")
    execution_end_date = fields.Datetime(string="Fecha Fin Real")

    # Campo para la firma digital
    customer_signature = fields.Binary(string="Firma del Cliente", attachment=True)

    def action_clean_signature(self):
        "Limpia la firma del cliente y recarga la vista"
        for record in self: 
            record.customer_signature = False
        return{
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


    # Campo para múltiples fotos (Evidencias)
    evidence_ids = fields.Many2many(
        'ir.attachment',
        string="Fotos de Evidencia",
        help="Fotos tomadas desde la app móvil"
    )