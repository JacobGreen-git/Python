from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.email_model import Email


@app.route ('/')
def home():
    return render_template ('email_entry.html')


@app.route('/add_email', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    Email.add_email(request.form)
    return redirect('/results')


@app.route ('/results')
def get_all():
    all_emails = Email.get_all()
    return  render_template('email_display.html', all_emails=all_emails)
