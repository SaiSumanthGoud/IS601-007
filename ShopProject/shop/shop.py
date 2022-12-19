import os
from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from werkzeug.utils import secure_filename
from shop.forms import AddProductForm, EditProductForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

@shop.route("/admin/product", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def product():
    id = request.args.get("id", None)
    if id:
        form = EditProductForm()
        type = "Edit"
    else:
        form = AddProductForm()
        type = "Create"
        
    if form.validate_on_submit():
        path = "static/assets/placeholder.png"
        if request.files['image']:
            f = request.files['image']
            path = os.path.join('static/assets/', secure_filename(f.filename))
            f.save(path)
        if form.id.data: # it's an update
            try:
                print(form.visible.data)
                result = DB.update("UPDATE IS601_Products set name = %s, description = %s,category = %s, visibility = %s,stock = %s, unit_price = %s, image=%s WHERE id = %s",
                form.name.data, form.description.data,form.category.data, 1 if form.visible.data else 0,form.stock.data, form.unit_price.data, path, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating product", e)
                flash(f"Error updating product {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_Products (name, description, category, visibility, stock, unit_price, image) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data,form.category.data, 1 if form.visible else 0,form.stock.data, form.unit_price.data, path)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = AddProductForm() # clear form
            except Exception as e:
                print("Error creating product", e)
                flash(f"Error creating product {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, visibility as visible,stock, unit_price, image FROM IS601_Products WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching product", e)
            flash("product not found", "danger")
    return render_template("product.html", form=form, type=type)