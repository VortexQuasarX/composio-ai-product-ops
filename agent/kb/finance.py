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
        "website": "https://www.paygent.co.jp",
        "one_line_description": "Japanese payment service provider (PSP) joint venture between NTT Data and Mitsubishi UFJ NICOS.",
        "authentication": {
            "methods": ["Basic Auth", "API Key", "Other"],
            "primary_method": "Basic Auth",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Client Certificate (mTLS) + Merchant ID / Password"
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
            "notes": "Enterprise payment gateway strictly limited to verified Japanese merchants and financial partners; formal sales onboarding and merchant screening required."
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
            "breadth": "Moderate",
            "major_resource_areas": ["Credit Card Settlement", "Convenience Store Payments", "Bank Transfers", "Recurring Billing", "Refunds"]
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
                "url": "https://www.paygent.co.jp/service/connect/",
                "title": "Paygent Connect Service Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Partner-gated", "Paid plan required"],
                "excerpt": "Paygent Connect provides automated payment processing protocols for e-commerce. Merchant registration, contract signing, and security vetting are required."
            }
        ]
    },
    "ipayx": {
        "website": "https://ipayx.com",
        "one_line_description": "Enterprise electronic bill presentment and payment (EBPP) processing platform for healthcare and municipalities.",
        "authentication": {
            "methods": ["API Key", "Basic Auth"],
            "primary_method": "API Key",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Proprietary merchant token credentials"
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
            "notes": "Specialized municipal and healthcare bill pay portal; developer onboarding is handled strictly through enterprise sales engagement."
        },
        "api": {
            "exists": True,
            "public": False,
            "type": ["REST"],
            "rest": True,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": False,
            "breadth": "Narrow",
            "major_resource_areas": ["Bill Presentment", "Payment Processing", "Reconciliation"]
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
                "url": "https://ipayx.com",
                "title": "iPayX Enterprise Billing",
                "source_type": "official_pricing",
                "supports": ["Contact-sales gated", "Paid plan required"],
                "excerpt": "iPayX provides electronic payment processing tailored for institutions and government entities. Access is negotiated via corporate sales agreements."
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
