from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

home_page = '''
<!doctype html>
<html lang="en">
<head>
  <title>Movie with me?</title>
</head>
<body>
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <p style="color:red;">{{ messages[0] }}</p>
    {% endif %}
  {% endwith %}

  <h1>Movie with me?</h1>
  <form method="post" action="/">
    <button type="submit" name="choice" value="yes">Yes</button>
    <button type="submit" name="choice" value="no">No</button>
  </form>
  <br>
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDJrN2o0MWhiemd3dHpqdXpiODlhbzI4c3MxZmV1YmZrMHFxZ2V4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R9TbpugxAhx9UnerhD/giphy.gif" alt="Demon Slayer GIF" width="300">
</body>
</html>
'''

gif_page = '''
<!doctype html>
<html lang="en">
<head>
  <title>Let's Watch!</title>
</head>
<body>
  <h1>Great! Here's a GIF for you!</h1>
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3FrZTQ4azA4NnE2N2l4cHJpMnh4aDE5cWZ4amcwb2gwNXUzNnJicyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PV7VZN4pix1EE2IAqo/giphy.gif" alt="Movie GIF" width="400">
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
