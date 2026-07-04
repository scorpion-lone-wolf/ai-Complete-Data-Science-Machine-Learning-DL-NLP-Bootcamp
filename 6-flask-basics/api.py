from flask import Flask, jsonify, request

app = Flask(__name__)

# data
data = [
    {
        "id": 1,
        "name": "Study",
        "description": "I need to complete this flask tutorial today",
    },
    {
        "id": 2,
        "name": "exercise",
        "description": "I need to do exercise daily",
    },
]


# routes
@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "healthy"}), 200


# create a task
@app.route("/task", methods=["POST"])
def create_task():
    try:
        # taking the user data from body
        body = request.get_json()
        name = body["name"]
        description = body["description"]

        task = {
            "id": len(data) + 1,
            "name": name,
            "description": description,
        }
        # insert the task
        data.append(task)
        return jsonify(task), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# get all task
@app.route("/task", methods=["GET"])
def get_all_task():
    return jsonify(data), 200


# get a single task by id
@app.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    print(id)
    for task in data:
        if task["id"] == id:
            return jsonify(task), 200
    return jsonify({"error": "task not found"}), 404


# update a task based on id
@app.route("/task/<int:id>", methods=["PATCH"])
def update_task(id):
    try:
        # taking the user data from body
        body = request.get_json() or {}
        name = body.get("name")
        description = body.get("description")
        if not name and not description:
            return jsonify({"error": "name or description is required"}), 400
        # find the task that need to be updated
        for task in data:
            if task["id"] == id:
                if name:
                    task["name"] = name
                if description:
                    task["description"] = description
                return jsonify(task), 200
        return jsonify({"error": "task not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# delete a task on id
@app.route("/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    for task in data:
        if task["id"] == id:
            data.remove(task)
            return jsonify(task), 200
    return jsonify({"error": "task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)
