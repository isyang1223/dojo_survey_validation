from flask import Flask, render_template, request, redirect, flash, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def take():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def result():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!") 
    return redirect("/")
  else:
    name = request.form['name']
    
  location = request.form['location']
  language = request.form['language']

  if len(request.form['comment']) < 1:
    flash("Comment cannot be empty!") 
    return redirect("/")
  elif len(request.form['comment']) > 120:
    flash("Comment cannot be longer than 120 characters!") 
    return redirect("/")
  else:
    comment = request.form['comment']

  return render_template('results.html',name = name, location = location, language = language, comment = comment)



app.run(debug=True) # run our server