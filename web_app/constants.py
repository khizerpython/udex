
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
DASHBOARD = "ea408d4b8c8840d6bb1c2d81ccac3b8c"

RIDER_DEPARTMENT_NAME="Operations"

# Regex

DESCRIPTION_REGEX = r"^[\w\d\-_,.@&%\"' \n]*$"


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




# WEB APP CONSTANT 
FAILURE = "548d273d-ddb8-4d37-871d-3717c5399645"
SUCCESS = "982cd9bc-d087-45f4-a2bf-fc7b23b8c639"

# Default 404 URL
DEFAULT_404_URL = "/not/found/" 