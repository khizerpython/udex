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

