from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample data for search
data = [
    {'name': 'John Doe', 'age': 25, 'city': 'New York'},
    {'name': 'Jane Smith', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Michael Johnson', 'age': 35, 'city': 'Chicago'},
    {'name': 'Emily Davis', 'age': 28, 'city': 'Los Angeles'}
]

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Search route
@app.route('/search', methods=['POST'])
def search():
    query = ''

    if request.headers['Content-Type'] == 'application/json':
        # Handle JSON request
        data = request.get_json()
        query = data['query']
    else:
        # Handle form request
        query = request.form.get('query')

    results = []

    # Perform search based on query
    for item in data:
        if query.lower() in item['name'].lower() or query.lower() in item['city'].lower():
            results.append(item)

    if request.headers['Content-Type'] == 'application/json':
        # Return search results as JSON
        return jsonify({'results': results})
    else:
        # Render template with search results
        return render_template('results.html', query=query, results=results)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
