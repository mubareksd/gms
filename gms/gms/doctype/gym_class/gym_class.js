// Copyright (c) 2024, Haron Computer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Class", {
	refresh(frm) {
        frm.trigger("add_publish_button");
	},
    branch: function(frm) {
        frappe.call({
            method: 'gms.gms.doctype.gym_class.gym_class.fetch_rooms',
            args: {
                branch: frm.doc.branch
            },
            callback: function(response) {
                var rooms = response.message;
                frm.set_query('room', function() {
                    return {
                        filters: {
                            'name': ['in', rooms]
                        }
                    };
                });
            }
        });
    },
    add_publish_button(frm) {
		frm.add_custom_button(frm.doc.published ? __("Unpublish") : __("Publish"), () => {
			frm.set_value("published", !frm.doc.published);
			frm.save();
		});
	},
});