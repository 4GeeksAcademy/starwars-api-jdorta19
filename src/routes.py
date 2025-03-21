from flask import Flask, request, jsonify
from models import db, User, People, Planet, Favorite

app = Flask(__name__)

@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([p.name for p in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({"name": person.name})

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([p.name for p in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    return jsonify({"name": planet.name})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.username for u in users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = 1  # Simulación de usuario actual
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([{"people_id": f.people_id, "planet_id": f.planet_id} for f in favorites])

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = 1  # Simulación de usuario actual
    favorite = Favorite(user_id=user_id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite added"}), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user_id = 1  # Simulación de usuario actual
    favorite = Favorite(user_id=user_id, people_id=people_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite added"}), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = 1
    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite removed"}), 200
    return jsonify({"error": "Favorite not found"}), 404

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user_id = 1
    favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite removed"}), 200
    return jsonify({"error": "Favorite not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
