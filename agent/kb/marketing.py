"""
Knowledge base definitions for MARKETING, ADS, EMAIL AND SOCIAL category (10 apps).
"""

MARKETING_APPS = {
    "google-ads": {
        "website": "https://developers.google.com/google-ads",
        "one_line_description": "Online advertising platform by Google for search, display, shopping, and video campaigns.",
        "authentication": {
            "methods": ["OAuth2"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Developer Token header required in addition to OAuth2 token"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": True,
            "developer_account_required": True,
            "access_classification": "Admin-gated",
            "notes": "Test accounts can be accessed freely with a test developer token; Basic and Standard Access require Google developer review and approval."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "gRPC", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Campaigns", "Ad Groups", "Ads", "Keywords", "Bidding Strategies", "Reporting", "Audiences"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/google-ads",
            "notes": "Composio provides Google Ads toolkit; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://developers.google.com/google-ads/api/docs/first-call/overview",
                "title": "Google Ads API Quickstart",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Admin-gated"],
                "excerpt": "To make calls to the Google Ads API, you need OAuth 2.0 credentials and an approved developer token linked to a manager account."
            }
        ]
    },
    "meta-ads": {
        "website": "https://developers.facebook.com/docs/marketing-apis",
        "one_line_description": "Digital advertising platform across Facebook, Instagram, Messenger, and Meta Audience Network.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Meta Graph API User/System Access Token"
        },
        "credential_access": {
            "self_serve": True,
            "free_access": False,
            "trial_available": True,
            "paid_plan_required": False,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Admin-gated",
            "notes": "Development mode allows self-serve sandbox ad account testing; live production ads management requires Meta App Review and Business Verification."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Ad Accounts", "Campaigns", "Ad Sets", "Creatives", "Custom Audiences", "Insights/Reporting", "Pixel"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/facebook-ads",
            "notes": "Composio supports Meta Marketing API; community MCP servers exist."
        },
        "evidence": [
            {
                "url": "https://developers.facebook.com/docs/marketing-apis/overview",
                "title": "Meta Marketing API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Admin-gated"],
                "excerpt": "The Marketing API is an HTTP-based RESTful API that enables businesses to manage ad accounts, create campaigns, and track conversion insights using OAuth access tokens."
            }
        ]
    },
    "linkedin-ads": {
        "website": "https://learn.microsoft.com/linkedin/marketing",
        "one_line_description": "B2B professional audience advertising and lead generation network by LinkedIn.",
        "authentication": {
            "methods": ["OAuth2"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": None
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": False,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": True,
            "developer_account_required": True,
            "access_classification": "Partner-gated",
            "notes": "Access to LinkedIn Marketing Developer Platform APIs requires applying for developer program approval."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Ad Accounts", "Campaigns", "Creatives", "Lead Gen Forms", "Analytics", "Audience Segments"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/linkedin",
            "notes": "Composio supports LinkedIn marketing actions; community MCP servers available."
        },
        "evidence": [
            {
                "url": "https://learn.microsoft.com/en-us/linkedin/marketing/overview",
                "title": "LinkedIn Marketing Developer Platform Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Partner-gated"],
                "excerpt": "The Marketing Developer Platform enables enterprise partners to build integrations with LinkedIn Ad campaigns. Applications must be reviewed and approved for access."
            }
        ]
    },
    "gohighlevel": {
        "website": "https://highlevel.stoplight.io",
        "one_line_description": "All-in-one sales and marketing automation platform for agencies and small businesses.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token", "API Key"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Location API Key / Company Private Key"
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
            "access_classification": "Self-serve paid",
            "notes": "HighLevel requires an active paid agency subscription ($97-$297/month) to access marketplace and API tokens; 14-day trial offered."
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
            "major_resource_areas": ["Contacts", "Opportunities", "Calendars", "Conversations", "Locations", "Pipelines", "Custom Fields"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/gohighlevel",
            "notes": "Composio provides GoHighLevel integration; community MCP connectors exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://highlevel.stoplight.io/docs/integrations/",
                "title": "HighLevel API v2 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "HighLevel API 2.0 utilizes OAuth 2.0 authentication to securely access sub-account locations, contacts, and marketing funnels."
            }
        ]
    },
    "mailchimp": {
        "website": "https://mailchimp.com/developer",
        "one_line_description": "Email marketing automation and audience engagement platform by Intuit.",
        "authentication": {
            "methods": ["API Key", "OAuth2"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "API Key includes data center prefix (e.g. key-us1)"
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
            "notes": "Mailchimp free tier allows self-serve generation of API keys in Account > Extras > API keys."
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
            "major_resource_areas": ["Audiences (Lists)", "Members (Subscribers)", "Campaigns", "Automations", "Reports", "Templates", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/mailchimp",
            "notes": "Composio provides Mailchimp toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://mailchimp.com/developer/marketing/docs/fundamentals/",
                "title": "Mailchimp Marketing API Fundamentals",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "OAuth2"],
                "excerpt": "The Mailchimp Marketing API provides programmatic access to Mailchimp data and functionality. You can authenticate using an API key or OAuth 2."
            }
        ]
    },
    "klaviyo": {
        "website": "https://developers.klaviyo.com",
        "one_line_description": "Intelligent marketing automation platform specialized in e-commerce email and SMS flows.",
        "authentication": {
            "methods": ["API Key", "OAuth2"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Private API Key header: Authorization: Klaviyo-API-Key pk_..."
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
            "notes": "Free tier enables instant self-serve API key creation in Settings > API Keys."
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
            "major_resource_areas": ["Profiles", "Metrics", "Events", "Campaigns", "Flows", "Segments", "Templates", "Tags"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/klaviyo",
            "notes": "Composio provides Klaviyo toolkit; community MCP integrations exist."
        },
        "evidence": [
            {
                "url": "https://developers.klaviyo.com/en/docs/api_overview",
                "title": "Klaviyo API Documentation Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "OAuth2"],
                "excerpt": "The Klaviyo API follows RESTful principles with versioned endpoints. Authenticate using private API keys via the Klaviyo-API-Key header or OAuth 2.0."
            }
        ]
    },
    "systeme-io": {
        "website": "https://systeme.io",
        "one_line_description": "All-in-one marketing platform for online businesses offering sales funnels, email marketing, and course hosting.",
        "authentication": {
            "methods": ["API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "X-API-Key header"
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
            "notes": "Systeme.io offers a generous free-forever plan that includes API key generation in account settings."
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
            "major_resource_areas": ["Contacts", "Tags", "Courses", "Funnels", "Payments", "Webhooks"]
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
                "url": "https://systeme.io/api-documentation",
                "title": "Systeme.io Public API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Self-serve free"],
                "excerpt": "The systeme.io REST API provides endpoints to manage contacts, tags, and subscriptions. Authenticate by providing your X-API-Key in HTTP headers."
            }
        ]
    },
    "pinterest": {
        "website": "https://developers.pinterest.com",
        "one_line_description": "Visual discovery and bookmarking engine with programmatic advertising and shopping pins.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
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
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Admin-gated",
            "notes": "Trial access allows immediate self-serve sandbox API testing; standard commercial access requires app review and approval."
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
            "major_resource_areas": ["Pins", "Boards", "Ad Accounts", "Campaigns", "Audiences", "Product Catalogs", "Analytics"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/pinterest",
            "notes": "Composio provides Pinterest toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://developers.pinterest.com/docs/api/v5/",
                "title": "Pinterest API v5 Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "The Pinterest API v5 allows developers to manage organic and advertising resources via REST endpoints authenticated with OAuth 2.0 Bearer tokens."
            }
        ]
    },
    "threads": {
        "website": "https://developers.facebook.com/docs/threads",
        "one_line_description": "Text-based social sharing platform by Instagram/Meta for public conversations.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Threads User Access Token"
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
            "notes": "Meta for Developers enables self-serve app creation and token generation for Threads accounts."
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
            "major_resource_areas": ["Posts (Threads)", "Media Containers", "Replies", "Insights", "User Profile"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/threads",
            "notes": "Composio supports Threads API; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://developers.facebook.com/docs/threads/overview",
                "title": "Threads API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Self-serve free"],
                "excerpt": "The Threads API allows developers to publish posts, retrieve insights, and manage replies on Threads using OAuth 2.0 authentication."
            }
        ]
    },
    "sendgrid": {
        "website": "https://sendgrid.com",
        "one_line_description": "Cloud-based customer communication platform for transactional and marketing email delivery.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Authorization: Bearer <API_KEY>"
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
            "notes": "Free tier permits sending up to 100 emails/day forever with instant self-serve API key generation."
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
            "major_resource_areas": ["Mail Send", "Marketing Campaigns", "Contacts", "Templates", "Suppression Lists", "Stats", "Event Webhook"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/sendgrid",
            "notes": "Composio supports SendGrid; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://docs.sendgrid.com/api-reference",
                "title": "Twilio SendGrid API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Bearer Token"],
                "excerpt": "The SendGrid v3 API is a RESTful API. Authenticate requests by sending your API key as a Bearer token in the Authorization header."
            }
        ]
    }
}
