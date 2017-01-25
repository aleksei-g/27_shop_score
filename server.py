from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, cast
from sqlalchemy.sql import func
from datetime import datetime, timedelta


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.reflect()


class Orders(db.Model):
    __table__ = db.Model.metadata.tables['orders']


@app.route('/')
def score():
    orders_today = Orders.query.filter(cast(Orders.created, Date) ==
                                       datetime.now().date())
    count_confirmed_orders = \
        orders_today.filter(Orders.confirmed.isnot(None)
                            ).order_by(Orders.created).count()
    not_confirmed_orders = orders_today.filter(Orders.confirmed.is_(None))
    price_sum = not_confirmed_orders.with_entities(
        func.sum(Orders.price)).scalar()
    if round(price_sum, 2) % 1 == 0:
        price_sum_format = '{:,.0f}'.format(price_sum).replace(',', ' ')
    else:
        price_sum_format = '{:,.2f}'.format(price_sum).replace(',', ' ')
    count_not_confirmed_order = not_confirmed_orders.count()
    wait_time = datetime.now() - \
        not_confirmed_orders.order_by(Orders.created).first().created
    wait_time = wait_time - timedelta(microseconds=wait_time.microseconds)
    return render_template('score.html',
                           wait_time=wait_time,
                           count_not_confirmed_order=count_not_confirmed_order,
                           count_confirmed_orders=count_confirmed_orders,
                           price_sum=price_sum_format
                           )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
