from typing import Dict


class AzureLocations:
    locations: Dict[str, str] = {
        # North America
        "canadacentral": "cac",
        "canadaeast": "cae",
        "centralus": "uc",
        "eastus": "ue",
        "eastus2": "ue2",
        "northcentralus": "unc",
        "southcentralus": "usc",
        "westus": "uw",
        "westus2": "uw2",
        "westus3": "uw3",
        "westcentralus": "uwc",
        # Latin America
        "brazilsouth": "brs",
        "brazilsoutheast": "brse",
        "brazilus": "brus",
        # Europe
        "northeurope": "en",
        "westeurope": "ew",
        "swedencentral": "swc",
        "uksouth": "uks",
        "ukwest": "ukw",
        "francecentral": "frc",
        "francesouth": "frs",
        "germanywestcentral": "gwc",
        "germanynorth": "den",
        "norwayeast": "noe",
        "norwaywest": "now",
        "polandcentral": "plc",
        "switzerlandnorth": "swn",
        "switzerlandwest": "chw",
        # Asia-Pacific
        "australiacentral": "auc",
        "australiacentral2": "auc2",
        "australiaeast": "aue",
        "australiasoutheast": "ause",
        "eastasia": "eas",
        "japaneast": "jae",
        "japanwest": "jpw",
        "koreacentral": "koc",
        "koreasouth": "krs",
        "southeastasia": "sea",
        "southindia": "sin",
        "westindia": "wi",
        "jioindiacentral": "jic",
        "jioindiawest": "jiw",
        "centralindia": "cin",
        # Middle East and Africa
        "uaenorth": "uan",
        "uaecentral": "uac",
        "southafricanorth": "san",
        "southafricawest": "saw",
        "qatarcentral": "qtc",
        # Global and Generic
        "asia": "as",
        "asiapacific": "ap",
        "australia": "au",
        "brazil": "br",
        "canada": "ca",
        "europe": "eu",
        "france": "fr",
        "germany": "de",
        "global": "gl",
        "india": "in",
        "japan": "jp",
        "korea": "kr",
        "norway": "no",
        "singapore": "sg",
        "southafrica": "za",
        "switzerland": "ch",
        "uae": "ae",
        "uk": "uk",
        "unitedstates": "us",
        "unitedstateseuap": "use",
        # Scenarios and Staging
        "centraluseuap": "uce",
        "eastus2euap": "ue2e",
        "eastusstg": "uestg",
        "centralusstage": "ucs",
        "eastusstage": "ues",
        "eastus2stage": "ue2s",
        "northcentralusstage": "uncs",
        "southcentralusstage": "uscs",
        "westusstage": "uws",
        "westus2stage": "uw2s",
        "eastasiastage": "eass",
        "southeastasiastage": "seas",
        "southcentralusstg": "uscstg",
    }
