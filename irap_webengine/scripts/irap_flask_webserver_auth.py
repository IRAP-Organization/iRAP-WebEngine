from flask import Flask, render_template ,jsonify, request
from flask_cors import CORS , cross_origin

import os
import rospkg

print("current directory : " , os.getcwd())

def get_package_path(package_name):
    rospack = rospkg.RosPack()
    try:
        package_path = rospack.get_path(package_name)
        return package_path
    except rospkg.ResourceNotFound:
        print(f"Error: Package '{package_name}' not found.")
        return None

print("webengine path : " , get_package_path("irap_webengine"))

webEngine = str(get_package_path("irap_webengine")) + "/scripts/" + "build" 

app = Flask(__name__, static_folder=webEngine, static_url_path='')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def static_proxy(path):
    # Send static files from the React build folder
    return app.send_static_file('index.html')

if __name__ == '__main__':

    # app.root_path = '/'
    app.run(host='0.0.0.0' , port=8080 , debug=False)
    
    CORS(app)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    cors.init_app()


