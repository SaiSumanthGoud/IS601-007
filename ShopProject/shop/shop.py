import os
import traceback
from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from werkzeug.utils import secure_filename
from shop.forms import AddProductForm, CheckoutForm, EditProductForm
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
        if form.id.data: # it's an update
            try:
                print(form.visible.data)
                result = DB.update("UPDATE IS601_Products set name = %s, description = %s,category = %s, visibility = %s,stock = %s, unit_price = %s, image=%s WHERE id = %s",
                form.name.data, form.description.data,form.category.data, 1 if form.visible.data else 0,form.stock.data, form.unit_price.data, form.image.data, form.id.data)
                if result.status:
                    flash(f"Updated Product - {form.name.data}", "success")
            except Exception as e:
                print("Error updating product", e)
                flash(f"Error updating product {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_Products (name, description, category, visibility, stock, unit_price, image) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data,form.category.data, 1 if form.visible.data else 0,form.stock.data, form.unit_price.data, form.image.data)
                if result.status:
                    flash(f"Created Product - {form.name.data}", "success")
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

@shop.route("/shop", methods=["GET","POST"])
def shop_list():
    rows = []
    category_list = []
    args = []
    # UCID: sp2927
    # Date: 19-12-2022
    query = """SELECT id, name, description, stock, unit_price, image FROM IS601_Products WHERE stock > 0 AND visibility = 1"""
    category_result = DB.selectAll("SELECT DISTINCT category from IS601_Products",)
    if category_result.status and category_result.rows:
        for cat in category_result.rows:
            print(cat['category'])
            category_list.append(cat['category'])
        print(category_list)

    product_name  = request.args.get("product_name")
    cat_selected  = request.args.get("category")
    sort_by = request.args.get('sort_by')
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    if product_name:
        query += " AND name like %s"
        args.append(f"%{product_name}%")
    if cat_selected:
        query += " AND category = %s"
        args.append(f"{cat_selected}")
    if sort_by and order:
        if order in ["asc", "desc"]:
            query += f" ORDER BY {sort_by} {order}"
    if limit:
        query += f" LIMIT {limit}"

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching products", e)
        flash("There was a problem loading products", "danger")
    return render_template("shop.html", rows=rows,category_list=category_list)
    
@shop.route("/admin/product/list", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def product_list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, category, stock, unit_price as cost, image, if (visibility = 1,'True','False') as visible FROM IS601_Products LIMIT 25")
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching products", e)
        flash("There was a problem loading products", "danger")
    return render_template("product_list.html", rows=rows)

@shop.route("/admin/productDetails", methods=["GET"])
def productDetails():
    id = request.args.get("id", None)
    type = "View"
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, visibility as visible, stock, unit_price, image FROM IS601_Products WHERE id = %s", id)
            if result.status and result.row:
                row = result.row
        except Exception as e:
            print("Error fetching product", e)
            flash("product not found", "danger")
    return render_template("product.html", row=row, type=type)

@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    product_id = request.form.get("product_id")
    id = request.form.get("id", product_id)
    action = request.args.get("action")
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if action == "clear":
        try:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", user_id)
            if result.status:
                flash("Cart cleared", "success")
        except Exception as e:
                    print("Error clearing cart" ,e)
                    flash("Error clearing cart", "danger")
    else:
        if id and user_id:
            if quantity > 0:
                try:
                    result = DB.selectOne("SELECT unit_price,name from IS601_Products WHERE id = %s", id)
                    print("result", result)
                    if result.status and result.row:
                        cost = result.row["unit_price"]
                        name = result.row["name"]
                        if product_id: # update from cart
                            result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s,
                            cost = %(cost)s
                            WHERE product_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "cost":cost,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Updated quantity for {name} to {quantity}", "success")
                        else: #add from shop
                            result = DB.insertOne("""
                            INSERT INTO IS601_S_Cart (product_id, quantity, cost, user_id)
                            VALUES(%(id)s, %(quantity)s, %(cost)s, %(user_id)s)
                            ON DUPLICATE KEY UPDATE
                            quantity = quantity + %(quantity)s,
                            cost = %(cost)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "cost":cost,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Added {quantity} of {name} to cart", "success")
                except Exception as e:
                    print("Error updating cart" ,e)
                    flash("Error updating cart", "danger")
            else:
                # assuming delete
                try:
                    result = DB.delete("DELETE FROM IS601_S_Cart where product_id = %s and user_id = %s", id, user_id)
                    if result.status:
                        flash("Deleted product from cart", "success")
                except Exception as e:
                    print("Error deleting product", e)
                    flash("Error deleting product from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, (c.quantity * c.cost) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)
    
@shop.route("/admin/products/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Products WHERE id = %s", id)
            if result.status:
                flash("Deleted product", "success")
        except Exception as e:
            print("Error deleting product",e)
            flash("Error deleting product", "danger")
    return redirect(url_for("shop.product_list"))

@shop.route("/checkout", methods=["GET","POST"])
@login_required
def checkout():
    form = CheckoutForm()
    user_id = current_user.get_id()
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, (c.quantity * c.cost) as subtotal, (((i.unit_price - c.cost)/c.cost) * 100) as price_change
        FROM IS601_S_Cart c JOIN IS601_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, user_id)
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("checkout.html", form=form, rows=rows)

@shop.route("/purchase", methods=["GET","POST"])
@login_required
def purchase():
    cart = []
    total = 0
    quantity = 0
    order = {}
    form = CheckoutForm()
    paymentMethod = request.form.get('paymentMethod')
    if paymentMethod == '':
        flash(f"Payment method has to be selected", "warning")
        return redirect(url_for('shop.checkout'))
    if form.validate_on_submit():
        amountPaid = request.form.get('amount')
        address = request.form.get('address')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        zipcode = request.form.get('zip')

        try:
            DB.getDB().autocommit = False # make a transaction

            # get cart to verify
            
            result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, i.stock, c.cost as cart_cost, i.unit_price as product_cost, (c.quantity * c.cost) as subtotal 
            FROM IS601_S_Cart c JOIN IS601_Products i on c.product_id = i.id
            WHERE c.user_id = %s
            """, current_user.get_id())
            if result.status and result.rows:
                cart = result.rows
            has_error = False
            for item in cart:
                if item["quantity"] > item["stock"]:
                    flash(f"Product {item['name']} doesn't have enough stock left", "warning")
                    has_error = True
                if item["cart_cost"] != item["product_cost"]:
                    flash(f"Product {item['name']}'s price has changed, please re-add the product to the cart", "warning")
                    has_error = True
                total += int(item["subtotal"] or 0)
                quantity += int(item["quantity"])
            if not has_error:
                if total != int(amountPaid):
                    flash("The amount entered does not match the cart total", "danger")
                    has_error = True
            # create order data
            order_id = -1
            if not has_error:
                result = DB.insertOne("""INSERT INTO IS601_S_Orders (
                    total_price, address, zip, payment_method, money_received, first_name, last_name, user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", total, address, zipcode, paymentMethod, amountPaid, first_name, last_name, current_user.get_id())
                if not result.status:
                    flash("Error generating order", "danger")
                    DB.getDB().rollback()
                    has_error = True
                else:
                    order_id = int(DB.db.fetch_eof_status()["insert_id"])
                    order["order_id"] = order_id
                    order["first_name"] = first_name
                    order["last_name"] = last_name
                    order["address"] = address
                    order["zip"] = zipcode
                    order["paymentMethod"] = paymentMethod
                    order["total"] = total
                    order["amountPaid"] = amountPaid
            # record order history
            if order_id > -1 and not has_error:
                # Note: Not really an insert 1, it'll copy data from Table B into Table A
                result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, cost, order_id, product_id, user_id)
                SELECT quantity, cost, %s, product_id, user_id FROM IS601_S_Cart c WHERE c.user_id = %s""",
                order_id, current_user.get_id())
                if not result.status:
                    flash("Error recording order history", "danger")
                    has_error = True
                    DB.getDB().rollback()
            # update stock based on cart data
            if not has_error:
                result = DB.update("""
                UPDATE IS601_Products 
                    set stock = stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE product_id = IS601_Products.id and user_id = %(uid)s) 
                    WHERE id in (SELECT product_id from IS601_S_Cart where user_id = %(uid)s)
                """, {"uid":current_user.get_id()} )
                if not result.status:
                    flash("Error updating stock", "danger")
                    has_error = True
                    DB.getDB().rollback()
            
            # empty the cart
            if not has_error:
                result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
                DB.getDB().commit()
                flash("Purchase successful!", "success")
            else:
                return redirect(url_for("shop.cart"))
        
        except Exception as e:
            print("Transaction exception", e)
            flash("Something went wrong", "danger")
            traceback.print_exc()
    else:
        return redirect(url_for('shop.checkout'))
        
    return render_template("order_summary.html", rows=cart, order=order)