package controlers;
import haxe.Template;
import haxe.Resource;
import haxe.ds.StringMap;
import php.Web;
import models.Contact;

class ContactCtrl {
	public function new(id : Int) {
		switch (Web.getMethod()) {
			case "GET":
				if (null == id) retrieveAll();
				else retrieveItem(id);
			case "POST":
				if (0 == id) create(Web.getParams());
				else {
					if (0 == Web.getPostData().length) delete(id);
					else update(id, Web.getParams());
				}
		}
	}

	function create(data : StringMap<String>) {
		var c : Contact = new Contact(data.get("firstname"), data.get("lastname"), data.get("email"), data.get("phone"));
		if (("" == c.firstname || null == c.firstname) || ("" == c.lastname || null == c.lastname)) {
			Web.setReturnCode(400); //bad request
			Sys.println("missing 'firsname' or 'lastname'");
		} else {
			c.insert();
			Web.redirect("?/contacts");
		}
	}
	
	function retrieveItem(id : Int) {
		var data : Contact;
		if (0 == id) data = new Contact("", "");
		else data = Contact.manager.get(id);
		if (null == data) Web.setReturnCode(404); //not found
		else {
			var tpl = new Template(Resource.getString("contact-edit"));
			Sys.println(tpl.execute(data));
		}
	}
	
	function retrieveAll() {
		var data : List<Contact> = Contact.manager.all();
		var tpl = new Template(Resource.getString("contacts-list"));
		Sys.println(tpl.execute({ Contact : data }));
	}
	
	function update(id : Int, data : StringMap<String>) {
		var c : Contact = Contact.manager.get(id);
		if (null == c) Web.setReturnCode(404); //not found
		else {
			c.firstname = data.get("firstname");
			c.lastname = data.get("lastname");
			c.email = data.get("email");
			c.phone = data.get("phone");
			c.update();
			Web.redirect("?/contacts");
		}
	}
	
	function delete(id : Int) {
		var c : Contact = Contact.manager.get(id);
		if (null == c) Web.setReturnCode(404); //not found
		else {
			c.delete();
			Web.redirect("?/contacts");
		}
	}
}
