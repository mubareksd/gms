frappe.ready(function() {
	var member = {{ frappe.form_dict.member | json }}

    frappe.web_form.set_value('member', member);

    frappe.web_form.on('member', (field, value) => {
	    frappe.web_form.set_df_property('member', 'hidden', 1);
    })

    frappe.web_form.on('class', (field, value) => {
	    frappe.web_form.set_df_property('class', 'hidden', 1);
    })

    frappe.web_form.on('booking_date', (field, value) => {
	    frappe.web_form.set_df_property('booking_date', 'hidden', 1);
    })
})