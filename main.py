from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import subprocess
import toml

app = Flask(__name__)
CORS(app)

@app.route('/runNotebook', methods=['POST'])
def run_notebook():
    notebook_path = 'pistachio.ipynb'
    output_path = 'reports'
    command = f'jupyter nbconvert --to notebook --execute {notebook_path} --output-dir {output_path}'
    subprocess.run(command, shell=True)
    return jsonify('Notebook executed successfully')

@app.route('/getBatterReport', methods=['GET'])
def get_batter_report():
    return send_from_directory('reports', 'batter_sWar.csv')

@app.route('/getPitcherReport', methods=['GET'])
def get_pitcher_report():
    return send_from_directory('reports', 'pitcher_sWar.csv')

@app.route('/getSettings', methods=['GET'])
def get_settings():
    try:
        with open('config/settings.toml', 'r') as file:
            settings_content = file.read()
            print(settings_content)
        return send_from_directory('config', 'settings.toml')
    except FileNotFoundError:
        return jsonify({'error': 'Settings file not found'}), 404

@app.route('/setSettings', methods=['POST'])
def set_settings():
    with open('config/settings.toml', 'r') as file:
        config = toml.load(file)

    data = request.get_json()
    print(data)

    if 'csv_path' in data:
        config['Settings']['csv_path'] = data['csv_path']
    if 'scout_id' in data:
        config['Settings']['scout_id'] = data['scout_id']
    if 'team_id' in data:
        config['Settings']['team_id'] = data['team_id']

    with open('config/settings.toml', 'w') as configfile:
        toml.dump(config, configfile)

    return jsonify('Settings updated successfully')

@app.route('/getBatterColumns', methods=['GET'])
def get_batter_columns():
    return send_from_directory('config', 'batter-columns.txt')

@app.route('/getPitcherColumns', methods=['GET'])
def get_pitcher_columns():
    return send_from_directory('config', 'pitcher-columns.txt')

@app.route('/setBatterColumns', methods=['POST'])
def set_batter_columns():
    data = request.get_data(as_text=True)
    with open('config/batter-columns.txt', 'w') as file:
        file.write(data)
    return jsonify('Batter columns updated successfully')

@app.route('/setPitcherColumns', methods=['POST'])
def set_pitcher_columns():
    data = request.get_data(as_text=True)
    with open('config/pitcher-columns.txt', 'w') as file:
        file.write(data)
    return jsonify('Pitcher columns updated successfully')

@app.route('/getFlagged', methods=['GET'])
def get_flagged():
    return send_from_directory('config', 'flagged.txt')

@app.route('/setFlagged', methods=['POST'])
def set_flagged():
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)
