import sys

from json import JSONDecodeError
from app import create_app
from app.utils import Utils


app = create_app()
try:
    cv_data = Utils.parse_data_json_file()
except (AttributeError, JSONDecodeError, KeyError) as exc:
    print("Exiting...")
    sys.exit(1)


@app.cli.command("personal")
@app.route('/personal')
def get_personal_info():
    """
    GET /personal
    :return: personal info of the candidate
    """
    data = {
        "name": cv_data.name,
        "address": cv_data.address
    }

    print(data)
    return data


@app.cli.command("experience")
@app.route('/experience')
def get_experience():
    """
    GET /experience
    :return: the candidate's experience
    """
    print(cv_data.experience)
    return cv_data.experience


@app.cli.command("education")
@app.route('/education')
def get_education():
    """
    GET /education
    :return: the candidate's education history
    """
    print(cv_data.education)
    return cv_data.education


if __name__ == '__main__':
    pass
