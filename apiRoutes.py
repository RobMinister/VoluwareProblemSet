from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to add a new item to a department's inventory
@app.route("/items", methods=["POST"])
def add_item():

    # Inbound Payload:
    # {
    #     "department": "Clothing",
    #     "name": "Men's Shirt",
    #     "inventory_count": 20,
    #     "alert_threshold": 10
    # }

    #Outbound Payload
    return jsonify({
        "message": "Item added successfully",
        "item_id": 1
    })

# Endpoint to update the inventory count and alert threshold of an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):

    # Inbound Payload:
    # {
    #     "inventory_count": 8,
    #     "alert_threshold": 5
    # }
    
    #Outbound Payload
    return jsonify({
        "message": "Item updated",
        "alert_triggered": True
    })

# Returns a full inventory report for the specified department, including item names, current stock, and alert thresholds
@app.route("/departments/<string:dept_name>/report", methods=["GET"])
def department_report(dept_name):

    #Outbound Payload
    return jsonify({
        "department": dept_name,
        "items": [
            {
                "name": "Men's Shirt",
                "inventory_count": 8,
                "alert_threshold": 10
            },
            {
                "name": "Women's Jeans",
                "inventory_count": 25,
                "alert_threshold": 5
            }
        ]
    })