from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    # ---------------------------------------------------------------
    # ELIMINAR ESTE ARCHIVO ANTES DE SUBIR A PRODUCCIÓN
    # ES SOLO UN PARCHE PARA ENTORNO LOCAL
    repair_count = fields.Integer(string='Reparaciones', default=0)    

    brand = fields.Char(string='Marca')

    # ---------------------------------------------------------------

    location_chars = fields.Char(string='Ubicación')
    horometer_reading = fields.Float(string='Horómetro')
    execution_date = fields.Date(string='F. Ejecución')

    alias = fields.Char(string='Alias')