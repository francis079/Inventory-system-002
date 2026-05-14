from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

inventory = []

def load_inventory():
    global inventory
    if os.path.exists('inventory.json'):
        with open('inventory.json', 'r') as f:
            inventory = json.load(f)


def save_inventory():
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)

load_inventory()

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    description = request.form.get('description', '')
    item_id = max([i['id'] for i in inventory] + [0]) + 1
    inventory.append({'id': item_id, 'name': name, 'category': category, 'quantity': quantity, 'price': price, 'description': description})
    save_inventory()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return 'Item not found', 404
    if request.method == 'POST':
        item['name'] = request.form['name']
        item['category'] = request.form['category']
        item['quantity'] = int(request.form['quantity'])
        item['price'] = float(request.form['price'])
        item['description'] = request.form.get('description', '')
        save_inventory()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    global inventory
    inventory = [i for i in inventory if i['id'] != item_id]
    save_inventory()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
