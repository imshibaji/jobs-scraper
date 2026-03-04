from flask import Flask, jsonify, request
from jobspy import scrape_jobs
import pandas as pd # Ensure pandas is imported

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello, World! Jobs Scraper is running. Use /scrape endpoint."}

@app.route('/scrape', methods=['GET'])
def scrape():
    search = request.args.get('search', 'software engineer')
    location = request.args.get('location', 'Kolkata, West Bengal, India')
    country = request.args.get('country', 'INDIA')
    limit = request.args.get('limit', 10)
    limit = int(limit)
    ago = request.args.get('ago', 72)
    
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "google"],
            search_term=search,
            location=location,
            results_wanted=limit,
            hours_old=ago,
            country_indeed=country,
        )

        # --- THE FIX STARTS HERE ---
        # 1. Fill NaN values with an empty string or None so JSON is valid
        jobs = jobs.fillna("") 

        # 2. Convert to list of dictionaries
        jobs_list = jobs.to_dict(orient="records")
        # --- THE FIX ENDS HERE ---
        
        response = {
            "total": len(jobs_list),
            "jobs": jobs_list
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)