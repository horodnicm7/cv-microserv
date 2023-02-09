## How to run?
1. Create a virtual environment and activate it
````
python3 -m venv virtualenv
source virtualenv/bin/activate
````
2. Install the dependencies
````
pip install -r requirements.txt
````
3. Run the project as a REST API
````
flask --app app/main --debug run
````

4. (Optional) If you want to run the project as CLI commands, 
first export the FLASK_APP variable to tell Flask where it can 
find the application
````
export FLASK_APP=app/main
````
then run any of these commands, to access specific endpoints:
````
flask personal
flask experience 
flask education
````
