# Copyright (c) 2024, Haron Computer and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class GymClass(WebsiteGenerator):
	pass

@frappe.whitelist()
def fetch_rooms(branch):
    rooms = frappe.get_all('Gym Room', filters={'branch': branch}, fields=['name'])
    return [room.get('name') for room in rooms]
