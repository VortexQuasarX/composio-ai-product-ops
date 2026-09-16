"""
Unified knowledge base aggregator for all 100 applications across 10 categories.
"""

from typing import Dict, Any

from agent.kb.crm import CRM_APPS
from agent.kb.support import SUPPORT_APPS
from agent.kb.messaging import MESSAGING_APPS
from agent.kb.marketing import MARKETING_APPS
from agent.kb.ecommerce import ECOMMERCE_APPS
from agent.kb.data_seo import DATA_SEO_APPS
from agent.kb.developer import DEVELOPER_APPS
from agent.kb.productivity import PRODUCTIVITY_APPS
from agent.kb.finance import FINANCE_APPS
from agent.kb.ai_media import AI_MEDIA_APPS

ALL_APPS_KB: Dict[str, Dict[str, Any]] = {}
ALL_APPS_KB.update(CRM_APPS)
ALL_APPS_KB.update(SUPPORT_APPS)
ALL_APPS_KB.update(MESSAGING_APPS)
ALL_APPS_KB.update(MARKETING_APPS)
ALL_APPS_KB.update(ECOMMERCE_APPS)
ALL_APPS_KB.update(DATA_SEO_APPS)
ALL_APPS_KB.update(DEVELOPER_APPS)
ALL_APPS_KB.update(PRODUCTIVITY_APPS)
ALL_APPS_KB.update(FINANCE_APPS)
ALL_APPS_KB.update(AI_MEDIA_APPS)


def get_app_knowledge(app_id: str) -> Dict[str, Any]:
    """Retrieves verified knowledge base entry for an application ID."""
    if app_id in ALL_APPS_KB:
        return ALL_APPS_KB[app_id]
    raise KeyError(f"Application ID '{app_id}' not found in knowledge base.")


def get_all_app_ids() -> list:
    """Returns list of all 100 app IDs in the knowledge base."""
    return list(ALL_APPS_KB.keys())
