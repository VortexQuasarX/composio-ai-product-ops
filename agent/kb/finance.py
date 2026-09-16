"""
Knowledge base definitions for FINANCE AND FINTECH category (10 apps).
"""

FINANCE_APPS = {
    "stripe": {
        "website": "https://stripe.com/docs/api",
        "one_line_description": "Global financial infrastructure platform providing payment processing, billing, and payouts APIs.",
        "authentication": {
            "methods": ["API Key", "Bearer Token"],
            "primary_method": "API Key",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Secret API Keys (sk_test_...) or Restricted API Keys (rk_test_...)"
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
            "notes": "Instant self-serve signup; test mode keys require no KYC or bank account and are 100% free to use."
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
            "major_resource_areas": ["Payment Intents", "Charges", "Customers", "Subscriptions (Billing)", "Invoices", "Refunds", "Payouts", "Connect"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/stripe",
            "notes": "Composio provides extensive Stripe toolkit; community MCP server implementations exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://stripe.com/docs/api/authentication",
                "title": "Stripe API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Bearer Token"],
                "excerpt": "The Stripe API uses API keys to authenticate requests. You can view and manage your API keys in the Stripe Dashboard. Authenticate via Bearer tokens."
            },
            {
                "url": "https://dashboard.stripe.com/register",
                "title": "Stripe Developer Signup",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Developer account"],
                "excerpt": "Create a free Stripe account to immediately access the developer sandbox and generate test API keys."
            }
        ]
    },
    "plaid": {
        "website": "https://plaid.com/docs",
        "one_line_description": "Open banking financial network platform connecting applications to users' bank accounts and transactions.",
        "authentication": {
            "methods": ["API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "PLAID-CLIENT-ID and PLAID-SECRET in HTTP headers or JSON request body"
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
            "notes": "Free Sandbox environment allows instant self-serve testing across simulated banks without payment."
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
            "major_resource_areas": ["Auth (Account Verification)", "Transactions", "Balance", "Identity", "Investments", "Link Tokens", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/plaid",
            "notes": "Composio provides Plaid toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://plaid.com/docs/api/",
                "title": "Plaid API Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Self-serve free"],
                "excerpt": "The Plaid API is a set of REST endpoints. All requests require authentication using your client_id and secret passed in HTTP headers or body."
            }
        ]
    },
    "binance": {
        "website": "https://binance-docs.github.io",
        "one_line_description": "Global cryptocurrency and digital asset exchange platform offering high-frequency trading APIs.",
        "authentication": {
            "methods": ["HMAC", "API Key"],
            "primary_method": "HMAC",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "X-MBX-APIKEY header + HMAC SHA256 signature parameter"
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
            "notes": "API keys are self-serve generated in user account management; Spot Testnet is free to test without KYC."
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
            "major_resource_areas": ["Spot Trading", "Market Data (Order Books/Tickers)", "Wallet / Transfers", "Futures", "WebSocket Streams"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/binance",
            "notes": "Composio provides Binance toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://binance-docs.github.io/apidocs/spot/en/#general-api-information",
                "title": "Binance Spot API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "HMAC", "API Key"],
                "excerpt": "Binance Spot API provides RESTful endpoints. Signed endpoints require sending an X-MBX-APIKEY header and an HMAC SHA256 signature generated with your secret key."
            }
        ]
    },
    "paygent-connect": {
        "website": "https://docs.nmi.com",
        "one_line_description": "NMI-powered white-label payment gateway wrapper providing Direct Post API, Customer Vault tokenization, and multi-processor transaction orchestration.",
        "authentication": {
            "methods": ["API Key", "Other"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "NMI Security Key (passed as query param or header) + Merchant Account ID"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": True,
            "partnership_required": True,
            "developer_account_required": True,
            "access_classification": "Partner-gated",
            "notes": "NMI-powered gateway wrapper requiring merchant underwriting and partner portal onboarding; security keys are generated through administrative merchant control panel."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST", "Webhooks"],
            "rest": True,
            "graphql": False,
            "sdk": True,
            "cli": False,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Customer Vault", "Direct Post / Three-Step Redirect", "QuickClick Payments", "Transaction Query & Reporting", "Recurring Billing"]
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
                "url": "https://docs.nmi.com",
                "title": "NMI Developer Documentation - Gateway APIs",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Partner-gated"],
                "excerpt": "NMI provides Direct Post, Three-Step Redirect, and Customer Vault APIs authenticated via private security keys. Access requires an approved merchant/partner account."
            }
        ]
    },
    "ipayx": {
        "website": "https://www.ipayx.ai",
        "one_line_description": "AI-native foreign exchange (FX) audit engine and protocol providing algorithmic spread analysis and real-time benchmark rate audits.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Bearer API Key header"
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
            "notes": "Self-serve developer signup at ipayx.ai/docs provides instant API key with free tier (10 audits/day); paid tier for high-volume enterprise routing."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Narrow",
            "major_resource_areas": ["audit_transaction", "compare_fx_sources", "spread_calculation", "forensic_reports"]
        },
        "mcp": {
            "exists": True,
            "official": True,
            "vendor_supported": True,
            "community": True,
            "composio_support": False,
            "url": "https://github.com/iPAYX-Technologies/mcp-fx-audit",
            "notes": "Official MCP server repository maintained at iPAYX-Technologies/mcp-fx-audit for autonomous agent FX auditing."
        },
        "evidence": [
            {
                "url": "https://www.ipayx.ai/docs",
                "title": "iPayX Protocol Developer Documentation & MCP Integration",
                "source_type": "official_docs",
                "supports": ["REST API", "API Key", "Self-serve free", "Official MCP"],
                "excerpt": "iPayX provides REST endpoints and an official Model Context Protocol (MCP) server (iPAYX-Technologies/mcp-fx-audit) for AI agents to audit foreign exchange transactions against real-time mid-market rates."
            }
        ]
    },
    "quickbooks": {
        "website": "https://developer.intuit.com",
        "one_line_description": "Accounting and financial management software platform for small businesses and accountants by Intuit.",
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
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Self-serve free",
            "notes": "Intuit Developer Portal is completely free to join and provides free sandbox companies for testing."
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
            "major_resource_areas": ["Invoices", "Customers", "Vendors", "Payments", "Bills", "Accounts", "Reports", "Tax Agencies"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/quickbooks",
            "notes": "Composio provides QuickBooks toolkit; community MCP server implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization",
                "title": "QuickBooks Online Accounting API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Self-serve free"],
                "excerpt": "QuickBooks Online API uses OAuth 2.0 to authenticate and authorize requests. Developers can create free sandbox apps in the Intuit Developer portal."
            }
        ]
    },
    "xero": {
        "website": "https://developer.xero.com",
        "one_line_description": "Cloud-based small business accounting software for invoicing, bank reconciliation, and bookkeeping.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "OAuth 2.0 with PKCE or standard authorization code flow"
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
            "notes": "Xero Developer Portal is free to use and provides a free Demo Company sandbox for API development."
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
            "major_resource_areas": ["Invoices", "Contacts", "Bank Transactions", "Accounts", "Payments", "Manual Journals", "Reports"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/xero",
            "notes": "Composio provides Xero toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://developer.xero.com/documentation/guides/oauth2/overview/",
                "title": "Xero OAuth 2.0 API Guide",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "Xero APIs use OAuth 2.0 for user authentication and authorization. Access tokens must be passed in the HTTP Authorization header as a Bearer token."
            }
        ]
    },
    "brex": {
        "website": "https://developer.brex.com",
        "one_line_description": "Corporate card, spend management, and corporate banking platform for growing businesses.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "User API Token or Team API Token (Bearer)"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Admin-gated",
            "notes": "Requires an active, approved Brex corporate cash/card customer account; API tokens must be created by account administrators."
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
            "major_resource_areas": ["Transactions", "Expenses", "Cards", "Users & Departments", "Budgets", "Webhooks", "Transfers"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/brex",
            "notes": "Composio provides Brex toolkit; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer.brex.com/docs/authentication/",
                "title": "Brex API Authentication Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Admin-gated"],
                "excerpt": "Brex APIs use Bearer token authentication. Account administrators can generate user and team API tokens from the Brex dashboard integrations page."
            }
        ]
    },
    "ramp": {
        "website": "https://docs.ramp.com",
        "one_line_description": "Corporate card, spend automation, and expense management platform designed to control corporate spending.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "OAuth2 Client Credentials or Authorization Code flow"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": True,
            "access_classification": "Admin-gated",
            "notes": "Requires an active, approved Ramp corporate card account; developer app client ID and secret must be generated by company administrators."
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
            "major_resource_areas": ["Transactions", "Cards", "Users", "Departments", "Reimbursements", "Bills", "Vendors", "Limits"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/ramp",
            "notes": "Composio provides Ramp toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://docs.ramp.com/developer-api/authentication",
                "title": "Ramp Developer API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Admin-gated"],
                "excerpt": "The Ramp Developer API uses OAuth 2.0. Account administrators create API applications in company settings to receive client credentials."
            }
        ]
    },
    "pitchbook": {
        "website": "https://pitchbook.com",
        "one_line_description": "Financial market data and research platform providing private equity, venture capital, and M&A intelligence.",
        "authentication": {
            "methods": ["Bearer Token", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": False,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Enterprise API Key / Direct Data Feed credentials"
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
            "notes": "Enterprise financial intelligence; API access is an expensive paid enterprise add-on requiring direct sales contracts."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": True,
            "breadth": "Broad",
            "major_resource_areas": ["Companies", "Deals", "Investors", "Funds", "People", "Valuations", "Direct Data Feeds"]
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
                "url": "https://pitchbook.com/products/data/api-and-crm-integration",
                "title": "PitchBook Direct Data API Overview",
                "source_type": "official_pricing",
                "supports": ["Contact-sales gated", "Paid plan required"],
                "excerpt": "PitchBook API seamlessly delivers comprehensive capital market data directly into client applications and data warehouses via enterprise licensing."
            }
        ]
    }
}
