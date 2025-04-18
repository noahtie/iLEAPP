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
        "output_types": "none",
        "artifact_icon": "settings"
    }
}

from scripts.ilapfuncs import artifact_processor, device_info

@artifact_processor
def hotspotInfo(files_found, report_folder, seeker, wrap_text, timezone_offset):
    data_list = []
    source_path = str(files_found[0])

    hostapd_conf = {}

    with open(source_path, "r") as fp:
        for line in fp:
            line = line.split('=')
            if len(line) == 2:
                key = line[0].strip()
                value = line[1].strip()
                hostapd_conf[key] = value
    
    data_list.append(tuple(hostapd_conf.values()))
    data_headers = tuple(hostapd_conf.keys())

    return data_headers, data_list, source_path