import frappe

def get_context(context):
	if frappe.db.exists("Gym Member", {"email": frappe.session.user}):
		member = frappe.get_doc("Gym Member", {"email": frappe.session.user})
		frappe.form_dict.new = 0
		frappe.form_dict.name = member.name
	# else:
	# 	frappe.local.flags.redirect_location = "/"
	# 	raise frappe.Redirect
