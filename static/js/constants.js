const ReturnEncryptionDecryptionIVKey = 'BBBBBBBBBBBBBBBB'
const FILE_SIZE_in_bytes = 5242880 
const FILE_SIZE_ERROR_MESSAGE  = "File size must be less than 5 MB."

const DESCRIPTION_REGEX = /^[\w\d\-_,.@&%\"' \n]*$/;
const NAME_REGEX = /^([a-zA-Z]+)((\s)([a-zA-Z]+))*$/;
const DESIGNATION_NAME_REGEX = /^(?!.*(?:- | -))(?!.* $)[a-zA-Z]+(?:-[a-zA-Z0-9]+)*(?: [a-zA-Z0-9]+)*$/;
const ROLE_NAME_REGEX = /^([a-zA-Z]+)((\s)([a-zA-Z&]+))*$/;
const USERNAME_REGEX = /^(?=[A-Za-z]{1})([a-zA-Z0-9@#_.-]){3,25}$/;
const PASSWORD_REGEX = /^.*(?=.{6,50})(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\W]).*$/;
const EMPLOYEE_ID_REGEX = /^[0-9]{5}$/;
const URL_NAME_REGEX = /^([a-zA-Z_]*){1,255}$/;
const CONTACT_NUMBER_REGEX = /((\+923|03)[\d]{9}$|(09)[\d]{8}$|(92)[\d]{10}$|(^\d{11})$)/;
const EMAIL_ADDRESS_REGEX = /^\w+([\.-]?|[\w])*@\w+([\.-]?[\w+])*(\.\w{2,3})+$/;
const ASSET_ID_REGEX = /^(?!\s)[\w\d\-_#!]*(\s[\w\d\-_#!]+)*$/;
// const SPECIFY_LOCATION_REGEX = /^[a-zA-Z0-9\-_#!]+(?: [a-zA-Z0-9\-_#!]+)*$/;
const SPECIFY_LOCATION_REGEX = /^[a-zA-Z0-9\-_#!()]+(?: [a-zA-Z0-9\-_#!()]+)*$/;
const CHANGE_MANAGEMENT_REGEX = /^[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$/;

const SYSTEM_NAME_REGEX = /^[A-Z]{2}-[A-Z]{2,6}-\d{3,5}$/
const IP_ADDRESS_REGEX  = /^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/
const DOMAIN_NAME_REGEX = /^[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(\.[a-zA-Z0-9][a-zA-Z0-9-]{0,62})*\.[a-zA-Z]{2,}$/
const MODEL_NUMBER_REGEX  = /^(?=[A-Za-z])([\w@#-]+(?: [\w@#-]+)*)$/
const KEY_LABEL_REGEX = /^[A-Z]{2}-[A-Z]{3}-[A-Z]{3}-([A-Z]+[0-9]+)$/

const GENERAL_REGEX  = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9]+)*$/
const LAST_WORKING_DAY_REGEX  =/^\d{4}-\d{2}-\d{2}$/

// External Party List
const VENDOR_SUPPLY_COMPANY_REGEX  = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_]+)*$/
const SERVICES_TYPE_REGEX = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_\.,']+)*$/


const ADDRESS_REGEX = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_\.,']+)*$/;
const FAX_REGEX = /^\+[\d]+[-][\d]+[-][\d]+$/;


// External Party Third Step Regex
const EQUIPMENT_NAME_REGEX  = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_]+)*$/
const TRAINING_TYPE_REGEX  = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_]+)*$/
const EXTERNAL_PARTY_NAME_REGEX  = /^[A-Za-z0-9]+(?:\s[A-Za-z0-9@#-_]+)*$/
const EXTERNAL_PARTY_AUTHORIZED_PERSON_REGEX = /^([a-zA-Z]+)((\s)([a-zA-Z]+))*$/;
const TRAINING_MODE_REGEX = /^([a-zA-Z]+)((\s)([a-zA-Z]+))*$/;


const HOD_ROLE_NAME = 'HOD'

const MAX_MULTIPLE_ASSET_INPUTS = 5;
const FILE_FIELD_ICON_CONTENT = "Only following extensions are allowed jpeg, jpg, pdf, doc, docx, xlsx, csv, msg"


// Allowed File Extension for Workflow Validators
const ALLOWED_FILE_EXTENSION = "jpeg|jpg|pdf|doc|docx|xlsx|csv|msg";
const ALLOWED_FILE_EXTENSION_ERROR_MESSAGE = "Only following extensions are allowed jpeg, jpg, pdf, doc, docx, xlsx, csv, msg"

// Minimum value length for col-6 class in history modal data.
const MIN_LENGTH_FOR_COL_6 = 50;