from __future__ import print_function
from flask import render_template, send_file, jsonify, request
from app import app

from mailmerge import MailMerge
from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

template = 'app/docx-templates/nego SVP above 50k_template.docx'

document = MailMerge(template)

@app.route('/', methods=['POST'])
@app.route('/index')
def index():
	data = request.get_json()

	document = export(input=data)

	f = document.write('app/outputs/export.docx')

	return send_file('outputs/export.docx', as_attachment=True, attachment_filename='export.docx')

def export(input):
	"""
	Get input and turn it into a document
	"""

	input['pras_no'] = input['details']['pras_no']
	input['end_user'] = input['details']['end_user']
	input['abc'] = input['details']['abc']
	input['procurement_mode'] = input['details']['procurement_mode']
	input['grand_total'] = input['details']['grand_total']
	input['delivery_installation_period'] = input['details']['delivery_installation_period']
	input['deadline_time'] = datetime.strptime(input['deadline_time'], '%H:%M').strftime('%I:%M %p')

	document.merge(**input)
	document.merge_rows('quantity', input['details']['items'])

	return document