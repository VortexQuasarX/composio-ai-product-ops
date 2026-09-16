"""
Knowledge base definitions for ECOMMERCE category (10 apps).
"""

ECOMMERCE_APPS = {
    "shopify": {
        "website": "https://shopify.dev",
        "one_line_description": "Leading global commerce platform powering online stores and retail point-of-sale systems.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Admin API Access Token (shpat_...)"
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
            "notes": "Shopify Partners accounts are free and include unlimited free development stores for building and testing apps."
        },
        "api": {
            "exists": True,
            "public": True,
            "type": ["GraphQL", "REST", "SDK", "CLI", "Webhooks"],
            "rest": True,
            "graphql": True,
            "sdk": True,
            "cli": True,
            "webhooks": True,
            "documentation_available": True,
            "breadth": "Very broad",
            "major_resource_areas": ["Products", "Orders", "Customers", "Inventory", "Fulfillments", "Discounts", "Themes", "Checkout"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/shopify",
            "notes": "Composio provides comprehensive Shopify toolkit; community MCP server implementations exist on GitHub."
        },
        "evidence": [
            {
                "url": "https://shopify.dev/docs/api/admin-rest",
                "title": "Shopify Admin REST API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "GraphQL", "OAuth2"],
                "excerpt": "The Admin API lets developers read and write store data, including products, inventory, and orders, authenticated via OAuth 2.0 or custom app tokens."
            },
            {
                "url": "https://www.shopify.com/partners",
                "title": "Shopify Partner Program",
                "source_type": "official_dev_portal",
                "supports": ["Self-serve free", "Developer account"],
                "excerpt": "Join the Shopify Partner Program for free to create development stores, test APIs, and launch apps in the Shopify App Store."
            }
        ]
    },
    "woocommerce": {
        "website": "https://woocommerce.com/document/woocommerce-rest-api",
        "one_line_description": "Open-source, highly customizable e-commerce platform built natively on WordPress.",
        "authentication": {
            "methods": ["Basic Auth", "API Key"],
            "primary_method": "Basic Auth",
            "oauth2": False,
            "api_key": True,
            "basic_auth": True,
            "bearer_token": False,
            "personal_access_token": False,
            "other": "Consumer Key + Consumer Secret via HTTP Basic Auth or query params"
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
            "notes": "Open-source software; store owners generate API credentials instantly in WordPress WooCommerce settings."
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
            "major_resource_areas": ["Products", "Orders", "Customers", "Coupons", "Reports", "Taxes", "Shipping Zones"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/woocommerce",
            "notes": "Composio provides WooCommerce toolkit; community MCP server available."
        },
        "evidence": [
            {
                "url": "https://woocommerce.github.io/woocommerce-rest-api-docs/",
                "title": "WooCommerce REST API Documentation",
                "source_type": "official_docs",
                "supports": ["REST API", "Basic Auth", "API Key"],
                "excerpt": "The WooCommerce REST API is fully integrated into WooCommerce. Authentication is handled via Consumer Key and Consumer Secret credentials."
            }
        ]
    },
    "bigcommerce": {
        "website": "https://developer.bigcommerce.com",
        "one_line_description": "Open SaaS enterprise e-commerce platform for fast-growing and established brands.",
        "authentication": {
            "methods": ["API Key", "OAuth2"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "X-Auth-Token header"
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
            "notes": "15-day free trial allows self-serve API account creation; partner developer sandboxes available."
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
            "breadth": "Very broad",
            "major_resource_areas": ["Catalog (Products/Categories)", "Orders", "Customers", "Carts", "Checkouts", "Storefront API", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/bigcommerce",
            "notes": "Composio supports BigCommerce; community MCP connectors exist."
        },
        "evidence": [
            {
                "url": "https://developer.bigcommerce.com/docs/start/authentication",
                "title": "BigCommerce API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "API Key"],
                "excerpt": "BigCommerce APIs authenticate via OAuth 2.0 access tokens sent as X-Auth-Token headers with each request."
            }
        ]
    },
    "salesforce-commerce-cloud": {
        "website": "https://developer.salesforce.com/docs/commerce",
        "one_line_description": "Enterprise cloud commerce platform offering unified B2C and B2B digital storefront solutions.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Shopper Login and API Access Service (SLAS) / Account Manager"
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
            "access_classification": "Contact-sales gated",
            "notes": "Enterprise e-commerce platform requiring commercial licensing and realm provisioning via Account Manager."
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
            "major_resource_areas": ["Shopper B2C APIs", "OCAPI (Open Commerce API)", "Product Catalogs", "Basket/Cart", "Orders", "Promotions"]
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
                "url": "https://developer.salesforce.com/docs/commerce/commerce-api/references",
                "title": "Salesforce Commerce API References",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "The Salesforce Commerce API is a RESTful API that enables headless storefronts. Requests require SLAS OAuth tokens and tenant-scoped endpoints."
            }
        ]
    },
    "magento-adobe-commerce": {
        "website": "https://developer.adobe.com/commerce",
        "one_line_description": "Flexible, multi-channel commerce platform available as self-hosted open source and enterprise cloud.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Integration Tokens / Admin Bearer Tokens"
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
            "notes": "Magento Open Source is free and self-hostable with complete REST and GraphQL API access."
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
            "breadth": "Very broad",
            "major_resource_areas": ["Catalog", "Carts", "Orders", "Customers", "Invoices", "Shipments", "Inventory", "GraphQL Storefront"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/magento",
            "notes": "Composio supports Magento; community MCP connectors available on GitHub."
        },
        "evidence": [
            {
                "url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/",
                "title": "Adobe Commerce Web API Authentication",
                "source_type": "official_docs",
                "supports": ["REST API", "GraphQL", "Bearer Token"],
                "excerpt": "Adobe Commerce and Magento Open Source provide REST and GraphQL web APIs authenticated via Bearer tokens or OAuth 1.0a/2.0 integrations."
            }
        ]
    },
    "squarespace": {
        "website": "https://developers.squarespace.com",
        "one_line_description": "Website building and hosting platform with integrated commerce and blogging tools.",
        "authentication": {
            "methods": ["Bearer Token", "OAuth2", "API Key"],
            "primary_method": "Bearer Token",
            "oauth2": True,
            "api_key": True,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "API Key sent as Bearer token in Authorization header"
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
            "notes": "Generating developer API keys requires an active Squarespace Commerce Advanced plan or trial."
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
            "major_resource_areas": ["Orders", "Products", "Inventory", "Transactions", "Profiles", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/squarespace",
            "notes": "Composio supports Squarespace; community MCP integrations exist."
        },
        "evidence": [
            {
                "url": "https://developers.squarespace.com/commerce-apis/overview",
                "title": "Squarespace Commerce APIs Overview",
                "source_type": "official_docs",
                "supports": ["REST API", "Bearer Token", "Paid plan required"],
                "excerpt": "Squarespace Commerce APIs enable integrations with orders and inventory. API key generation requires a Commerce Advanced subscription."
            }
        ]
    },
    "ecwid": {
        "website": "https://api-docs.ecwid.com",
        "one_line_description": "Embeddable e-commerce widget and online store builder by Lightspeed.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "Secret Token / Public Token"
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
            "notes": "Ecwid developer account and store control panel provide free self-serve API access tokens."
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
            "major_resource_areas": ["Products", "Orders", "Customers", "Categories", "Store Profile", "Discounts", "Webhooks"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/ecwid",
            "notes": "Composio supports Ecwid; community MCP connectors available."
        },
        "evidence": [
            {
                "url": "https://api-docs.ecwid.com/reference/overview",
                "title": "Ecwid REST API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Bearer Token"],
                "excerpt": "The Ecwid REST API lets you manage products, orders, and customer data using OAuth 2.0 tokens or secret access tokens."
            }
        ]
    },
    "gumroad": {
        "website": "https://gumroad.com/api",
        "one_line_description": "E-commerce platform for creators to sell digital products, memberships, and courses directly to audiences.",
        "authentication": {
            "methods": ["OAuth2", "Bearer Token", "Personal Access Token"],
            "primary_method": "OAuth2",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": True,
            "other": "Personal Access Token generated in settings"
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
            "notes": "Free to sign up; users can generate personal access tokens directly in Settings > Advanced > Applications."
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
            "breadth": "Moderate",
            "major_resource_areas": ["Products", "Sales", "Subscribers", "Licenses", "Pings (Webhooks)"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/gumroad",
            "notes": "Composio provides Gumroad toolkit; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://gumroad.com/api",
                "title": "Gumroad API Reference",
                "source_type": "official_docs",
                "supports": ["REST API", "OAuth2", "Personal Access Token"],
                "excerpt": "The Gumroad API lets you read and write data on Gumroad. Authenticate using an OAuth2 access token or a personal access token."
            }
        ]
    },
    "amazon-sp-api": {
        "website": "https://developer-docs.amazon.com/sp-api",
        "one_line_description": "Amazon Selling Partner API for third-party sellers and vendors to manage orders, inventory, and listings.",
        "authentication": {
            "methods": ["AWS Signature", "OAuth2", "Bearer Token"],
            "primary_method": "AWS Signature",
            "oauth2": True,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": True,
            "personal_access_token": False,
            "other": "AWS Signature v4 signing + Login with Amazon (LWA) OAuth2 tokens"
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": True,
            "admin_approval_required": True,
            "contact_sales_required": False,
            "partnership_required": True,
            "developer_account_required": True,
            "access_classification": "Partner-gated",
            "notes": "Requires an active Amazon Professional Selling account ($39.99/mo) and submitting a developer registration profile for security approval."
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
            "major_resource_areas": ["Orders", "Fulfillment by Amazon (FBA)", "Catalog Items", "Pricing", "Reports", "Feeds", "Finances", "Notifications"]
        },
        "mcp": {
            "exists": True,
            "official": False,
            "vendor_supported": False,
            "community": True,
            "composio_support": True,
            "url": "https://docs.composio.dev/tools/amazon",
            "notes": "Composio provides Amazon Selling Partner toolkit; community MCP implementations exist."
        },
        "evidence": [
            {
                "url": "https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api",
                "title": "Connecting to the Amazon SP-API",
                "source_type": "official_docs",
                "supports": ["REST API", "AWS Signature", "Partner-gated"],
                "excerpt": "Calls to the Selling Partner API must be authenticated using Login with Amazon (LWA) access tokens and signed with AWS Signature Version 4."
            }
        ]
    },
    "fanbasis": {
        "website": "https://www.fanbasis.com",
        "one_line_description": "Creator economy platform enabling athletes and influencers to sell personalized experiences to fans.",
        "authentication": {
            "methods": ["Unknown"],
            "primary_method": "Unknown",
            "oauth2": False,
            "api_key": False,
            "basic_auth": False,
            "bearer_token": False,
            "personal_access_token": False,
            "other": None
        },
        "credential_access": {
            "self_serve": False,
            "free_access": False,
            "trial_available": False,
            "paid_plan_required": False,
            "admin_approval_required": False,
            "contact_sales_required": False,
            "partnership_required": False,
            "developer_account_required": False,
            "access_classification": "No developer access found",
            "notes": "No public developer portal or API documentation available; consumer and creator marketplace web portal only."
        },
        "api": {
            "exists": False,
            "public": False,
            "type": [],
            "rest": False,
            "graphql": False,
            "sdk": False,
            "cli": False,
            "webhooks": False,
            "documentation_available": False,
            "breadth": "Unknown",
            "major_resource_areas": []
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
                "url": "https://www.fanbasis.com",
                "title": "Fanbasis Official Site",
                "source_type": "official_dev_portal",
                "supports": ["No developer access found"],
                "excerpt": "Fanbasis is a platform connecting fans directly with athletes and creators for VIP experiences. No public developer API is documented."
            }
        ]
    }
}
