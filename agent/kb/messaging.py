"""
Knowledge base definitions for COMMUNICATIONS AND MESSAGING category (10 apps).
"""

MESSAGING_APPS = {
    "slack": {
        "website": "https://api.slack.com",
        "one_line_description": "Cloud-based team messaging and workplace collaboration platform with extensive app integrations.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Bot Token (xoxb-) and User Token (xoxp-)"
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
            "notes": "Creating Slack apps and bot tokens via api.slack.com is completely free and self-serve."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "SDK", "Webhooks", "CLI"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Chat (Messages)", "Conversations (Channels)", "Users", "Files", "Reactions", "Views (Modals)", "Workflows"]
        },
        "mcp": {
            "exists": True,
            "official": True,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/slack",
            "notes": "Official reference MCP server maintained by Model Context Protocol core; Composio provides Slack toolkit."
        },
        "evidence": [
            {
                "url": "https://api.slack.com/web",
                "title": "Slack Web API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "The Slack Web API allows apps to interact with Slack workspaces using standard HTTP methods and JSON responses authenticated via Bearer tokens."
            },
            {
                "url": "https://api.slack.com/apps",
                "title": "Slack Your Apps Management Portal",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Developer account"],
                "excerpt": "Anyone with a Slack account can create an app for free, configure bot scopes, and install it to development workspaces."
            }
        ]
    },
    "twilio": {
        "website": "https://twilio.com",
        "one_line_description": "Cloud communications platform providing APIs for programmable SMS, voice calls, WhatsApp, and video.",
        "authentication": {
            "methods": ["Basic Auth", "API Key", "Bearer Token"],
            "primary_method": "Basic Auth",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Account SID + Auth Token or API Key + Secret"
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
            "notes": "Free trial credit provided upon phone verification; pay-as-you-go billing required for production."
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
            "major_resource_areas": ["Programmable Messaging (SMS/MMS)", "Voice", "Verify", "Phone Numbers", "Conversations", "Serverless Functions"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/twilio",
            "notes": "Composio provides comprehensive Twilio toolkit; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://www.twilio.com/docs/usage/api",
                "title": "Twilio REST API Basics",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "API Key"],
                "excerpt": "Twilio's APIs are RESTful. HTTP requests require HTTP Basic authentication using your Twilio Account SID and Auth Token."
            }
        ]
    },
    "zoho-cliq": {
        "website": "https://zoho.com/cliq",
        "one_line_description": "Enterprise chat software for team collaboration, audio/video calls, and task coordination.",
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
            "notes": "Zoho Cliq free plan covers up to 100 users with full access to the Zoho Developer Console."
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
            "major_resource_areas": ["Channels", "Messages", "Bots", "Commands", "Forms", "Users"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/zoho",
            "notes": "Composio supports Zoho Cliq actions; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://www.zoho.com/cliq/help/restapi/v2/",
                "title": "Zoho Cliq API v2 Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API availability"],
                "excerpt": "Zoho Cliq REST API v2 enables external applications to interact with channels and post messages using OAuth 2.0 tokens."
            }
        ]
    },
    "lark": {
        "website": "https://open.larksuite.com",
        "one_line_description": "All-in-one enterprise collaboration suite combining messaging, video conferencing, docs, and calendar.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Tenant Access Token / User Access Token"
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
            "notes": "Lark Open Platform allows free self-serve app creation and API testing."
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
            "major_resource_areas": ["IM (Messaging)", "Calendar", "Docs (Bitable/Base)", "Video Conference", "Contact (Directory)", "Approval"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://open.larksuite.com/document/home/index",
            "notes": "Composio supports Larksuite; community MCP servers available on GitHub."
        },
        "evidence": [
            {
                "url": "https://open.larksuite.com/document/home/index",
                "title": "Lark Open Platform Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "Lark Open Platform offers open REST APIs and event subscriptions across IM, calendar, and collaborative docs using tenant access tokens."
            }
        ]
    },
    "pumble": {
        "website": "https://pumble.com",
        "one_line_description": "Team messaging and workspace chat tool with voice calls and file sharing by Cake.com.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Bot Token / Webhook URL"
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
            "notes": "Free tier includes incoming webhooks and bot integration creation."
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
            "major_resource_areas": ["Messages", "Channels", "Users", "Incoming Webhooks"]
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
                "url": "https://pumble.com/help/integrations/incoming-webhooks/",
                "title": "Pumble Incoming Webhooks and API",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Webhooks"],
                "excerpt": "Pumble allows developers to post automated messages into channels via incoming webhook URLs and REST endpoints."
            }
        ]
    },
    "discord": {
        "website": "https://discord.com",
        "one_line_description": "Voice, video, and text communication service for gaming, creator communities, and developer teams.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Bot Token (Authorization: Bot <token>)"
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
            "notes": "Discord Developer Portal is 100% free with instant self-serve bot creation and token generation."
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
            "major_resource_areas": ["Channels", "Messages", "Guilds (Servers)", "Users", "Webhooks", "Interactions (Slash Commands)"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/discord",
            "notes": "Composio provides Discord toolkit; community MCP server implementations exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://discord.com/developers/docs/intro",
                "title": "Discord Developer Portal Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "OAuth2"],
                "excerpt": "Discord provides a rich REST API and real-time Gateway for building bots, applications, and webhooks authenticated with bot tokens."
            }
        ]
    },
    "telegram": {
        "website": "https://core.telegram.org",
        "one_line_description": "Cloud-based mobile and desktop messaging app with privacy focus and open bot ecosystem.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Bot Token embedded in URL: /bot<token>/"
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
            "notes": "Instant free bot creation via @BotFather chat; no credit card or account approval needed."
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
            "major_resource_areas": ["Messages", "Chats", "Updates", "Inline Queries", "Payments", "Stickers", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/telegram",
            "notes": "Composio provides Telegram bot toolkit; community MCP connectors exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://core.telegram.org/bots/api",
                "title": "Telegram Bot API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Self-serve free"],
                "excerpt": "The Bot API is an HTTP-based interface created for developers to build bots for Telegram. Bots can be created freely using @BotFather."
            }
        ]
    },
    "whatsapp-business": {
        "website": "https://developers.facebook.com/docs/whatsapp",
        "one_line_description": "Enterprise customer messaging solution for businesses to communicate directly via WhatsApp.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Meta Graph API System User Access Token"
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
            "access_classification": "Admin-gated",
            "notes": "Requires Meta Business Manager account, business verification, and phone number registration; per-conversation fees apply."
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
            "major_resource_areas": ["Messages", "Message Templates", "Phone Numbers", "Media", "Webhooks", "Business Profiles"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/whatsapp",
            "notes": "Composio supports WhatsApp Business Cloud API; community MCP servers exist."
        },
        "evidence": [
            {
                "url": "https://developers.facebook.com/docs/whatsapp/cloud-api/overview",
                "title": "WhatsApp Business Cloud API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Admin-gated"],
                "excerpt": "The Cloud API allows medium and large businesses to communicate with customers at scale through Meta's cloud servers, authenticated via System User access tokens."
            }
        ]
    },
    "aircall": {
        "website": "https://aircall.io",
        "one_line_description": "Cloud call center and phone system software designed for customer support and sales teams.",
        "authentication": {
            "methods": ["Basic Auth", "Bearer Token", "API Key"],
            "primary_method": "Basic Auth",
            "oauth2": True,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API ID + API Token in Basic Auth or Bearer token"
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
            "notes": "7-day trial available; generating API keys requires company admin access in dashboard."
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
            "major_resource_areas": ["Calls", "Numbers", "Users", "Contacts", "Tags", "Webhooks", "Insights"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/aircall",
            "notes": "Composio supports Aircall; community MCP connectors available."
        },
        "evidence": [
            {
                "url": "https://developer.aircall.io/api-references/",
                "title": "Aircall Public API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "API Key"],
                "excerpt": "Aircall API is organized around REST. All requests require authentication using your API ID and API token sent as HTTP Basic Auth credentials."
            }
        ]
    },
    "vonage": {
        "website": "https://developer.vonage.com",
        "one_line_description": "Communications API platform (formerly Nexmo) for SMS, voice, video, and conversational messaging.",
        "authentication": {
            "methods": ["API Key", "Bearer Token", "JWT"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API Key + Secret query/body params, or JWT signed by private key"
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
            "notes": "Free trial credit (€2) granted upon signup; pay-per-use billing for messages and voice minutes."
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
            "major_resource_areas": ["SMS", "Voice", "Messages API", "Verify", "Video", "Number Insight", "SIP Trunking"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/vonage",
            "notes": "Composio supports Vonage; community MCP integrations exist."
        },
        "evidence": [
            {
                "url": "https://developer.vonage.com/en/getting-started/concepts/authentication",
                "title": "Vonage API Authentication Guide",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "JWT"],
                "excerpt": "Vonage APIs support two main authentication mechanisms: API Key/Secret for legacy APIs, and Application IDs with JSON Web Tokens (JWT) signed by a private key for modern APIs."
            }
        ]
    }
}
