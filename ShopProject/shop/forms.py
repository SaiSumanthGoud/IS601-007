from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, URLField, IntegerField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, InputRequired

class ProductForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    category = StringField("category", validators=[DataRequired(), Length(max=30)])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    unit_price = IntegerField("cost", validators=[NumberRange(min=0)])
    image = URLField("image", validators=[Optional()])
    visible = BooleanField("visible")

class AddProductForm(ProductForm):
    submit = SubmitField("Add Product")

class EditProductForm(ProductForm):
    submit = SubmitField("Edit Product")

class CheckoutForm(FlaskForm):
    first_name = StringField("first name", validators=[DataRequired(), Length(max=30)])
    last_name = StringField("last name", validators=[DataRequired(), Length(max=30)])
    address = StringField("address", validators=[InputRequired(), DataRequired(), Length(max=100)])
    zip = StringField("Zip", validators=[DataRequired(), InputRequired(), Length(5)], render_kw={"pattern": '[0-9]*', "title": "Enter at least 5 digits"})
    paymentMethod = SelectField(u'Select your Payment Method', default=('', "Select your Payment Method"), choices=[('', "Select your Payment Method"), ("debit", "Debit Card"), ("credit", "Credit Card"), ("paypal", "Paypal")], validators=[DataRequired()])
    amount = IntegerField("Enter Amount To Be Paid", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Place Order")
