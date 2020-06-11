from definitions import PATH_INPUT_CSV, PATH_OUTPUT_GEOJSON
from modules.geojson.df_to_geojson import df_to_geojson
from modules.geojson.export_geojson import export_geojson
from modules.init.init_program import init_program
import pandas as pd

def main():

    # init
    init_program()

    # actions to perform...
    df = pd.read_csv(PATH_INPUT_CSV)
    cols = ["provnum","name","address","city","state","zip","county","bedcert","ownership","employee_cases",
            "resident_cases", "resident_deaths","cna_hprd",'lpn_hprd',"rn_hprd","total_hprd"]
    geojson_dict = df_to_geojson(df, cols, lon="google_long", lat="google_lat")
    export_geojson(geojson_dict, PATH_OUTPUT_GEOJSON)




if __name__ == '__main__':
    main()