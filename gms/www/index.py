import frappe

def get_context():
    return {
        "name": frappe.db.get_value("Gym Setting", None, "gym_name"),
        "image": frappe.db.get_value("Gym Setting", None, "image")
    }