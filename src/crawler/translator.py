class TranslationDict:
    _instance = None
    translated_keywords = {
        "en": ["finance", "financial", "financial report"],
        "fr": ["finance", "financier", "rapport financier"],
        "de": ["Finanzen", "finanziell", "Finanzbericht"],
        "it": ["finanza", "finanziario", "rapporto finanziario"],
        "es": ["finanzas", "financiero", "informe financiero"],
        "nl": ["financiën", "financieel", "financieel verslag"],
        "ru": ["финансы", "финансовый", "финансовый отчет"],
        "pl": ["finanse", "finansowy", "raport finansowy"],
        "ro": ["finanțe", "financiar", "raport financiar"],
        "el": ["χρηματοοικονομικά", "οικονομικός", "οικονομική έκθεση"],
        "hu": ["pénzügy", "pénzügyi", "pénzügyi jelentés"],
        "sv": ["finans", "finansiell", "finansiell rapport"],
        "pt": ["finanças", "financeiro", "relatório financeiro"],
        "da": ["finans", "finansiel", "finansiel rapport"],
        "fi": ["rahoitus", "rahoitusala", "talousraportti"],
        "sk": ["financie", "finančný", "finančná správa"],
        "sl": ["finance", "finančni", "finančno poročilo"],
        "lt": ["finansai", "finansinis", "finansinė ataskaita"],
        "lv": ["finanses", "finansiāls", "finanšu pārskats"],
        "et": ["rahandus", "finants", "finantsaruanne"]
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TranslationDict, cls).__new__(cls)
        return cls._instance
