# Copyright (c) 2024, Haron Computer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMember(Document):
    def validate(self):
        self.set_full_name()
        if not self.email:
            self.email = self.first_name + "" + "@gym.com"

    def before_save(self):
        if not self.user:
            self.user = self.create_user()

    def set_full_name(self):
        self.full_name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

    def create_user(self):
        if not frappe.db.exists("User", self.email):
            user = frappe.get_doc(
                dict(
                    doctype="User",
                    email=self.email,
                    mobile_no=self.phone,
                    first_name=self.first_name,
                    middle_name=self.middle_name,
                    last_name=self.last_name,
                    gender=self.gender,
                    new_password='mj65tuf5udhfdskjfh',
                    roles=[{"role": "Gym Member"}],
                )
            )
            user.flags.ignore_permissions = True
            user.insert()
            return user.name
        else:
            frappe.throw("User already exists")
            return None
