print("Hello world")

from flask import Flask
import redis

app=Flask("counter")

#db = redis.Redis(host ='localhost',port=63679,decode_responses=True)

#count = 0

db = redis.Redis(
    host='redis-server',
    port=6379,
    decode_responses=True
)

@app.route('/')
def index():
    # .incr() is atomic; it adds 1 to the 'hits' key. 
    # If 'hits' doesn't exist, Redis creates it starting at 0.
  
   # global count
    #count = count + 1

    count = db.incr('hits')

    
    return f"""
    <html>
        <head><title>Counter App</title></head>
        <body style="text-align: center; margin-top: 50px; font-family: sans-serif;">
            <h1>Welcome!</h1>
            <p>This page has been viewed</p>
            <h2 style="color: #2e7d32;">{count} times</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    print("Starting app")
    app.run(debug=True, host="0.0.0.0")
