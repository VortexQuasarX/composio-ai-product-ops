"""
Knowledge base definitions for PRODUCTIVITY AND PROJECT MANAGEMENT category (10 apps).
"""

PRODUCTIVITY_APPS = {
    "notion": {
        "website": "https://developers.notion.com",
        "one_line_description": "Connected workspace for notes, wikis, project management, and collaborative document databases.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Internal Integration Secret (Bearer secret_...)"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free for all Notion users; internal integration tokens can be created immediately in the Notion My Integrations portal."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Databases", "Pages", "Blocks", "Users", "Comments", "Search"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/notion",
            "notes": "Composio provides Notion toolkit; community MCP server implementations widely available on GitHub."
        },
        "evidence": [
            {
                "url": "https://developers.notion.com/reference/intro",
                "title": "Notion API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "The Notion API provides REST endpoints to read and write Notion data. Authenticate using Bearer tokens with an internal integration secret or public OAuth flow."
            },
            {
                "url": "https://www.notion.so/profile/integrations",
                "title": "Notion Integrations Portal",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Bearer Token"],
                "excerpt": "Create an integration to connect Notion with your everyday tools. Integrations can be created for free by any workspace member."
            }
        ]
    },
    "airtable": {
        "website": "https://airtable.com/developers",
        "one_line_description": "Low-code relational database and app-building platform structured like a collaborative spreadsheet.",
        "authentication": {
            "methods": ["Personal Access Token", "OAuth2", "Bearer Token"],
            "primary_method": "Personal Access Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Personal Access Tokens (pat...)"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free plan permits self-serve generation of scoped Personal Access Tokens in Airtable Developer Hub."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Records", "Bases & Tables", "Views", "Fields & Schema", "Webhooks", "Comments"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/airtable",
            "notes": "Composio provides Airtable toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://airtable.com/developers/web/api/introduction",
                "title": "Airtable Web API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Personal Access Token", "OAuth2"],
                "excerpt": "Airtable Web API provides RESTful endpoints to query and modify records. Requests authenticate via Personal Access Tokens passed as HTTP Bearer tokens."
            }
        ]
    },
    "linear": {
        "website": "https://developers.linear.app",
        "one_line_description": "High-performance issue tracking, software roadmap, and project management tool for engineering teams.",
        "authentication": {
            "methods": ["Personal Access Token", "OAuth2", "Bearer Token"],
            "primary_method": "Personal Access Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Personal API Keys (lin_api_...)"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free plan allows instant self-serve creation of Personal API Keys and OAuth applications in account settings."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["GraphQL", "SDK", "Webhooks"],
            "rest": False,
            "graphql": True,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Issues", "Projects", "Teams", "Cycles (Sprints)", "Roadmaps", "Comments", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": True,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/jerhadf/linear-mcp-server",
            "notes": "Vendor-supported Linear MCP server available; Composio provides comprehensive Linear toolkit."
        },
        "evidence": [
            {
                "url": "https://developers.linear.app/docs/graphql/working-with-the-graphql-api",
                "title": "Linear GraphQL API Reference",
                "source_type": "official_docs",
                "supports": ["GraphQL", "Personal Access Token", "OAuth2"],
                "excerpt": "Linear's API is built around GraphQL. You can authenticate requests using a personal API key or through an OAuth 2.0 application."
            }
        ]
    },
    "jira": {
        "website": "https://developer.atlassian.com",
        "one_line_description": "Agile project and issue tracking tool for enterprise software development and scrum teams by Atlassian.",
        "authentication": {
            "methods": ["Basic Auth", "OAuth2", "API Key"],
            "primary_method": "Basic Auth",
            "oauth2": True,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Basic Auth using email:api_token or OAuth 2.0 (3LO)"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Atlassian Cloud free tier (up to 10 users) provides instant self-serve API token generation via id.atlassian.com."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Issues", "Projects", "Workflows", "Sprints (Agile API)", "Dashboards", "Permissions", "Users"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/jira",
            "notes": "Composio provides Jira toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/",
                "title": "Jira Cloud REST API v3 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "OAuth2"],
                "excerpt": "Jira Cloud REST API v3 is an HTTP interface to manage Jira data. Requests are authenticated via API tokens with Basic Auth or OAuth 2.0."
            }
        ]
    },
    "asana": {
        "website": "https://developers.asana.com",
        "one_line_description": "Work and project management software for coordinating team tasks, milestones, and goals.",
        "authentication": {
            "methods": ["Personal Access Token", "OAuth2", "Bearer Token"],
            "primary_method": "Personal Access Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Personal Access Tokens generated in developer console"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free Asana tier allows self-serve generation of Personal Access Tokens in Developer App Console."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Tasks", "Projects", "Sections", "Workspaces", "Stories (Comments)", "Portfolios", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/asana",
            "notes": "Composio provides Asana toolkit; community MCP server available on GitHub."
        },
        "evidence": [
            {
                "url": "https://developers.asana.com/docs/overview",
                "title": "Asana API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Personal Access Token", "OAuth2"],
                "excerpt": "The Asana REST API provides programmatic access to tasks and projects. Authenticate using Personal Access Tokens or OAuth 2.0."
            }
        ]
    },
    "monday-com": {
        "website": "https://developer.monday.com",
        "one_line_description": "Cloud work operating system (Work OS) enabling teams to build custom workflow management apps.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Personal API Token sent in Authorization header"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free Developer Accounts can be created freely at developer.monday.com with permanent sandboxes."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["GraphQL", "SDK", "Webhooks"],
            "rest": False,
            "graphql": True,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Boards", "Items (Rows)", "Columns", "Groups", "Updates", "Users", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/monday",
            "notes": "Composio provides Monday.com toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.monday.com/api-reference/docs/introduction",
                "title": "monday.com GraphQL API Reference",
                "source_type": "official_docs",
                "supports": ["GraphQL", "Bearer Token", "Self-serve free"],
                "excerpt": "The monday.com API is built on GraphQL. Authenticate your API calls using personal API tokens or OAuth tokens passed in the Authorization header."
            }
        ]
    },
    "clickup": {
        "website": "https://clickup.com/api",
        "one_line_description": "All-in-one productivity platform combining tasks, docs, chat, goals, and sprint planning.",
        "authentication": {
            "methods": ["API Key", "OAuth2", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Personal API Key (pk_...) passed in Authorization header"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free Forever plan allows self-serve generation of personal API keys in user settings > Apps."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Tasks", "Lists", "Folders", "Spaces", "Workspaces (Teams)", "Comments", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/clickup",
            "notes": "Composio provides ClickUp toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://clickup.com/api/developer-portal/authentication/",
                "title": "ClickUp API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "OAuth2"],
                "excerpt": "ClickUp API 2.0 is a REST API. You can authenticate using personal API keys for personal scripts or OAuth 2.0 for public integrations."
            }
        ]
    },
    "coda": {
        "website": "https://coda.io/developers",
        "one_line_description": "All-in-one collaborative doc platform blending documents, spreadsheets, and interactive applications.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API Token passed as Bearer header: Authorization: Bearer <token>"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free tier enables instant self-serve generation of API tokens in Account Settings > Developer Tools."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Docs", "Pages", "Tables", "Rows", "Columns", "Formulas", "Controls", "Packs SDK"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/coda",
            "notes": "Composio provides Coda toolkit; community MCP implementations exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://coda.io/developers/apis/v1",
                "title": "Coda API v1 Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Self-serve free"],
                "excerpt": "The Coda REST API allows developers to read, insert, and update rows in Coda tables using Bearer tokens."
            }
        ]
    },
    "smartsheet": {
        "website": "https://smartsheet.com/developers",
        "one_line_description": "Enterprise collaborative work management and spreadsheet automation platform.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API Access Token (Bearer)"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve trial",
            "notes": "30-day free trial allows self-serve generation of API access tokens; paid subscription required after trial."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Sheets", "Rows", "Columns", "Workspaces", "Reports", "Users", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/smartsheet",
            "notes": "Composio supports Smartsheet; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://smartsheet.redoc.ly/",
                "title": "Smartsheet API 2.0 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "The Smartsheet API 2.0 provides REST access to sheets and automated workflows. Authenticate with an API access token passed in the Authorization header."
            }
        ]
    },
    "harvest": {
        "website": "https://help.getharvest.com/api-v2",
        "one_line_description": "Time tracking, invoicing, and team expense monitoring software for professional services.",
        "authentication": {
            "methods": ["Bearer Token", "Personal Access Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Authorization: Bearer <PAT> + Harvest-Account-Id header"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Developers can create free developer accounts at id.getharvest.com/developers to generate Personal Access Tokens."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Moderate",
            "major_resource_areas": ["Time Entries", "Clients", "Projects", "Tasks", "Invoices", "Expenses", "Users"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/harvest",
            "notes": "Composio supports Harvest; community MCP servers available on GitHub."
        },
        "evidence": [
            {
                "url": "https://help.getharvest.com/api-v2/authentication-api/overview/authentication/",
                "title": "Harvest API v2 Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Personal Access Token"],
                "excerpt": "Harvest API v2 supports two authentication methods: Personal Access Tokens and OAuth 2.0. Both methods require sending the token in an Authorization Bearer header."
            }
        ]
    }
}
