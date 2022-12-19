from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, URLField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

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