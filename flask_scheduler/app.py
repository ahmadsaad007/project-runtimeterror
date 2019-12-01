from flask import Flask, render_template, url_for, flash, redirect
from forms import ScheduleForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aae3d59542630a35356332ea6ca60652'

@app.route('/',methods=['GET','POST'])
def home():
    form = ScheduleForm()
    checkValidation = form.validate_on_submit()
    if checkValidation:
        flash(f'Schedule will be made for {form.class1.data}, {form.class2.data}, {form.class3.data}','success')
        classes = [
            {
                'crn':'11111',
                'name':'class name 1',
                'meeting_time':'MWF 5:00-5:50'
            },
            {
                'crn':'2222',
                'name':'class name 2',
                'meeting_time':'MWF 6:00-6:50'
            }
        ]
        return render_template('schedule.html',title='Schedule Maker - Schedule',classes=classes)
    print(form.errors)
    print(checkValidation)
    return render_template('home.html',title='Schedule Maker - Home', form = form)

@app.route('/schedule')
def schedulePage():
    return render_template('schedule.html',title='Schedule Maker - Schedule',classes=classes)

if __name__ == '__main__':
    app.run(debug=True)