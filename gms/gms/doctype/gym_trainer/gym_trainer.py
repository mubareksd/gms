# Copyright (c) 2024, Haron Computer and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class GymTrainer(WebsiteGenerator):
	def validate(self):
		self.set_full_name()
	def set_full_name(self):
		self.full_name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
