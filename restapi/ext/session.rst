session - получение информации по сессии пользователя
=============================================================================

GET /restapi/services/run/session
Authorization: Bearer <token>

.. code-block:: json

	{
		"alerts": [],
		"domain": "localhost",
		"errNum": 0,
		"errText0": "",
		"errrrrrText2": 0,
		"errrrrrr2": "",
		"events": [
			{
				"created_at": "2017-01-15T20:21:52+06:00",
				"created_by": "1",
				"html": "Актуализация информации",
				"id": "1",
				"is_closed": "1",
				"manager_id": "1",
				"percent": "90",
				"sys$uuid": "9bd94352-088b-45bf-9e57-520017a88a1f",
				"title": "Актуализация информации",
				"updated_at": "2020-12-14T14:21:22+06:00",
				"updated_by": "1",
				"url": "http://www.semsk.kz"
			},
			{
				"created_at": "2017-01-15T20:22:24+06:00",
				"created_by": "1",
				"html": "Актуализация информации",
				"id": "2",
				"is_closed": "1",
				"manager_id": "1",
				"percent": "70",
				"sys$uuid": "0a69bdb8-d422-47bf-afb1-7f3ba49eea38",
				"title": "Встреча с клиентом",
				"updated_at": "2020-12-14T13:54:11+06:00",
				"updated_by": "1",
				"url": "http://www.semsk.kz"
			},
			{
				"created_at": "2017-01-15T20:22:46+06:00",
				"created_by": "1",
				"html": "Актуализация информации",
				"id": "3",
				"is_closed": "1",
				"manager_id": "1",
				"percent": "30",
				"sys$uuid": "b6a64606-37d2-4efa-9e50-7a30636a2b73",
				"title": "Поздравить с днем рождения",
				"updated_at": "2020-12-14T13:54:15+06:00",
				"updated_by": "1",
				"url": "http://www.semsk.kz"
			},
			{
				"created_at": "2017-04-16T10:58:49+06:00",
				"created_by": "1",
				"html": "test",
				"id": "4",
				"is_closed": "1",
				"manager_id": "1",
				"sys$uuid": "c95e3efe-63b7-49dc-8469-fa3cb1b10428",
				"title": "test",
				"updated_at": "2020-12-14T13:54:26+06:00",
				"updated_by": "1",
				"url": "http://www.semsk.kz"
			}
		],
		"quick_actions": [
			{
				"created_at": "2020-05-29T17:15:06+06:00",
				"created_by": "1",
				"dscr": "Создание, разработка сущностей",
				"icon": "flaticon-settings icon-5x",
				"id": "1",
				"page_id": "8",
				"sys$uuid": "bdb1c409-9fdb-49e1-9781-d75cef952898",
				"title": "Сущности",
				"updated_at": "2020-05-29T17:32:08+06:00",
				"url": "#/settings/entities"
			},
			{
				"created_at": "2020-05-29T17:33:10+06:00",
				"created_by": "1",
				"dscr": "Создание, сброс пароля",
				"icon": "flaticon-users icon-5x",
				"id": "2",
				"page_id": "13",
				"sys$uuid": "56e6cf3d-8e40-45ca-a75e-ba758a81f891",
				"title": "Пользователи",
				"updated_at": "2020-05-29T17:33:10+06:00",
				"url": "#/settings/users"
			}
		],
		"session_parameters": [
			{
				"code": "show_header",
				"title": "Show Header",
				"value": "1"
			},
			{
				"code": "show_left_sidebar",
				"title": "Show left sidebar",
				"value": "1"
			},
			{
				"code": "show_theme_panel",
				"title": "show Theme Panel",
				"value": "0"
			},
			{
				"code": "deleteall_enabled",
				"title": "Delete All Enabled",
				"value": "0"
			},
			{
				"code": "custom",
				"title": "Custom",
				"value": "002"
			},
			{
				"code": "custom_css",
				"title": "Custom CSS",
				"value": "crm/crm.css"
			},
			{
				"code": "force_resetpassword",
				"title": "force_resetpassword",
				"value": "1"
			},
			{
				"code": "disable_header_logo",
				"title": "disable_header_logo",
				"value": "0"
			},
			{
				"code": "generate_ddl",
				"title": "Generate DDL",
				"value": "1"
			},
			{
				"code": "show_header_language_bar",
				"title": "show_header_language_bar",
				"value": "1"
			},
			{
				"code": "enable_widget_designer",
				"title": "enable_widget_designer",
				"value": "1"
			},
			{
				"code": "hide_header_profile_bar",
				"title": "hide_header_profile_bar",
				"value": "0"
			},
			{
				"code": "show_footer",
				"title": "show_footer",
				"value": "1"
			},
			{
				"code": "custom_layout_css",
				"title": "custom_layout_css",
				"value": "theme/assets/admin/layout/css/layout.css"
			},
			{
				"code": "barcode_reader_listener_include",
				"title": "barcode_reader_listener_include",
				"value": "0"
			},
			{
				"code": "theme_css",
				"title": "theme_css",
				"value": "/cms/css/bi-group-new.css"
			},
			{
				"code": "is_dev_instance",
				"title": "Разработческая инстанция",
				"value": "1"
			},
			{
				"code": "hide_header_profile_myprofile",
				"title": "hide_header_profile_myprofile",
				"value": "hide_header_profile_myprofile"
			},
			{
				"code": "shortDateTimeFormat",
				"title": "shortDateTimeFormat",
				"value": "DD.MM.YYYY HH:mm"
			},
			{
				"code": "shortDateFormat",
				"title": "shortDateFormat",
				"value": "DD.MM.YY"
			},
			{
				"code": "longDateFormat",
				"title": "longDateFormat",
				"value": "DD.MM.YY"
			},
			{
				"code": "longDateTimeFormat",
				"title": "longDateTimeFormat",
				"value": "DD.MM.YY HH:mm"
			},
			{
				"code": "index_widget",
				"title": "index_widget",
				"value": "/restapi/widget/index_default"
			},
			{
				"code": "header_logo_url",
				"title": "Header Logo URL",
				"value": "https://damu1.bapps.kz/restapi/getfile?code=cms-2ae869a2-9c77-413d-9f50-4ed4641df345"
			},
			{
				"code": "version",
				"title": "Version",
				"value": "1.3.1"
			},
			{
				"code": "page_cache",
				"title": "Кэширование страниц",
				"value": "0"
			},
			{
				"code": "shortTimeFormat",
				"value": "HH:mm"
			},
			{
				"code": "shortcut_icon_url",
				"title": "shortcut_icon_url",
				"value": "https://vps4.bapps.kz:19999/restapi/getfile?code=images-d1dbec8b-37bc-49c8-b7e9-ae1e287a6c4d\u0026attachment=true"
			},
			{
				"code": "header_search_uri",
				"title": "header_search_uri",
				"value": "#/core/search/?text="
			},
			{
				"code": "header_logo_url3_1",
				"title": "header_logo_url3_1",
				"value": "/static5/assets/img/logo-white.svg"
			},
			{
				"code": "header_logo_url3_2",
				"title": "header_logo_url3_2",
				"value": "/static3/assets/media/logos/damu-crm-logo-dark.png"
			},
			{
				"code": "show_header_inbox",
				"title": "show_header_inbox",
				"value": "0"
			},
			{
				"code": "angular_logo_2",
				"title": "Angular Logo 2",
				"value": "/static/img/logos/damu-crm-logo-dark-white.png"
			},
			{
				"code": "angular_logo_3",
				"title": "Angular Logo 3",
				"value": "/restapi/getfile?code=CUST-8f046b5b-970c-4810-a39b-3fada5f24593\u0026attachment=true"
			},
			{
				"code": "ui_show_patch_info_in_detail",
				"title": "Показывать информацию по патче в детализации",
				"value": "1"
			},
			{
				"code": "ui_show_browse_button",
				"title": "ui_show_browse_button",
				"value": "1"
			},
			{
				"code": "angular_start_url",
				"title": "angular_start_url",
				"value": "in_etg_doc"
			},
			{
				"code": "angular_index_widget",
				"title": "angular_index_widget",
				"value": "5"
			},
			{
				"code": "loginpage",
				"title": "Default Login Page Code",
				"value": "/cms/page/login_cms"
			},
			{
				"code": "angular_logo_1",
				"title": "Angular Logo 1",
				"value": "http://localhost/restapi/getfile?code=cms-2ae869a2-9c77-413d-9f50-4ed4641df345"
			}
		],
		"session_role_params": [
			{
				"code": "force_resetpassword",
				"value": "1"
			},
			{
				"code": "is_admin",
				"value": "1"
			},
			{
				"code": "generate_ddl",
				"value": "1"
			},
			{
				"code": "generate_bpm",
				"value": "1"
			},
			{
				"code": "enable_widget_designer",
				"value": "1"
			},
			{
				"code": "ui_show_browse_button",
				"value": "1"
			}
		],
		"session_roles": [
			{
				"code": "admin"
			},
			{
				"code": "admin"
			}
		],
		"sessioninfo": {
			"age": "36",
			"avatar_url": "\u0026thumb=120-0",
			"bp_process_roles_list": [
				"entity_export_to_file",
				"entity_import_from_file",
				"entity_publish",
				"user_lock",
				"page_create_menu",
				"exp_template",
				"report_gen",
				"exp_template_export_to_file",
				"roles_copy_grants",
				"entity_attrs_process_01",
				"user_push_not",
				"entity_2_wf",
				"exp_template_wizard",
				"entity_to_ora_sql",
				"entity_export_to_remote",
				"rest_services_export_to_file",
				"users_sign",
				"locked_rows_action",
				"table_log_restore_bp_process",
				"validate_all",
				"queries_to_exp_temp",
				"entity_rename",
				"acc_cls_publish",
				"entity_to_ora_git",
				"rest_services_import_from_file",
				"export_core_update_mysql",
				"report_exp_result",
				"module_info_to_json",
				"module_info_merge_from_json",
				"export_object_to_json",
				"export_object_to_file",
				"import_object_from_file",
				"object_export_to_remote",
				"include_object_into_patch_out",
				"patch_out_to_file",
				"luas_using",
				"user_unlock",
				"entity_to_pg_git",
				"entity_process_by_url",
				"export_object_to_hash",
				"rest_services_copy",
				"users_change_old_password",
				"files_upload",
				"cms_p_file_upload",
				"cms_p_change_img_src",
				"mysqldump_core_modules",
				"eds_qrcode_read_from_pdf",
				"queries_to_exp_temp_csv",
				"users_reset_password",
				"entities_add_tp",
				"queries2chart",
				"bp_process_export_to_file",
				"core_mysql_dmp_cmd_delta",
				"details_copy",
				"pages_to_exp_temp_xls",
				"del_non_linked_rows",
				"tasks_start_approve",
				"find_linked_records",
				"entities_copy",
				"core_di_chs_test",
				"patch_out_reset",
				"crontab_reload",
				"entity_module_sql_check",
				"entity_to_mysql_git",
				"pages_copy",
				"imp2excel_to_wf",
				"csv_to_entity",
				"crontab_reload_remote",
				"sphinx_sql_to_table",
				"find_linked_rows_main_user",
				"role_grant_all_view_access_mod",
				"crontab_restart_remote",
				"email_plan_do",
				"task_reassign",
				"task_hst_add",
				"task_set_approve_t_s_id",
				"task_send_notification",
				"export_template_online",
				"exp_templates_online",
				"task_reassign_manual",
				"bp_process_insert",
				"bp_process_import_from_file",
				"workflow_notify_close",
				"task_notify_assign",
				"task_restore_manual",
				"bp_process_export_to_remote",
				"bp_ats_process_file",
				"bp_process_publish",
				"bp_process_copy",
				"bp_processes_svg_download",
				"etg_import",
				"etg_import",
				"etg_doc_wf",
				"etg_doc_set_read_dt",
				"etg_doc_task_assign",
				"etg_doc_task_report",
				"etg_doc_task_appr",
				"etg_doc_task_sign",
				"users_email_change_req",
				"users_email_change_req"
			],
			"dep_id": "104",
			"email": "admin",
			"experience": "3",
			"id": "1",
			"lang": "ru",
			"login": "admin",
			"rolesidlist": "{1,2}",
			"title": "Administrator"
		},

	}