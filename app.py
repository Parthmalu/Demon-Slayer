from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

home_page = '''
<!doctype html>
<html lang="en">
<head>
  <title>Movie with me?(Tuesday)</title>
  <style>
    body {
      background: linear-gradient(135deg, #6b73ff 0%, #000dff 100%);
      height: 100vh;
      margin: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 3.5rem;
      margin-bottom: 25px;
      text-shadow: 2px 2px 8px #000000aa;
    }
    form button {
      font-size: 1.3rem;
      padding: 12px 28px;
      margin: 0 15px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background-color: #ff4757;
      color: white;
      box-shadow: 0 4px 8px rgba(255, 71, 87, 0.6);
      transition: background-color 0.3s ease;
    }
    form button:hover {
      background-color: #ff6b81;
    }
    .no {
      background-color: #57606f;
      box-shadow: 0 4px 8px rgba(87, 96, 111, 0.6);
    }
    .no:hover {
      background-color: #747d8c;
    }
    .error-message {
      color: #ff6b81;
      font-weight: bold;
      margin-bottom: 20px;
      text-shadow: 1px 1px 4px #00000099;
    }
    img {
      margin-top: 35px;
      max-width: 320px;
      border-radius: 12px;
      box-shadow: 0 0 15px #ff4757aa;
    }
  </style>
</head>
<body>
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <div class="error-message">{{ messages[0] }}</div>
    {% endif %}
  {% endwith %}

  <h1>Movie with me?</h1>
  
  <form method="post" action="/">
    <button type="submit" name="choice" value="yes">Yes</button>
    <button type="submit" name="choice" value="no" class="no">No</button>
  </form>
  
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDJrN2o0MWhiemd3dHpqdXpiODlhbzI4c3MxZmV1YmZrMHFxZ2V4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R9TbpugxAhx9UnerhD/giphy.gif" alt="Demon Slayer GIF">
</body>
</html>
'''

gif_page = '''
<!doctype html>
<html lang="en">
<head>
  <title>Let's Watch!</title>
  <style>
    body {
      background: linear-gradient(135deg, #ff6b81 0%, #ff4757 100%);
      height: 100vh;
      margin: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 3rem;
      margin-bottom: 30px;
      text-shadow: 2px 2px 8px #590000bb;
    }
    img {
      max-width: 400px;
      border-radius: 12px;
      box-shadow: 0 0 25px #ff6b8188;
    }
  </style>
</head>
<body>
  <h1>Yayyyyy!!!!</h1>
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3FrZTQ4azA4NnE2N2l4cHJpMnh4aDE5cWZ4amcwb2gwNXUzNnJicyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PV7VZN4pix1EE2IAqo/giphy.gif" alt="Movie GIF">
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == "yes":
            return redirect(url_for('gif'))
        else:
            flash("TRY PRESSING YES")
            return redirect(url_for('home'))
    return render_template_string(home_page)

@app.route("/gif")
def gif():
    return render_template_string(gif_page)

if __name__ == "__main__":
    app.run(debug=True)
