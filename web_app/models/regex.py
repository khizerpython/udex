from django.core.validators import RegexValidator
from web_app import constants 

# Department Regex Validators
name = RegexValidator(constants.NAME_REGEX , message = "Department name must be alphabetic")
description = RegexValidator(constants.DESCRIPTION_REGEX, message = "Invalid Description")



#Designation name Regex
designation_name = RegexValidator(constants.DESIGNATION_NAME_REGEX , message = "Only A-Z, 0-9, - and spaces between words are allowed")



# ROLE NAME REGEX
role_name = RegexValidator(constants.ROLE_NAME_REGEX , message = "Invalid Format, only A-Z, a-z are allowed and special character & is allowed")

# Auth User Regex Validators
employee_id_regex = RegexValidator(constants.EMPLOYEE_ID_REGEX , message = "Employee id must be a number .length will be 5")
first_name_regex = RegexValidator(constants.NAME_REGEX,message="First name must be Alphabetic")
last_name_regex = RegexValidator(constants.NAME_REGEX,message="Last name must be Alphabetic")
username_regex = RegexValidator(constants.USERNAME_REGEX,message="invalid username, can only contain characters in between 3-25 range. String range 3-25")
contact_number_regex = RegexValidator(constants.CONTACT_NUMBER_REGEX,message="Please enter valid contact number")
url_name_regex = RegexValidator(constants.URL_NAME_REGEX,message="Please enter valid URL name")
workflow_abbreviation_regex = RegexValidator(constants.WORKFLOW_ABBREVIATION_REGEX,message="Invalid workflow case string")


# Change Mnagement form regex
process_to_be_change_regex = RegexValidator(constants.WHOLE_FORM_REGEX,message="Please enter valid input")
propose_change_regex = RegexValidator(constants.WHOLE_FORM_REGEX,message="Please enter valid input")
justification_regex = RegexValidator(constants.WHOLE_FORM_REGEX,message="Please enter valid input")
comment_regex = RegexValidator(constants.WHOLE_FORM_REGEX,message="Please enter valid input")

# Asset Movement regex
specify_other_location = RegexValidator(constants.SPECIFY_LOCATION_REGEX,message="Only A-z, a-z, 0-9 and (!#-_) special charactersand one space in between characters are allowed")


system_name_regex = RegexValidator(constants.SYSTEM_NAME_REGEX,message="Format of system name should be XX-XXX-000.")
ip_address_regex = RegexValidator(constants.IP_ADDRESS_REGEX,message="Please write a proper ip address")
domain_name_regex = RegexValidator(constants.DOMAIN_NAME_REGEX,message="Please write a proper domain name")
model_number_regex = RegexValidator(constants.MODEL_NUMBER_REGEX,message="Please write a proper model number")
key_label_regex = RegexValidator(constants.KEY_LABEL_REGEX,message="Please write a proper key label .THE PROPER FORMAT IS XX-XXX-XXX-XXX000")


general_regex = RegexValidator(constants.GENERAL_REGEX,message="Please add a proper notice period. Only A-Z, a-z and 0-9 are allowed")
specify_other_vehicle_regex = RegexValidator(constants.GENERAL_REGEX,message="Please add a proper Vehicle Name. Only A-Z, a-z and 0-9 are allowed")
last_working_day_regex = RegexValidator(constants.LAST_WORKING_DAY_REGEX,message="Please write a proper date. The format is Y-M-D")


# External Party List Regex
vendor_supplier_company_regex  = RegexValidator(constants.VENDOR_SUPPLY_COMPANY_REGEX,message="Only A-z, a-z, 0-9 and (@#-_) special characters and one space in between characters are allowed")
services_types_regex  = RegexValidator(constants.SERVICES_TYPE_REGEX,message="Only A-z, a-z, 0-9 and (@#-_) special characters and one space in between characters are allowed")


# Faqs

faq_question_regex =  RegexValidator(constants.FAQ_QUESTION_REGEX,message="Only A-Z, a-z, 0-9 and special characters (@ # - ; : |) and one space in between characters are allowed")

# Blog Name Regex
blog_name_regex =  RegexValidator(constants.BLOG_NAME_REGEX,message="Only A-Z, a-z, 0-9 and special characters (@ # - ; : |) and one space in between characters are allowed")
