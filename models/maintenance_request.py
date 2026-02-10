from odoo import models, fields, api

class MaintenanceChecklistLine(models.Model):
    _name = 'maintenance.checklist.line'
    _description = 'Línea de Checklist'

    request_id = fields.Many2one('maintenance.request', string="Solicitud")
    is_done = fields.Boolean(string="Hecho")
    name = fields.Char(string="Descripción", required=True)

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    name = fields.Char(string="Solicitud", default="Nuevo", readonly=True)

    request_title = fields.Char(string="Título de la Solicitud")

    partner_id = fields.Many2one('res.partner', string="Cliente")

    technician_id = fields.Many2many(
        'res.users',
        string="Técnicos Asignados"
    )

    hour_type = fields.Selection([
        ('operational', 'Operativo'),
        ('snack', 'Refrigerio'),
        ('transfer', 'Traslado')    
    ], string="Tipo de Hora")

    equipment_found_status = fields.Selection([
        ('operative', 'Operativo'),
        ('inoperative', 'Inoperativo')
    ], string="¿Cómo encontró el equipo?")

    # Service_description no va en el front
    service_description = fields.Html(string="Descripción del Servicio")

    checklist_ids = fields.One2many(
        'maintenance.checklist.line', 
        'request_id', 
        string="Descripción del Servicio"
    )

    equipment_final_status = fields.Selection([
        ('operative', 'Operativo'),
        ('inoperative', 'Inoperativo')
    ], string="¿Cómo se deja el equipo?")       

    has_pending = fields.Selection([
        ('yes', 'Sí'),
        ('no', 'No')
    ], string="¿Encontró pendientes?")

    pending_comments = fields.Html(string="Pendientes / Comentarios")

    service_rating = fields.Selection([
        ('good', 'Bueno'),
        ('regular', 'Regular'),
        ('bad', 'Malo')
    ], string="¿Cómo califica el servicio brindado?")

    # Campos de Horómetro (no se utiliza)  
    work_hours_start = fields.Float(string="Horas Trabajo Inicio", help="Lectura del horómetro al iniciar")
    work_hours_end = fields.Float(string="Horas Trabajo Fin", help="Lectura del horómetro al finalizar")

    # Campos de Fechas Específicas de ejecución
    execution_start_date = fields.Datetime(string="Fecha Inicio Real")
    execution_end_date = fields.Datetime(string="Fecha Fin Real")

    # CAMPOS DE FIRMA / RESPONSABLES
    signed_by_customer = fields.Char(string="Contacto Cliente/Técnico")
    signed_by_technician = fields.Char(string="Técnico (Nombre)")

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

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('maintenance.request.jh') or 'Nuevo'

        result = super(MaintenanceRequest, self).create(vals)
        return result