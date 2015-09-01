package models;
import sys.db.Object;
import sys.db.Types;
using StringTools;

@:id(id)
class Contact extends Object {
    public var id(default, null) : SId;
    public var firstname(default, set) : String;
    public var lastname(default, set) : String;
    public var email(default, set) : String;
    public var phone(default, set) : String;
    
    public function new(firstname : String, lastname : String, ?email : String = "", ?phone : String = "") {
		super();
		this.firstname = firstname;
		this.lastname = lastname;
		this.email = email;
		this.phone = phone;
	}
	
	function set_firstname(firstname : String) : String {
		if (null == id || ("" != firstname && null != firstname)) this.firstname = firstname.htmlEscape();
		return this.firstname;
	}
	
	function set_lastname(lastname : String) : String {
		if (null == id || ("" != lastname && null != lastname)) this.lastname = lastname.htmlEscape();
		return this.lastname;
	}
	
	function set_email(email : String) : String {
		if (null != email) {
			var regexp = ~/^[a-z0-9._%-]+@[a-z0-9.-]+\.[a-z][a-z]+$/i;
			if ("" == email || regexp.match(email)) this.email = email;
		}
		return this.email;
	}
	
	function set_phone(phone : String) : String {
		if (null != phone) {
			var regexp = new EReg("^[0-9 ]*$", "");
			if ("" == phone || regexp.match(phone)) this.phone = phone;
		}
		return this.phone;
	}
}
