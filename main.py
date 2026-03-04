from flask import Flask, jsonify, request, render_template
from jobspy import scrape_jobs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and all origins

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/jobs', methods=['GET'])
def scrape():
    search = request.args.get('search', 'software engineer')
    location = request.args.get('location', 'remote')
    country = request.args.get('country', 'india')
    limit = request.args.get('limit', 21)
    limit = int(limit)
    ago = request.args.get('ago', 72)
    
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "google", "zip_recruiter"],
            search_term=search,
            location=location,
            results_wanted=limit,
            hours_old=ago,
            country_indeed=country,
        )

        # This drops the entire job "dataset" if there's no description
        jobs = jobs[jobs['description'].notna() & (jobs['description'] != "")]

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