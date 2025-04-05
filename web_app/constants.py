
import os
ENCRYPTION_DECRYPTION_PASSWORD =  os.environ.get('ENCRYPTION_DECRYPTION_PASSWORD')

NEW_USER_WELCOME_EMAIL_SUBJECT = "Account Activation - UDEX"
# RAPID_BLOGS_S3_STORAGE_ROUTE =  os.environ.get('RAPID_BLOGS_S3_STORAGE_ROUTE')
# RAPID_RESOURCES_S3_STORAGE_ROUTE =  os.environ.get('RAPID_RESOURCES_S3_STORAGE_ROUTE')

# MONGO_DB_CLIENT_PATH = os.environ.get('MONGO_DB_CLIENT_PATH')

ADMIN_EMAIL_ADDRESS = 'khizerkhan736@gmail.com'

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M"
DATE_TIME_FORMAT_AM_PM = "%Y-%m-%d %I:%M %p"
DATE_FORMAT = "%Y-%m-%d"

# Regex

DESCRIPTION_REGEX = r"^[\w\d\-_,.@&%\"' \n]*$"

JOB_NAME_REGEX = r"^[A-Za-z]+(?:[\s-][A-Za-z0-9]+)*$"

NAME_REGEX = r"^([a-zA-Z]+)((\s)([a-zA-Z]+))*$"
DESIGNATION_NAME_REGEX = r"^(?!.*(?:- | -))(?!.* $)[a-zA-Z]+(?:-[a-zA-Z0-9]+)*(?: [a-zA-Z0-9]+)*$"
ROLE_NAME_REGEX = r"^([a-zA-Z]+)((\s)([a-zA-Z&]+))*$"
USERNAME_REGEX = r"^(?=[A-Za-z]{1})([a-zA-Z0-9@#_.-]){3,25}$"
PASSWORD_REGEX = r"^.*(?=.{6,50})(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\W]).*$"
EMPLOYEE_ID_REGEX = r"^[0-9]{5}$"
CONTACT_NUMBER_REGEX = r"((\+923|03)[\d]{9}$|(09)[\d]{8}$|(92)[\d]{10}$|(^\d{11})$)"
URL_NAME_REGEX = r"^([a-zA-Z_]*){1,255}$"
WORKFLOW_ABBREVIATION_REGEX = r"^[A-Z]{2,3}(\-Case [\d]+)$"
WHOLE_FORM_REGEX = r"^[\w\d\-_,.@&%\"' \n]*$"
ASSET_ID_REGEX = r"^(?!\s)[\w\d\-_#!]*(\s[\w\d\-_#!]+)*$"
SPECIFY_LOCATION_REGEX = r"^[a-zA-Z0-9\-_#!]+(?: [a-zA-Z0-9\-_#!]+)*$"



# employee registration
SYSTEM_NAME_REGEX = r'^[A-Z]{2}-[A-Z]{2,6}-\d{3,5}$'
IP_ADDRESS_REGEX = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
DOMAIN_NAME_REGEX = r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(\.[a-zA-Z0-9][a-zA-Z0-9-]{0,62})*\.[a-zA-Z]{2,}$"

MODEL_NUMBER_REGEX  = r"^(?=[A-Za-z])([\w@#-]+(?: [\w@#-]+)*)$"
KEY_LABEL_REGEX = r"^[A-Z]{2}-[A-Z]{3}-[A-Z]{3}-([A-Z]+[0-9]+)$"

GENERAL_REGEX  = r"^[A-Za-z0-9]+(?:\s[A-Za-z0-9]+)*$"
LAST_WORKING_DAY_REGEX  ="^\d{4}-\d{2}-\d{2}$"


# External Party Regex
VENDOR_SUPPLY_COMPANY_REGEX  = r"^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_]+)*$"
SERVICES_TYPE_REGEX = r"^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_\.,']+)*$"

# Faq question regex
FAQ_QUESTION_REGEX =  r"^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#_\-;:\.|]+)*$"

# Blog name regex
BLOG_NAME_REGEX =  r"^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#_\-;:\.|]+)*$"

BPMADMIN_UUID  = "a8881ea6-ae38-4e1b-ae26-3809cf831bd1"
SUPERADMIN_UUID = "6ee81df2-492a-4dfe-ae2a-3b9e3f562af5"

BPMADMINROLE_UUID = "f61deaac-b837-4258-a38b-5467c4144758"
BPMSUPERADMINROLE_UUID = "6f4a9b6f-2dbe-411c-b94b-be1ef5905583"



# WEB APP CONSTANT 
FAILURE = "548d273d-ddb8-4d37-871d-3717c5399645"
SUCCESS = "982cd9bc-d087-45f4-a2bf-fc7b23b8c639"

# Default 404 URL
DEFAULT_404_URL = "/not/found/" 