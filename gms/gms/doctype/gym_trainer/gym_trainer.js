// Copyright (c) 2024, Haron Computer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer", {
	refresh(frm) {
        frm.trigger("add_publish_button");
	},
    add_publish_button(frm) {
		frm.add_custom_button(frm.doc.published ? __("Unpublish") : __("Publish"), () => {
			frm.set_value("published", !frm.doc.published);
			frm.save();
		});
	},
});
