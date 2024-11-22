from Python import create_app

# Create an app instance using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the Flask application on all available network interfaces
    app.run(host='0.0.0.0', port=5000, debug=True)
