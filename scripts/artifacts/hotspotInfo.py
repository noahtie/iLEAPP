__artifacts_v2__ = {
    "hotspotInfo": {
        "name": "HotSpot Info",
        "description": "Extract HotSpot Info",
        "author": "@NoahTie",
        "creation_date": "2025-04-18",
        "last_update_date": "2025-04-18",
        "requirements": "none",
        "category": "Identifiers",
        "notes": "",
        "paths": ('*/hostapd.conf'),
        "output_types": ["html", "tsv"],
        "artifact_icon": "save"
    }
}

from scripts.ilapfuncs import artifact_processor, device_info

@artifact_processor
def hotspotInfo(files_found, report_folder, seeker, wrap_text, timezone_offset):
    source_path = str(files_found[0])

    hostapd_conf = {}

    with open(source_path, "r") as fp:
        for line in fp:
            line = line.split('=')
            if len(line) == 2:
                key = line[0].strip()
                value = line[1].strip()
                hostapd_conf[key] = value
    
    data_list = list(hostapd_conf.items())
    data_headers = ('Property', 'Property Value')

    return data_headers, data_list, source_path