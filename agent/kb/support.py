"""
Knowledge base definitions for SUPPORT AND HELPDESK category (10 apps).
"""

SUPPORT_APPS = {
    "zendesk": {
        "website": "https://developer.zendesk.com",
        "one_line_description": "Cloud-based customer service, helpdesk ticketing, and CRM communications platform.",
        "authentication": {
            "methods": ["OAuth2", "API Key", "Basic Auth"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "HTTP Basic Auth using email/token:api_key"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve trial",
            "notes": "14-day free trial allows self-serve API token generation; admin privileges required to enable API access in admin center."
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
            "major_resource_areas": ["Tickets", "Users", "Organizations", "Help Center (Knowledge Base)", "Chat", "Voice", "Triggers"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/zendesk",
            "notes": "Composio provides Zendesk toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.zendesk.com/api-reference/ticketing/introduction/",
                "title": "Zendesk Support API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "OAuth2"],
                "excerpt": "The Zendesk Support REST API lets you manage tickets, users, and organizations using OAuth 2.0 or an API token combined with an agent's email address."
            }
        ]
    },
    "intercom": {
        "website": "https://developers.intercom.com",
        "one_line_description": "AI-first customer service and live messaging platform with automated helpdesk bots.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Access Token (Bearer)"
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
            "notes": "Intercom Developer Hub provides free developer test workspaces with instant Access Token provisioning."
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
            "major_resource_areas": ["Conversations", "Contacts", "Admins", "Articles", "Help Center", "Tickets", "Tags"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/intercom",
            "notes": "Composio supports Intercom actions; community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://developers.intercom.com/docs/references/rest-api/api.intercom.io/",
                "title": "Intercom REST API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "The Intercom API is organized around REST. All API access requires authentication using Bearer tokens obtained via OAuth or direct access token generation in the developer workspace."
            }
        ]
    },
    "freshdesk": {
        "website": "https://freshdesk.com",
        "one_line_description": "Omnichannel customer support and ticketing platform by Freshworks.",
        "authentication": {
            "methods": ["API Key", "Basic Auth", "OAuth2"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "HTTP Basic Auth using API Key as username and 'X' as password"
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
            "notes": "Freshdesk Free plan (Sprout) includes self-serve API key generation in user profile settings."
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
            "major_resource_areas": ["Tickets", "Contacts", "Companies", "Conversations", "Solutions", "Surveys", "Agents"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/freshdesk",
            "notes": "Composio provides Freshdesk toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://developers.freshdesk.com/api/",
                "title": "Freshdesk API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Basic Auth"],
                "excerpt": "Freshdesk provides a RESTful API to integrate helpdesk operations. Authentication is performed via HTTP Basic authentication using an API key."
            }
        ]
    },
    "front": {
        "website": "https://front.com",
        "one_line_description": "Customer communication hub combining shared inboxes with automated workflows.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "JSON Web Token (JWT) API token"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve trial",
            "notes": "7-day free trial allows testing; creating API tokens requires company admin permissions."
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
            "major_resource_areas": ["Conversations", "Messages", "Inboxes", "Channels", "Contacts", "Rules", "Analytics"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/front",
            "notes": "Composio provides Front integration; community MCP servers exist."
        },
        "evidence": [
            {
                "url": "https://dev.frontapp.com/docs",
                "title": "Front Developer Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "Front's Core API is a RESTful interface to manage shared inbox data. Requests require Bearer token authorization using either OAuth or an API token."
            }
        ]
    },
    "pylon": {
        "website": "https://usepylon.com",
        "one_line_description": "B2B support platform built to manage customer issues across Slack, Teams, email, and ticketing.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": True,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Contact-sales gated",
            "notes": "Targeted at B2B high-touch customer support; onboarding typically requires contacting sales or booking a demo."
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
            "major_resource_areas": ["Issues", "Accounts", "Contacts", "Messages", "Webhooks"]
        },
        "mcp": {
            "exists": False,
            "official": False,
            "vendor_supported": False,
            "community": False,
            "composio_support": False,
            "url": None,
            "notes": "No MCP server found; not supported in Composio."
        },
        "evidence": [
            {
                "url": "https://docs.usepylon.com/",
                "title": "Pylon Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "API availability"],
                "excerpt": "Pylon developer API enables programmatic creation and synchronization of customer support issues and accounts via Bearer tokens."
            }
        ]
    },
    "liveagent": {
        "website": "https://liveagent.com",
        "one_line_description": "All-in-one help desk software with live chat, ticketing, and call center capabilities.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "apikey header or Bearer token"
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
            "notes": "14-day free trial allows self-serve generation of API keys in admin panel."
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
            "major_resource_areas": ["Tickets", "Chats", "Calls", "Agents", "Departments", "Contacts", "Canned Messages"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/liveagent",
            "notes": "Composio supports LiveAgent; community MCP connectors available."
        },
        "evidence": [
            {
                "url": "https://api.liveagent.com/docs/v3/",
                "title": "LiveAgent API v3 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Bearer Token"],
                "excerpt": "LiveAgent REST API v3 provides endpoints to manage tickets, agents, and departments. Authenticate via apikey header."
            }
        ]
    },
    "plain": {
        "website": "https://plain.com",
        "one_line_description": "Developer-first customer service platform offering headless support infrastructure via GraphQL API.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
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
            "notes": "Self-serve signup includes free tier with instant API key creation in workspace settings."
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
            "breadth": "Moderate",
            "major_resource_areas": ["Threads", "Customers", "Timeline Entries", "Labels", "Workspaces", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/plain",
            "notes": "Composio supports Plain; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://plain.com/docs",
                "title": "Plain Developer Documentation",
                "source_type": "official_docs",
                "supports": ["GraphQL", "Bearer Token", "API availability"],
                "excerpt": "Plain's API is built on GraphQL and authenticated with Bearer tokens. It lets you create and update customer threads, timeline entries, and events."
            }
        ]
    },
    "help-scout": {
        "website": "https://helpscout.com",
        "one_line_description": "Customer service software platform focused on personalized email and chat support.",
        "authentication": {
            "methods": ["OAuth2"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Client Credentials or Authorization Code flow"
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
            "notes": "15-day free trial provides self-serve OAuth app creation in developer settings."
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
            "major_resource_areas": ["Mailboxes", "Conversations", "Customers", "Tags", "Users", "Workflows", "Reports"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/helpscout",
            "notes": "Composio supports Help Scout; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://developer.helpscout.com/mailbox-api/",
                "title": "Help Scout Mailbox API 2.0",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "Help Scout Mailbox API 2.0 uses OAuth 2.0 to authenticate requests. Both authorization code and client credentials flows are supported."
            }
        ]
    },
    "gorgias": {
        "website": "https://gorgias.com",
        "one_line_description": "E-commerce-focused customer support platform with direct Shopify, BigCommerce, and Magento integrations.",
        "authentication": {
            "methods": ["Basic Auth", "API Key", "OAuth2"],
            "primary_method": "Basic Auth",
            "oauth2": True,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "HTTP Basic Auth using email:api_key"
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
            "notes": "7-day free trial allows self-serve generation of API keys in Settings > REST API."
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
            "major_resource_areas": ["Tickets", "Customers", "Messages", "Macros", "Rules", "Integrations", "Satisfaction Surveys"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/gorgias",
            "notes": "Composio supports Gorgias; community MCP integrations exist."
        },
        "evidence": [
            {
                "url": "https://developers.gorgias.com/reference/introduction",
                "title": "Gorgias API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "API Key"],
                "excerpt": "The Gorgias REST API uses HTTP Basic authentication. Your username is your account email address and your password is your API key."
            }
        ]
    },
    "gladly": {
        "website": "https://gladly.com",
        "one_line_description": "People-centered customer service platform for enterprise retail and consumer brands.",
        "authentication": {
            "methods": ["Basic Auth", "Bearer Token", "API Key"],
            "primary_method": "Basic Auth",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API token with Basic Auth or Bearer token"
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
            "notes": "Enterprise customer service platform requiring sales contract; credentials generated by tenant administrators."
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
            "major_resource_areas": ["Customers", "Conversations", "Topics", "Agents", "Phone Calls", "Tasks"]
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
                "url": "https://developer.gladly.com/",
                "title": "Gladly Developer Portal",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "API availability"],
                "excerpt": "Gladly REST API enables integration with customer profiles and conversations using API tokens issued through the Gladly admin settings."
            },
            {
                "url": "https://www.gladly.com/pricing/",
                "title": "Gladly Enterprise Pricing",
                "source_type": "official_pricing",
                "supports": ["Contact-sales gated", "Paid plan required"],
                "excerpt": "Gladly is priced on an enterprise per-seat model with annual commitments, requiring direct sales consultation."
            }
        ]
    }
}
