create sequence if not exists auth_group_id_seq; alter table auth_group alter column id set default nextval('auth_group_id_seq'); alter sequence auth_group_id_seq owned by auth_group.id;
create sequence if not exists auth_group_permissions_id_seq; alter table auth_group_permissions alter column id set default nextval('auth_group_permissions_id_seq'); alter sequence auth_group_permissions_id_seq owned by auth_group_permissions.id;
create sequence if not exists auth_permission_id_seq; alter table auth_permission alter column id set default nextval('auth_permission_id_seq'); alter sequence auth_permission_id_seq owned by auth_permission.id;
create sequence if not exists auth_user_id_seq; alter table auth_user alter column id set default nextval('auth_user_id_seq'); alter sequence auth_user_id_seq owned by auth_user.id;
create sequence if not exists auth_user_groups_id_seq; alter table auth_user_groups alter column id set default nextval('auth_user_groups_id_seq'); alter sequence auth_user_groups_id_seq owned by auth_user_groups.id;
create sequence if not exists auth_user_user_permissions_id_seq; alter table auth_user_user_permissions alter column id set default nextval('auth_user_user_permissions_id_seq'); alter sequence auth_user_user_permissions_id_seq owned by auth_user_user_permissions.id;
create sequence if not exists ccode_id_seq; alter table ccode alter column id set default nextval('ccode_id_seq'); alter sequence ccode_id_seq owned by ccode.id;
create sequence if not exists chanpar_id_seq; alter table chanpar alter column id set default nextval('chanpar_id_seq'); alter sequence chanpar_id_seq owned by chanpar.id;
create sequence if not exists confirmrule_id_seq; alter table confirmrule alter column id set default nextval('confirmrule_id_seq'); alter sequence confirmrule_id_seq owned by confirmrule.id;
create sequence if not exists django_admin_log_id_seq; alter table django_admin_log alter column id set default nextval('django_admin_log_id_seq'); alter sequence django_admin_log_id_seq owned by django_admin_log.id;
create sequence if not exists django_content_type_id_seq; alter table django_content_type alter column id set default nextval('django_content_type_id_seq'); alter sequence django_content_type_id_seq owned by django_content_type.id;
create sequence if not exists partnergroup_id_seq; alter table partnergroup alter column id set default nextval('partnergroup_id_seq'); alter sequence partnergroup_id_seq owned by partnergroup.id;
create sequence if not exists routes_id_seq; alter table routes alter column id set default nextval('routes_id_seq'); alter sequence routes_id_seq owned by routes.id;
create sequence if not exists translate_id_seq; alter table translate alter column id set default nextval('translate_id_seq'); alter sequence translate_id_seq owned by translate.id;
create sequence if not exists ta_id_seq; alter table ta alter column idta set default nextval('ta_id_seq'); alter sequence ta_id_seq owned by ta.idta;

