SQLite format 3   @     -   $                                                            - -�'   �    �����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
   
    X ��|^:����Z)���yW2 � � � X                                , 7/Can delete entreprisedelete_entreprise, 7/Can change entreprisechange_entreprise& 1)Can add entrepriseadd_entreprise) 5+Can delete log entrydelete_logentry) 5+Can change log entrychange_logentry# /%Can add log entryadd_logentry  +#Can delete sitedelete_site  +#Can change sitechange_site %Can add siteadd_site& 1)Can delete sessiondelete_session& 1)Can change sessionchange_session  +#Can add sessionadd_session/ ;1Can delete content typedelete_contenttype/ ;1Can change content typechange_contenttype)
 5+Can add content typeadd_contenttype 	 +#Can delete userdelete_user  +#Can change userchange_user %Can add useradd_user" -%Can delete groupdelete_group" -%Can change groupchange_group 'Can add groupadd_group, 7/Can delete permissiondelete_permission, 7/Can change permissionchange_permission& 1)Can add permissionadd_permission
    ������vdR<#
�������r\G/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               /delete_entreprise/change_entreprise)add_entreprise+delete_logentry+change_logentry%add_logentry#delete_site#change_siteadd_site)delete_session)change_session#add_session1delete_contenttype1change_contenttype+add_contenttype
#delete_user	#change_useradd_user%delete_group%change_groupadd_group/delete_permission/change_permission)add_permission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  �  ��$q                                                                                                                                                                  �++�Stableauth_permissionauth_permissionCREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
)=Q+ indexsqlite_autoindex_auth_permission_1auth_permission�99�Utableauth_group_permissionsauth_group_permissionsCREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
)K_9 indexsqlite_autoindex_auth_group_permissions_1auth_group_permissions�!!�ctableauth_groupauth_groupCREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
)    C@��                                                                                                                                                                                                                                                            3G! indexsqlite_autoindex_auth_group_1auth_group�z--�'tableauth_user_groupsauth_user_groupsCREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
)?S- indexsqlite_autoindex_auth_user_groups_1auth_user_groups	�'	AA�Ytableauth_user_user_permissionsauth_user_user_permissionsCREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
)S
gA indexsqlite_autoindex_auth_user_user_permissions_1auth_user_user_permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 d d                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          � �'AApbkdf2_sha256$10000$Ne6QPgb6Hz2g$lct0N0y4dqgiljPBJI9Bss0b/x/Wk+FjN6oqnC01FhA=2013-11-18 12:22:10.874444letsider2013-11-18 12:22:10.874444
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         letsider    �  �u��                                                                                                                                                        �J�ctableauth_userauth_userCREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
)1E indexsqlite_autoindex_auth_user_1auth_user�33�Ctabledjango_content_typedjango_content_typeCREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
)EY3 indexsqlite_autoindex_django_content_type_1django_content_type    ����r^A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    # !!!entrepriseentrepriseentreprise log entryadminlogentry sitesitessite sessionsessionssession( %%#content typecontenttypescontenttype userauthuser groupauthgroup !!permissionauthpermission
   a {����a��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         !!entrepriseentrepriseadminlogentrysitessitesessionssession%#contenttypescontenttypeauthuserauthgroup!authpermission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  �  �`�L                                                                                                                                         �D))�Ctabledjango_sessiondjango_sessionCREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);O) indexsqlite_autoindex_django_session_1django_session�,##�tabledjango_sitedjango_siteCREATE TABLE "django_site" (
    "id" integer NOT NULL PRIMARY KEY,
    "domain" varchar(100) NOT NULL,
    "name" varchar(50) NOT NULL
)�1--�tabledjango_admin_logdjango_admin_logCREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" datetime NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "content_type_id" integer REFERENCES "django_content_type" ("id"),
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL,
    "change_message" text NOT NULL
)   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ##example.comexample.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 � ��9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              �                                                                c                                                                  C                            !	 tezefzefef�ergrterg�    J  J�@�}                                                        �l77�wtableentreprise_entrepriseentreprise_entrepriseCREATE TABLE "entreprise_entreprise" (
    "id" integer NOT NULL PRIMARY KEY,
    "nom" varchar(100) NOT NULL,
    "adresse" varchar(250) NOT NULL,
    "codePostal" bigint NOT NULL,
    "ville" varchar(50) NOT NULL,
    "pays" varchar(30) NOT NULL,
    "telephone" bigint NOT NULL,
    "fax" bigint NOT NULL
)�=+�-indexauth_permission_37ef4eb4auth_permissionCREATE INDEX "auth_permission_37ef4eb4" ON "auth_permission" ("content_type_id")�K9�;indexauth_group_permissions_5f412f9aauth_group_permissionsCREATE INDEX "auth_group_permissions_5f412f9a" ON "auth_group_permissions" ("group_id")�K9�Eindexauth_group_permissions_83d7f98bauth_group_permissionsCREATE INDEX "auth_group_permissions_83d7f98b" ON "auth_group_permissions" ("permission_id")� ?-�!indexauth_user_groups_6340c63cauth_user_groupsCREATE INDEX "auth_user_groups_6340c63c" ON "auth_user_groups" ("user_id")
   p ���������������������|vp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
	
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  � �N�} �                                                                                                                                �?-�1indexdjango_admin_log_37ef4eb4django_admin_log$CREATE INDEX "django_admin_log_37ef4eb4" ON "django_admin_log" ("content_type_id")�?-�#indexauth_user_groups_5f412f9aauth_user_groupsCREATE INDEX "auth_user_groups_5f412f9a" ON "auth_user_groups" ("group_id")�(SA�Iindexauth_user_user_permissions_6340c63cauth_user_user_permissions CREATE INDEX "auth_user_user_permissions_6340c63c" ON "auth_user_user_permissions" ("user_id")�.SA�Uindexauth_user_user_permissions_83d7f98bauth_user_user_permissions!CREATE INDEX "auth_user_user_permissions_83d7f98b" ON "auth_user_user_permissions" ("permission_id")|;)�!indexdjango_session_b7b81f0cdjango_session"CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date")� ?-�!indexdjango_admin_log_6340c63cdjango_admin_log#CREATE INDEX "django_admin_log_6340c63c" ON "django_admin_log" ("user_id")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              