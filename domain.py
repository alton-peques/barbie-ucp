"""Domain configuration — this file IS the retargeting surface.

Everything that makes this deployment a collector-Barbie finder (DollScout)
instead of, say, a vinyl or trading-card finder lives here. To point Magpie at
your own hobby, edit this file plus the fenced BRAND blocks in index.html —
see RETARGETING.md for the full checklist. The engine (app.py) never needs
to change.
"""

# --- Site identity ---------------------------------------------------------

# Shown in the startup banner; the visible wordmark lives in index.html.
SITE_NAME = "DollScout"

# Canonical public origin (used for robots/sitemap + host redirects).
SITE_ORIGIN = "https://www.dollscout.com"
# Non-canonical public hostnames that 301 to SITE_ORIGIN (host-gated so Fly
# health checks / direct-IP hits, which use other Host values, pass through).
REDIRECT_HOSTS = {"dollscout.fly.dev", "dollscout.com"}

# --- Search shaping ---------------------------------------------------------

# The UCP global catalog is all-of-ecommerce; without an explicit anchor a
# query like "Ken doll" or "1990s" drifts into generic/baby dolls. The anchor
# is quietly prepended to any query that doesn't already contain it.
QUERY_ANCHOR = "Barbie"

# What an empty search box searches for.
DEFAULT_QUERY = "Barbie collector doll"

# Passed as UCP context.intent on every search (chips get appended).
SEARCH_INTENT = "Barbie collector shopping"

# Relevance guard: keep a result only if its title or description names the
# brand. Distinct from QUERY_ANCHOR — the anchor keeps the *query* on-topic,
# these keep the *results* on-topic.
BRAND_TERMS = ("barbie", "mattel")

# Merchant ban list: results from these sellers are hidden everywhere (search +
# quick-view). Each entry is a lowercase substring matched against the seller's
# myshopify domain, its custom-domain host, and its name — so "sell4value"
# catches sell4value.com, sell4value.myshopify.com, and the "SELL4VALUE"
# display name. Curate per deployment; empty tuple disables the filter.
BANNED_SELLERS = ("sell4value",)

# Popular searches surfaced as indexable deep-links (/?q=...) so Google can
# crawl them. Also pre-warmed into the search cache at boot.
POPULAR_QUERIES = [
    "Holiday Barbie", "Bob Mackie Barbie", "Silkstone Barbie", "Barbie Signature",
    "NRFB Barbie", "Dolls of the World Barbie", "Byron Lars Barbie", "OOAK Barbie",
    "Barbie Looks", "Birthday Wishes Barbie",
]

# --- SEO meta for /?q= deep-links -------------------------------------------

# .format(q=...) templates for query-specific <title>/description injection.
DEEP_LINK_TITLE = "{q} — Barbie dolls on DollScout"
DEEP_LINK_DESC = ("Find {q} collector Barbie dolls across thousands of independent Shopify shops "
                  "in one search on DollScout.")

# COUPLING TRAP: this must EXACTLY match the og:title / twitter:title content
# attribute in index.html — render_index() find-and-replaces that literal string
# to inject per-query social meta. If they drift apart, deep-link og:title
# silently stops updating. (RETARGETING.md step 3.)
DEFAULT_META_TITLE = "DollScout — The Unofficial Collector Barbie Finder"

# --- Barbie World (/world) ---------------------------------------------------

# Config for the immersive 3D map at /world: a navigable low-poly town where
# every doll in the catalog stands as a figure in a themed district. Each
# area's ``q`` runs through the exact same /api/search pipeline (query anchor
# + brand relevance guard), so the dolls that populate a district genuinely
# match its theme. ``style`` picks that district's 3D landmark/decor set in
# world.html; ``x``/``z``/``r`` place it on the island (world units, plaza at
# origin); ``ground``/``accent``/``palette`` drive terrain + building colors.
WORLD_NAME = "Barbie World"
WORLD_TAGLINE = ("The catalog, rendered — every doll a figure in a town you can "
                 "explore. Descend to discover.")
WORLD_AREAS = [
    {
        "id": "dreamhouse-heights", "name": "Dreamhouse Heights", "emoji": "🏰",
        "tagline": "Barbie Signature on the hill",
        "q": "Barbie Signature collector doll",
        "style": "dreamhouse", "x": 0, "z": -470, "r": 205,
        "ground": "#f7a8cd", "accent": "#e0218a",
        "palette": ["#ff7fb8", "#ffa1c9", "#ffc2dc", "#f06aa8", "#ffd9e9"],
    },
    {
        "id": "holiday-village", "name": "Holiday Village", "emoji": "🎄",
        "tagline": "Holiday Barbie, every year of her",
        "q": "Holiday Barbie",
        "style": "holiday", "x": 385, "z": -350, "r": 190,
        "ground": "#eef6fb", "accent": "#2b7bb9",
        "palette": ["#d9534f", "#3d7d4f", "#f2f7fa", "#c8dff0", "#e8b04b"],
    },
    {
        "id": "world-tour-harbor", "name": "World Tour Harbor", "emoji": "🌍",
        "tagline": "Dolls of the World at the docks",
        "q": "Dolls of the World Barbie",
        "style": "harbor", "x": 545, "z": 40, "r": 185,
        "ground": "#bfe3d8", "accent": "#17766d",
        "palette": ["#2e8f86", "#54b0a5", "#e7d9a8", "#c96f4a", "#7fc8bd"],
    },
    {
        "id": "birthday-park", "name": "Birthday Park", "emoji": "🎈",
        "tagline": "Birthday Wishes under the balloons",
        "q": "Birthday Wishes Barbie",
        "style": "park", "x": 380, "z": 380, "r": 185,
        "ground": "#cdebb4", "accent": "#3f8f2f",
        "palette": ["#ffd166", "#ef767a", "#7bc47f", "#f9a03f", "#b5e2fa"],
    },
    {
        "id": "designer-row", "name": "Designer Row", "emoji": "✨",
        "tagline": "Bob Mackie glamour, gowns & gold",
        "q": "Bob Mackie Barbie",
        "style": "designer", "x": 0, "z": 500, "r": 195,
        "ground": "#f4dfae", "accent": "#8a6a12",
        "palette": ["#caa84a", "#e6c877", "#8d6b1f", "#f3e3b5", "#b28f34"],
    },
    {
        "id": "silkstone-salon", "name": "Silkstone Salon", "emoji": "💄",
        "tagline": "The Fashion Model Collection quarter",
        "q": "Silkstone Fashion Model Collection Barbie",
        "style": "silkstone", "x": -385, "z": 375, "r": 185,
        "ground": "#e6d4ee", "accent": "#7a4b9d",
        "palette": ["#3a3140", "#f5eef8", "#a583bd", "#d0b7de", "#63527a"],
    },
    {
        "id": "malibu-beach", "name": "Malibu Beach", "emoji": "🌴",
        "tagline": "Sun, surf & vintage Malibu",
        "q": "Malibu Barbie beach",
        "style": "beach", "x": -560, "z": 25, "r": 180,
        "ground": "#fbe6ad", "accent": "#0f7ea8",
        "palette": ["#ffb45e", "#5ec8dd", "#fff0c6", "#ff8b6a", "#79d0c1"],
    },
    {
        "id": "vintage-quarter", "name": "Vintage Quarter", "emoji": "📻",
        "tagline": "1959 & the swinging decades",
        "q": "vintage 1960s Barbie",
        "style": "vintage", "x": -390, "z": -350, "r": 190,
        "ground": "#ecd9b0", "accent": "#a05f18",
        "palette": ["#d8a24a", "#b7743a", "#e9d3a0", "#8f5b2c", "#f0e2c0"],
    },
]

# --- Chip taxonomy -----------------------------------------------------------

# Authored public-knowledge taxonomy of Barbie collecting terms: common Barbie
# line/designer/era names used purely as search sharpeners against the UCP
# global catalog. Each chip's ``q`` value is appended to the shopper's query.
# Insertion order is preserved (Python 3.7+ dicts) and drives display order.
TAXONOMY = {
    "Decade": [
        {"label": "1959–60s", "q": "vintage 1960s"},
        {"label": "1970s", "q": "1970s vintage"},
        {"label": "1980s", "q": "1980s"},
        {"label": "1990s", "q": "1990s"},
        {"label": "2000s", "q": "2000s"},
        {"label": "2010s", "q": "2010s"},
        {"label": "2020s", "q": "2020s"},
    ],
    "Line / Series": [
        {"label": "Barbie Signature", "q": "Barbie Signature"},
        {"label": "Silkstone / Fashion Model", "q": "Silkstone Fashion Model Collection"},
        {"label": "Holiday Barbie", "q": "Holiday Barbie"},
        {"label": "Birthday Wishes", "q": "Birthday Wishes"},
        {"label": "Dolls of the World", "q": "Dolls of the World"},
        {"label": "Barbie Looks", "q": "Barbie Looks"},
    ],
    "Designer": [
        {"label": "Bob Mackie", "q": "Bob Mackie"},
        {"label": "Byron Lars", "q": "Byron Lars"},
        {"label": "Robert Best", "q": "Robert Best"},
        {"label": "Carlyle Nuera", "q": "Carlyle Nuera"},
    ],
    "Type": [
        {"label": "Collector", "q": "collector"},
        {"label": "Playline", "q": "playline"},
        {"label": "OOAK", "q": "OOAK one of a kind"},
        {"label": "NRFB", "q": "NRFB new in box"},
    ],
}
