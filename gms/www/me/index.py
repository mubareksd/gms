import frappe

def get_context():
    return {
        "member": frappe.db.sql("""
        SELECT `tabGym Member`.full_name FROM `tabUser` INNER JOIN `tabGym Member` ON `tabUser`.name = `tabGym Member`.user WHERE `tabUser`.name = %s
        """, frappe.session.user, as_dict=True),
        "classes": frappe.db.sql("""
        SELECT `tabGym Class`.name, `tabGym Class`.route, `tabGym Class`.class_name, `tabGym Class`.start_date, `tabGym Class`.end_date FROM `tabUser` INNER JOIN `tabGym Member` ON `tabUser`.name = `tabGym Member`.user INNER JOIN `tabGym Class Booking` ON `tabGym Member`.name = `tabGym Class Booking`.member INNER JOIN `tabGym Class` ON `tabGym Class Booking`.class = `tabGym Class`.name WHERE `tabUser`.name = %s
            """, frappe.session.user, as_dict=True),
        "trainers": frappe.db.sql("""
        SELECT `tabGym Trainer`.name, `tabGym Trainer`.route, `tabGym Trainer`.full_name FROM `tabUser` INNER JOIN `tabGym Member` ON `tabUser`.name = `tabGym Member`.user INNER JOIN `tabGym Trainer Subscription` ON `tabGym Trainer Subscription`.member = `tabGym Member`.name INNER JOIN `tabGym Trainer` ON `tabGym Trainer Subscription`.trainer = `tabGym Trainer`.name WHERE `tabUser`.name = %s
        """, frappe.session.user, as_dict=True),
        "measurements": frappe.db.sql("""
        SELECT `tabGym Member Measurement`.weight, `tabGym Member Measurement`.height, `tabGym Member Measurement`.body_mass_index, `tabGym Member Measurement`.body_fat_percentage, `tabGym Member Measurement`.muscle_mass, `tabGym Member Measurement`.date FROM `tabUser` INNER JOIN `tabGym Member` ON `tabUser`.name = `tabGym Member`.user INNER JOIN `tabGym Member Measurement` ON `tabGym Member`.name = `tabGym Member Measurement`.member WHERE `tabUser`.name = %s
        """, frappe.session.user, as_dict=True),
    }