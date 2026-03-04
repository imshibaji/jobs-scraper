# পাইথনের লাইটওয়েট ভার্সন ব্যবহার করা হয়েছে
FROM python:3.10-slim

# সার্ভারে প্রয়োজনীয় টুলস ইনস্টল করা (jobspy এর জন্য লাগতে পারে)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# কাজের ডিরেক্টরি সেট করা
WORKDIR /app

# লাইব্রেরিগুলো কপি এবং ইনস্টল করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# সব কোড কপি করা
COPY . .

# পোর্ট এক্সপোজ করা
EXPOSE 8000

# অ্যাপ রান করা
CMD ["python", "main.py"]