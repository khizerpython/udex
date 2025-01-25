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

const CTO_DEPARTMENT_UUID = "6b200d87-f2bc-4835-88cf-c3e02329dc51";


// Department uuids for employee registration second step
const IT_SUPPORT_DEPARTMENT_UUID = "bd3785ff-fbd1-4466-9d14-c7faf6f5cd80";
const RAPID_SUPPORT_DEPART_UUID = "1c350295-c922-4e2d-8251-e37dde0b0ee7"
const ADMIN_DEPART_UUID = "57257098-7cee-4ede-92d9-db4aeaf08a57"
const SUPPLY_CHAIN_DEPART_UUID = "207b468f-545f-4ff5-818d-f280efa799df"
const INFOSEC_DEPART_UUID = "1a4eb520-06d8-4454-a13c-202a7f668b68"
const HR_DEPART_UUID  = "c7373ee3-8bb1-4a1b-ae21-5a185106347d"


// Employee Registration WorkFlow second step
const EMPLOYEE_REGISTRATION_WORKFLOW_SECOND_STEP_UUID = "45b5ee0a-6234-4674-a035-133a59f87ec9"

// Employee Registration WorkFlow third step
const EMPLOYEE_REGISTRATION_WORKFLOW_THIRD_STEP_UUID = "fc0c559c-a5a4-471a-931f-17a701721234"

// Employee DeRegistration WorkFlow second step
const EMPLOYEE_DEREGISTRATION_WORKFLOW_SECOND_STEP_UUID = "43e4236c-9257-459c-949a-412778c0f2bf"


// Employee DeRegistration WorkFlow third step
const EMPLOYEE_DEREGISTRATION_THIRD_STEP_UUID = "2991fe3d-be79-43b2-b114-1003c7070b26"

// Employee DeRegistration WorkFlow fourth step
const EMPLOYEE_DEREGISTRATION_WORKFLOW_FOURTH_STEP_UUID = "781e9293-648a-4ae8-aba0-b7dbc32a3f1e"



const EMPLOYEE_REGISTRATION_REINITIATION_INPUT_FIELDS_NAME = ['model_number','system_name','ip_address','domain_name']

// Employee Registration workflow history excluded keys
const EMPLOYEE_REGISTRATION_HISTORY_EXCULDED_KEYS = ['department_id','initiated_by','workflow_focus_column','workflow_topic','next_approver']
const EXCLUDE_NEXT_STEP_KEY = ['next_step_id_id']
const CHANGE_MANAGEMENT_OTHER_CHANGE = 'Other'

// CHANGE MANAGEMENT EXCLUDED KEYS 
const CHANGE_MANAGEMENT_EXCLUDED_KEYS = ['backdoor','backdoor_date_and_time','case_id','workflow_execution_step_id']

// EQIPMENT INVENTORY LIST Excluded keys
const EQUIPMENT_INVENTORY_LIST_EXCLUDED_KEYS = ['case_id','workflow_execution_step_id']
const EXTERNAL_PARTY_EXCLUDED_KEYS = ['case_id','workflow_execution_step_id']
const EMLOYEE_DEREGISTRATION_EXCLUDED_KEYS = ['case_id','workflow_execution_step_id']
const EMLOYEE_REGISTRATION_EXCLUDED_KEYS = ['case_id','workflow_execution_step_id']


// Corrective and Preventice Action step step id
const CORRECTIVE_AND_PREVENTIVE_ACTION_SECOND_STEP_UUID  ='4aad5d4e-1e48-4ecf-bd3a-25cbc6912239'


const HOD_ROLE_NAME = 'HOD'

const MAX_MULTIPLE_ASSET_INPUTS = 5;
const FILE_FIELD_ICON_CONTENT = "Only following extensions are allowed jpeg, jpg, pdf, doc, docx, xlsx, csv, msg"
const CTO_ASSET_PROTECTED_OPTIONS = ["Not applicable", "Storage/Hard drive removed", "Information wiped off", "Information is encrypted", "Information is sent in text but accompanied by company official", "Hard copy information is securely sealed"]
const CTO_TRANSPORTATION_INSURED = ["Not applicable", "Yes", "No"]
const HISTORY_KEYS_MAPPER = {
    'action':'Action',
    'change_type':'Change Type',
    'depart_user':'Department Employee',
    'category_choice':'Severity',
    'propose_change': 'Proposed Change',
    'contingency_plan': 'Contingency Plan',
    'close_date': 'Close Date',
    'process_to_be_change':'Process to be Change',
    'reason': 'Reason',
    'duration': 'Duration',
    'time_unit': 'Time Unit',
    'activity_start_date':'Activity Start Date',
    'days_option': 'Days',
    'minutes':'Minutes',
    'hours':'Hours',
    'months_option':'Months',
    'month_weeks':'Weeks',
    'month_days':'Days',
    'years_option':'Years',
    'year_months':'Months',
    'year_weeks':'Weeks',
    'nature': 'Nature',
    
    'asset_id': 'Asset Ids',
    'to_location': 'To Location',
    'from_location': 'From Location',
    'movement_type' : 'Movement Type',
    'other_to_location': "Other Specified Location",
    
    'basic': "Basis",
    'department':"Department",
    'department_name':"Department",
    'info_asset_protected': "Info Asset Protected",
    'transport_is_insured':"Transport is Insured",
    'incident_severity':"Incident Severity",
    'incident_location':"Incident Location",
    'incident_category':"Incident Category",
    'due_date':"Due Date",
    'corrective_actions':"Corrective Actions",
    'findings':"Findings",
    'recommendations':"Recommendations",
    "date_of_incident":"Date of Incident",
    "time_of_incident":"Time of Incident",
    "corrective_and_preventive_action":"Corrective and Preventive Action",
    "root_cause":"Root Cause",
    "other":"Others",
    "nc_type":"Type of NC",
    "area_operation":"Area Operation",

    // Employee Registration
    "background_verification":"Background Verification",
    "employee_details":"Employee Details",
    "department_id":"Department",
    "designation_id":"Designation",
    "contact_number":"Contact Number",
    "cell_phone":"Cell Phone",
    "gender":"Gender",
    "email":"Email",
    "employee_id":"Employee ID",
    "first_name":"First Name",
    "fuel":"Fuel",
    "last_name":"Last Name",
    "middle_name":"Middle Name",
    "salary_packages":"Salary Packages",
    "vehicle":"Vehicle",
    "other_specify_vehicle":"Other Specify Vehicle",



    "asset_register":"Asset Register",
    "next_step_id_id":"Next Step",
    "access_right_defined":"Is access right defined ?",
    "other_isms_templates":"Other ISMS Templates",
    "account_created_on_bpm":"Account created on BPM",
    "information_security_training":"Information Security Training",
    "email":"Email",
    "email_id_is_created":"Is email id created ?",
    "registered_on_domain":"Is registered on Domain ?",
    "added_to_team_rapidcompute":"Is added to team@rapidcompute ?",
    "added_to_employees_cybernet":"Is added to employees@cyber.net.pk ?",
    "registered_on_domain_select_choice":"Registered on domain select choice",
    "machine":"Machine",
    "model_number":"Model Number",
    "key_label":"Key Label",
    "phone_number":"Phone Number",
    "cell_phone_sim_provided":"Is cell phone sim provided ?",
    "drawer_keys_is_provided":"Are drawer keys provided ?",
    "company_id_card_provided":"Is company id card provided ?",
    "static":"Static",
    "ip_address":"IP Address",
    "data_backup":"Data Backup",
    "domain_name":"Domain Name",
    "system_name":"System Name",
    "ip_address_is_assigned":"Is IP address assigned ?",
    "system_is_registered_on_domain":"Is system registered on domain?",
    "local_administrative_rights_removed":"Is local administrative rights removed ?",
    "dlp_agent_installed_and_policy_applied":"Is DLP agent installed and policy are applied ?",
    "hard_drive_of_systerm_is_fully_formatted":"Is hard drive of systerm is fully formatted ?",
    "all_unused_services_and_ports_are_blocked":"Are all unused services and ports blocked ?",
    "software_with_latest_patches_are_installed":"Are software with latest patches installed ?",
    "system_name_is_defined_as_per_naming_convention":"Is system name defined as per naming convention ?",
    "antivirious_with_latest_definitions_are_installed":"Is antivirus with latest definitions installed ?",
    "access_rights_given_on_asset_classification_folders":"Are access rights given on asset classification folders ?",
    "usd_cd_dvd_and_other_and_other_removal_media_are_blocked":"Are USB CD DVD and other removal media blocked ?",
    "email_configured_on_outlook_with_pst_location_defined_in_2_folders":"Is email configured on Outlook with pst location defined in 2 folders ?",
    "operating_system_with_latest_services_pack_and_patches_is_installed":"Is operating system with latest services pack and patches installed ?",

    // Employee Deregistration
    "user_id":"User ID",
    "email_id":"Email ID",
    "username":"User Name",
    "any_advance":"Any Advance",
    "attendance_report_for_the_period_month":"Attendance report for the period month",
    "clearance_from_other_departments":"Clearance from other departments",
    "designation_id":"Designation",
    "last_working_day":"Last working day",
    "notice_period":"Notice Period",
    "official_number":"Official Number",
    "personal_number":"Personal Number",
    "to_the_last_working_day":"To last working day",
    //  second step of employee deregistration it support and rapid support
    "software_uninstalled": "Is software uninstalled ?",
    "antivirus_uninstalled":"Is antivirus uninstalled ?",
    "hard_drive_of_systerm_is_fully_formatted":"Is hard drive of system fully formatted ?",
    "ip_address_is_deassigned":"Is IP address unassigned ?",
    "operating_system_with_latest_services_pack_and_patches_is_not_installed":"Is operating System with latest services pack and patches uninstalled ?",
    "access_rights_removed_from_asset_classification_folders" : "Are access rights removed from asset classification folder ?",
    "system_is_deregistered_on_domain":"Is system deregistered on domain",
    "email_id_deactivated":"Is email id deactivated ?",
    "deregistered_from_domain":"Is user deregistered from domain ?",
    "de_registered_on_domain_select_choice":"Deregistered from domain",
    "removed_from_employees_cybernet":"Is employee removed from employees@cyber.net.pk ?",
    "removed_from_team_rapidcompute":"Is employee removed from team@rapidcompute ?",

    // Second step employee de registration from admin options de-registration
    "cell_phone_sim_received":"Is cell phone sim received ?",
    "company_id_card_received":"Is company ID card received ?",
    "drawer_keys_is_received":"Are drawer keys received ?",
    "laptop_received":"Is laptop received ?",
    "medical_card_received":"Is medical card received ?",
    "vehicle_received":"Is vehicle received ?",
    "information_asset_collected":"Is information asset collected ?",
    "any_advance_or_outstanding":"Is any advance or outstanding taken ?",
    "clearance_from_other_department":"Is cleared from other departments ?",

    // Second step employee de registration from admin options de-registration
    "access_revoked_from_bpm":"Is access revoked from BPM portal ?",


    // External Party List 
    "access_type":"Access Type",
    "approved" :"Approved",
    "date_of_signing":"Date of Signing",
    "date_of_training":"Date oif Training",
    "expiry_month":"Expiry Month",
    "expiry_year":"Expiry Year",
    "justification":"Justification",
    "location":"Location",
    "mode_of_training":"Training Mode",
    "name_of_training":"Name of Training",
    "risk_ratings":"Risk Rating",
    "services_types":"Services Type",
    "sla_nda":"SLA/NDA",
    "sla_status":"SLA Status",
    "vendor_supplier_company":"Vendor Supplier Company",

    // External Party LisT Second Step
    "date_of_training":"Date of training",
    "external_party_authorized_person":"External party authorized person",
    "external_party_name":"External party name",
    "mode_of_training":"Mode of training",
    "type_of_training" : "Type of training",

    // Equipment Inventory 
    "responsible_person" : "Responsible Person"






    
}



const CHANGE_MANAGEMENT_ORDER_LIST = ['change_type','propose_change','contingency_plan','process_to_be_change','category_choice','activity_start_date','time_unit','duration','days_option','hours','minutes','months_option','month_weeks','month_days','years_option','year_months','year_weeks','reason','department','depart_user'] 

const ASSET_MOVEMENT_ORDER_LIST = ['asset_id','nature','movement_type','from_location','to_location',,'other_to_location','reason','info_asset_protected','transport_is_insured']

const CORRECTIVE_AND_PREVENTIVE_ACTION_ORDER_LSIT = ['department_name','area_operation','basic','nc_type','due_date','root_cause','corrective_and_preventive_action','reason','close_date']

const INCIDENT_MANAGEMENT_ORDER_LIST = ['department_name','date_of_incident','time_of_incident','incident_location','other_to_location','incident_category','other','incident_severity','reason','due_date','corrective_actions','findings','recommendations']

const EXTERNAL_PARTY_ORDER_LIST = ['vendor_supplier_company','sla_nda','justification','date_of_signing','expiry_year','expiry_month','services_types','access_type','location','risk_ratings','name_of_training','mode_of_training','date_of_training','reason']

const EQUIPMENT_INVENTORY_ORDER_LIST  =['department','employee_id','location','equipment_details', 'reason']

const EMPLOYEE_REGISTRATION_ORDER_LIST_ONE  =['department_id','first_name','last_name','contact_number','gender','designation_id','employee_id','salary_packages','fuel','cell_phone','vehicle','other_specify_vehicle','employee_details','background_verification', 'reason']

// EMPLOYEE REGISTRATION SECOND STEP KEYS
const EMPLOYEE_REGISTRATION_SECOND_STEP_ORDER_LIST_SUPPORT_HOD = ['email_id_is_created','email','registered_on_domain','registered_on_domain_select_choice','added_to_team_rapidcompute','added_to_employees_cybernet']
const EMPLOYEE_REGISTRATION_SECOND_STEP_ORDER_LIST_IT_SUPPORT_HOD = ['system_name_is_defined_as_per_naming_convention','system_name','system_is_registered_on_domain','ip_address_is_assigned','static','ip_address' //IT HOD OPTIONS
                                                                        ,'hard_drive_of_systerm_is_fully_formatted','operating_system_with_latest_services_pack_and_patches_is_installed' //IT HOD OPTIONS
                                                                        ,'software_with_latest_patches_are_installed','antivirious_with_latest_definitions_are_installed' //IT HOD OPTIONS
                                                                        ,'all_unused_services_and_ports_are_blocked','usd_cd_dvd_and_other_and_other_removal_media_are_blocked', //IT HOD OPTIONS
                                                                        'dlp_agent_installed_and_policy_applied','local_administrative_rights_removed', //IT HOD OPTIONS
                                                                        'email_configured_on_outlook_with_pst_location_defined_in_2_folders','access_rights_given_on_asset_classification_folders','data_backup']

const EMPLOYEE_REGISTRATION_SECOND_STEP_ORDER_LIST_ADMIN_HOD = ['company_id_card_provided','cell_phone_sim_provided','phone_number','drawer_keys_is_provided','key_label']
const EMPLOYEE_REGISTRATION_SECOND_STEP_ORDER_LIST_SUPPLY_CHAIN_HOD = ['machine','model_number']
const EMPLOYEE_REGISTRATION_SECOND_STEP_ORDER_LIST_IS_HOD_HOD = ['account_created_on_bpm','asset_register','access_right_defined','information_security_training','other_isms_templates']


const EMPLOYEE_DE_REGISTRATION_ORDER_LIST_ONE = ['username','user_id','department_id','designation_id','email_id','personal_number','official_number','notice_period','last_working_day','attendance_report_for_the_period_month', 'reason']
// EMPLOYEE DE REGISTRATION SECOND STEP KEYS
const EMPLOYEE_DE_REGISTRATION_SECOND_STEP_ORDER_LIST_IT_SUPPORT_HOD = ['system_name','hard_drive_of_systerm_is_fully_formatted','operating_system_with_latest_services_pack_and_patches_is_not_installed','software_uninstalled','antivirus_uninstalled','ip_address','ip_address_is_deassigned','system_is_deregistered_on_domain','domain_name','access_rights_removed_from_asset_classification_folders']
const EMPLOYEE_DE_REGISTRATION_SECOND_STEP_ORDER_LIST_SUPPORT_HOD = ['email_id_deactivated','email','deregistered_from_domain','de_registered_on_domain_select_choice','removed_from_team_rapidcompute','removed_from_employees_cybernet']
const EMPLOYEE_DE_REGISTRATION_SECOND_STEP_ORDER_LIST_ADMIN_HOD = ['company_id_card_received','medical_card_received','cell_phone_sim_received','phone_number','drawer_keys_is_received','key_label','vehicle_received'
                                                                ,'laptop_received','fuel','clearance_from_other_department','any_advance_or_outstanding','information_asset_collected']

const EMPLOYEE_DE_REGISTRATION_SECOND_STEP_ORDER_LIST_IS_HOD = ['access_revoked_from_bpm']

// Allowed File Extension for Workflow Validators
const ALLOWED_FILE_EXTENSION = "jpeg|jpg|pdf|doc|docx|xlsx|csv|msg";
const ALLOWED_FILE_EXTENSION_ERROR_MESSAGE = "Only following extensions are allowed jpeg, jpg, pdf, doc, docx, xlsx, csv, msg"

// Minimum value length for col-6 class in history modal data.
const MIN_LENGTH_FOR_COL_6 = 50;