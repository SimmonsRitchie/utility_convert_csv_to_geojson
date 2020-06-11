def df_to_geojson(df, properties, lat="latitude", lon="longitude"):

    """
    Takes dataframe and returns a dictionary in geojson format. That dictionary can be turned into a string with
    json.dump(), saved as a .json file, and then used by leaflet or other mapping libraries

    :param df: Obj. Your pandas dataframe
    :param properties: List. A list of all the columns in your dataframe that you want assigned to the geojson's 'properties' prop
    :param lat: Optional. String. The name of the column in your df that has your latitude. Defaults to 'latitude'
    :param lon: Optional. String. The name of the column in your df that has your latitude. Defaults to 'longitude'
    :return: A dictionary in geojson format
    """

    geojson = {"type": "FeatureCollection", "features": []}
    for _, row in df.iterrows():
        feature = {
            "type": "Feature",
            "properties": {},
            "geometry": {"type": "Point", "coordinates": []},
        }
        feature["geometry"]["coordinates"] = [row[lon], row[lat]]
        for prop in properties:
            feature["properties"][prop] = row[prop]
        geojson["features"].append(feature)
    return geojson
