from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'tabel Training Course'

    name = fields.Char(string='Nama Kursus',required=True)
    keterangan = fields.Text(string='Keterangan')
    user_id = fields.Many2one(comodel_name='res.users',string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')
    
    _sql_constrains = [
        ('name_course_unique', 'UNIQUE(name)', 'Nama kursus sudah ada')
    ]

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'

    name = fields.Char(string='Sesi Training',required=True)
    course_id = fields.Many2one(comodel_name="training.course", string='ID Kursus', required=True)
    start_date = fields.Date(string='Tanggal Mulai', required=True)
    duration = fields.Float(string='Durasi', required=True)
    seets = fields.Integer(string='Jumlah Peserta', required=True,default=1)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur')
    
    
    
    


    
    
