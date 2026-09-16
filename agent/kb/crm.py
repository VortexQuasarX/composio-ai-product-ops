"""
Knowledge base definitions for CRM AND SALES category (10 apps).
"""

CRM_APPS = {
    "salesforce": {
        "website": "https://developer.salesforce.com",
        "one_line_description": "Enterprise cloud CRM platform for sales, customer relationship operations, and automated workflows.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token", "Session/Cookie"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Connected Apps JWT Bearer Flow"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Free Developer Edition orgs are self-serve without credit card; production orgs require tenant admin approval."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SOAP", "GraphQL", "SDK", "CLI"],
            "rest": True,
            "graphql": True,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["SObjects", "Leads", "Opportunities", "Accounts", "Contacts", "Metadata", "Bulk API"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/modelcontextprotocol/servers",
            "notes": "Composio provides production Salesforce toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm",
                "title": "Salesforce REST API Developer Guide",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "Salesforce REST API provides a powerful, convenient, and simple Web services API for interacting with Lightning Platform. It supports OAuth 2.0 authentication and standard HTTP methods."
            },
            {
                "url": "https://developer.salesforce.com/signup",
                "title": "Salesforce Developer Edition Signup",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Developer account"],
                "excerpt": "Sign up for a free, full-featured Developer Edition of Salesforce to build, test, and package applications without expiring."
            }
        ]
    },
    "hubspot": {
        "website": "https://developers.hubspot.com",
        "one_line_description": "Inbound marketing, customer relationship management, and sales pipeline software suite.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Private App Access Tokens (Bearer)"
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
            "notes": "Free HubSpot Developer Accounts allow self-serve creation of test accounts, OAuth apps, and Private App tokens."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "CLI", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["CRM Objects", "Contacts", "Companies", "Deals", "Tickets", "Engagements", "Workflows"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/hubspot",
            "notes": "Composio provides comprehensive HubSpot toolkit; community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://developers.hubspot.com/docs/api/overview",
                "title": "HubSpot API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "HubSpot's API gives developers full access to CRM records, marketing assets, and platform workflows using standard REST protocols."
            },
            {
                "url": "https://developers.hubspot.com/docs/api/private-apps",
                "title": "HubSpot Private Apps Documentation",
                "source_type": "official_auth_docs",
                "supports": ["Bearer Token", "Self-serve free"],
                "excerpt": "Private apps allow developers to generate custom access tokens to authenticate API calls without public app marketplace review."
            }
        ]
    },
    "pipedrive": {
        "website": "https://developers.pipedrive.com",
        "one_line_description": "Sales-focused customer relationship management tool emphasizing visual deal pipelines.",
        "authentication": {
            "methods": ["OAuth2", "API Key"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Personal API Token"
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
            "notes": "14-day free trial available without credit card; sandbox accounts provided via Pipedrive Developer Program."
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
            "major_resource_areas": ["Deals", "Persons", "Organizations", "Activities", "Pipelines", "Products", "Notes"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/pipedrive",
            "notes": "Composio provides Pipedrive toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://developers.pipedrive.com/docs/api/v1",
                "title": "Pipedrive API v1 Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API Key"],
                "excerpt": "Pipedrive API v1 offers access to deals, persons, and pipeline operations using OAuth 2.0 or personal API tokens."
            }
        ]
    },
    "attio": {
        "website": "https://attio.com",
        "one_line_description": "Real-time, schema-driven relationship management platform designed for modern tech teams.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
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
            "notes": "Free tier enables instant self-serve API key generation in workspace settings."
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
            "major_resource_areas": ["Objects", "Records", "Attributes", "Lists", "Notes", "Tasks", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/attio",
            "notes": "Composio supports Attio actions; community MCP servers exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://developers.attio.com/reference/overview",
                "title": "Attio API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "API availability"],
                "excerpt": "Attio API provides programmatic access to read and write records, custom objects, and workspace attributes via Bearer authentication."
            }
        ]
    },
    "twenty": {
        "website": "https://twenty.com",
        "one_line_description": "Open-source extensible CRM designed as a self-hostable alternative to traditional enterprise CRMs.",
        "authentication": {
            "methods": ["Bearer Token", "API Key", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
        },
        "credential_access": {
            "self_serve": True,
            "free_access": True,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": False,
            "access_classification": "Self-serve free",
            "notes": "Open-source codebase is freely self-hostable with full API access; Twenty Cloud offers self-serve free tier."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "GraphQL", "Webhooks"],
            "rest": True,
            "graphql": True,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Standard Objects", "Custom Objects", "Core Workspace", "Activities", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/twentyhq/twenty",
            "notes": "Composio supports Twenty CRM; community MCP connectors available on GitHub."
        },
        "evidence": [
            {
                "url": "https://docs.twenty.com/developers/api/",
                "title": "Twenty Developer API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "GraphQL", "Bearer Token"],
                "excerpt": "Twenty exposes both REST and GraphQL endpoints for interacting with all CRM entities, custom fields, and metadata models."
            }
        ]
    },
    "podio": {
        "website": "https://podio.com",
        "one_line_description": "Customizable workspace and work management CRM platform by Citrix.",
        "authentication": {
            "methods": ["OAuth2", "API Key"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Server-side and App authentication"
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
            "notes": "Free tier for up to 5 employees includes developer API key creation."
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
            "breadth": "Moderate",
            "major_resource_areas": ["Items", "Apps", "Workspaces", "Tasks", "Comments", "Files"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://developer.podio.com",
            "notes": "Composio supports Podio; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.podio.com/",
                "title": "Podio API Developer Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "The Podio API allows third-party developers to access items, apps, and workspaces using OAuth 2.0 authentication."
            }
        ]
    },
    "zoho-crm": {
        "website": "https://zoho.com/crm",
        "one_line_description": "Comprehensive customer relationship management software suite for multi-channel sales teams.",
        "authentication": {
            "methods": ["OAuth2"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": None
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
            "notes": "Zoho Developer Console and Zoho CRM free tier allow self-serve creation of OAuth client credentials."
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
            "breadth": "Very broad",
            "major_resource_areas": ["Leads", "Contacts", "Accounts", "Deals", "Modules", "Blueprints", "Org Settings"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/zoho",
            "notes": "Composio provides Zoho CRM toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://www.zoho.com/crm/developer/docs/api/v6/",
                "title": "Zoho CRM REST API v6 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "Zoho CRM REST APIs allow developers to perform CRUD operations on CRM modules using OAuth 2.0 access tokens."
            }
        ]
    },
    "close": {
        "website": "https://close.com",
        "one_line_description": "Sales communication and CRM software with integrated VOIP calling, SMS, and email sequencers.",
        "authentication": {
            "methods": ["API Key", "Basic Auth"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "HTTP Basic Auth with API key as username"
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
            "notes": "14-day free trial allows self-serve API key provisioning; paid commercial plan required thereafter."
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
            "major_resource_areas": ["Leads", "Contacts", "Opportunities", "Activities", "Tasks", "Custom Fields", "Phone Calls"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/close",
            "notes": "Composio supports Close CRM; community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://developer.close.com/",
                "title": "Close API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Basic Auth"],
                "excerpt": "The Close API is organized around REST. All requests must be authenticated using HTTP Basic Auth using your API key as the username."
            }
        ]
    },
    "copper": {
        "website": "https://copper.com",
        "one_line_description": "CRM solution purpose-built for Google Workspace with direct integration into Gmail and Drive.",
        "authentication": {
            "methods": ["API Key", "OAuth2"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "X-PW-AccessToken + X-PW-Application headers"
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
            "notes": "14-day free trial includes self-serve API key generation; paid plan required after trial."
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
            "major_resource_areas": ["Leads", "People", "Companies", "Opportunities", "Tasks", "Projects", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/copper",
            "notes": "Composio supports Copper CRM; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://developer.copper.com/",
                "title": "Copper Developer Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "OAuth2"],
                "excerpt": "Copper REST API requires API key authentication via X-PW-AccessToken and X-PW-UserEmail headers."
            }
        ]
    },
    "dealcloud": {
        "website": "https://api.docs.dealcloud.com",
        "one_line_description": "Financial services and private capital CRM platform by Intapp for dealmaking and compliance.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Intapp OnePlace API Key"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": True,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Contact-sales gated",
            "notes": "Enterprise financial CRM with strictly gated sales access; no self-serve developer registration available."
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
            "major_resource_areas": ["Deals", "Intermediaries", "Contacts", "Companies", "Pipelines", "Audit Logs"]
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No MCP server found; not supported by Composio."
        },
        "evidence": [
            {
                "url": "https://api.docs.dealcloud.com/",
                "title": "DealCloud API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "API availability"],
                "excerpt": "DealCloud API provides programmatic access to enterprise deal data, requiring authorized Bearer token authentication issued to licensed client tenants."
            },
            {
                "url": "https://www.intapp.com/dealcloud/",
                "title": "Intapp DealCloud Enterprise Platform",
                "source_type": "official_pricing",
                "supports": ["Contact-sales gated", "Paid plan required"],
                "excerpt": "Intapp DealCloud is an enterprise solution tailored for investment banking, private equity, and advisory firms available via institutional sales consultation."
            }
        ]
    }
}
