from flask import Flask, render_template, abort
from calendar import Calendar
from datetime import date

app = Flask(__name__)


@app.route('/', defaults={'year': None})
@app.route('/<int:year>/')
def index(year):
    cal = Calendar(0)
    try:
        if not year:
            year = date.today().year
        cal_list = [
            cal.monthdatescalendar(year, i+1)
            for i in range(12)
        ]
    except:
        abort(404)
    else:
        return render_template('cal.html', year=year, cal=cal_list)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
