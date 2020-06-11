import logging
import simplejson as json

def export_geojson(geojson_dict, output_path):
    geojson_str = json.dumps(geojson_dict, indent=2, ignore_nan=True)
    with open(output_path, "w") as output_file:
        output_file.write(geojson_str)
    logging.info("exported")
    logging.info(f"Geojson has {len(geojson_dict['features'])} features")