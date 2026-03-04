from flask import Flask, jsonify, request
from jobspy import scrape_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello, World! Jobs Scraper is running. Use /scrape endpoint."}

@app.route('/scrape', methods=['GET'])
def scrape():
    # Dynamically take parameters
    search = request.args.get('search', 'software engineer')
    location = request.args.get('location', 'Kolkata, West Bengal, India')
    country = request.args.get('country', 'INDIA')
    
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "google"],
            search_term=search,
            location=location,
            results_wanted=10,
            hours_old=72,
            country_indeed=country,
        )

        # Use to_dict instead of to_json to keep it as a Python list of objects
        jobs_list = jobs.to_dict(orient="records")
        
        # Build the final response object
        response = {
            "total": len(jobs),
            "jobs": jobs_list
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Using a safe port (8000) to avoid browser "Unsafe Port" errors
    app.run(host='0.0.0.0', port=8000, debug=True)