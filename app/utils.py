import json
from json import JSONDecodeError

from app.models import CV, Experience, Education


class Utils:
    @staticmethod
    def parse_data_json_file(path: str = "data/cv.json"):
        """
        Method that parses a json file and loads its contents in predefined models for CV
        :param path: the path to json file
        :return: CV
        """
        with open(path, encoding="utf-8") as file:
            try:
                data = json.load(file)
            except JSONDecodeError as exc:
                print(f"Exception occured while decoding json file: {str(exc)}")
                raise exc

            experiences = [Experience(**experience_info)
                           for experience_info in data.get("experience")]
            education = [Education(**education_info)
                         for education_info in data.get("education")]

            return CV(name=data["name"],
                      address=data["address"],
                      experience=experiences,
                      education=education)

