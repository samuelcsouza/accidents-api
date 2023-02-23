from pymongo import MongoClient

_mongo_client = MongoClient(
    "mongodb://mongoadmin:secret@localhost:27017/?authMechanism=DEFAULT",
    connect=False,
)

_mongo_db = _mongo_client["highways"]

accidents_collection = _mongo_db.create_collection("accidents")

def read_file(file_path, encoding="Windows-1252"):
    with open(file_path, "r", encoding=encoding) as _fp:
        col_names = next(_fp).strip().replace('"', "").split(";")
        for line in _fp:
            line_values = line.strip().replace('"', "").replace(",", ".").split(";")

            dict_values = dict(zip(col_names, line_values))

            yield dict_values

_file = read_file("data/datatran2022.csv")

for row in _file:
    row["location"] = {
        "type": "Point",
        "coordinates": [ float(row["longitude"]), float(row["latitude"]) ]
    }

    accidents_collection.insert_one(row)

accidents_collection.create_index([("location", "2dsphere")])
