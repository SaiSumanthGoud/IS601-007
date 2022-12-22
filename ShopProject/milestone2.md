<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Sai Sumanth Goud Parakala (sp2927)</td></tr>
<tr><td> <em>Generated: </em> 22/12/2022 18:11:20</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/sp2927" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208471074-1e20fd4e-ba7f-48c9-8a73-e383d9ceb70a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of admin create item page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208471265-ec096da9-5488-416e-9b45-30ae7b011e48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of populated Products table clearly showing the column<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the form is filled with valid data and submitted, I check if<br>an id is present in the arguments to confirm if it is an<br>edit or create operation. If no id, the server validation is done with<br>the validate_on_submit() function.&nbsp;</li><li>Once validated, all the details are inserted into the database and<br>a message is flashed to confirm creation.&nbsp;</li><li>If any error occurs, then the respective<br>message is flashed</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/29">https://github.com/SaiSumanthGoud/IS601-007/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/admin/product">https://is601-sp2927-prod-2.herokuapp.com/admin/product</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208493321-a5a01c52-01df-4169-a469-985249634f39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing first 5 items without filters/sorting applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208493448-c491078f-a0ef-4b69-a4f8-f8327e4f8150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing last 5 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208493880-2fcb3a51-2ee2-414a-934a-e392e3c312e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both category filter and a sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208484862-958083ec-ba0d-4864-95ac-c5f642c3dbdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <ul><li>On page load, the category list dropdown is generated by accumulating the category<br>types present in the database.</li><li>Then we check if any of the filters are<br>selected, if yes then the respective filters are appended to the fetching query.</li><li>All<br>the products are fetched from the database with filters applied if any whose<br>stock is greater than 0, and visibility is set to true.<br></li><li>A message is<br>flashed if any error occurs while fetching products</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/30">https://github.com/SaiSumanthGoud/IS601-007/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/shop">https://is601-sp2927-prod-2.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208499123-135f36f2-a611-4034-a2e4-b804440dd04f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Admin/Shop Owner Product List page with non visible product highlighted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <ul><li>All the product details are fetched including non-visible items. Visibility is marked true<br>if 1 else false in the query logic.</li><li>The fetched products are rendered with<br>the help of table_helper.html</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/30">https://github.com/SaiSumanthGoud/IS601-007/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/admin/product/list">https://is601-sp2927-prod-2.herokuapp.com/admin/product/list</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208529451-79e04d81-8f1e-4f29-b290-04a0b3524e64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208529671-f7a6c3f0-9220-49e1-a4f5-6dc9af180dd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208532405-65da790f-04fc-43de-afe7-d72f08e443cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208532630-27275af4-70cc-4365-aad5-c4f179044026.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before Editing a Product <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208536987-efeec892-91bb-4a7b-90d4-88d746f53658.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after Editing a Product title, description and its stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208539191-8f6372c1-2d82-4f76-a559-3afe81aeb974.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of admin edit page after Editing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ul><li>The edit page takes an id as an argument and preloads its details<br>in the form.</li><li>After updating the values and clicking "Edit Product", all the values<br>are updated in the data base with an update query.</li><li>A message is flashed<br>for success or failure of the operation.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/31">https://github.com/SaiSumanthGoud/IS601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/admin/product?id=21">https://is601-sp2927-prod-2.herokuapp.com/admin/product?id=21</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208540305-3dadd061-d8c8-42df-8af4-26228182f02e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the clickable item that directs the user to the Product Details<br>Page. Here the highlighted title is clickable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208540092-803536fd-ab85-4b18-8b08-3a4a6a2592e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ul><li>On clicking the product title on the shop list page, the product details<br>page is loaded with the corresponding id passed as an argument.</li><li>The id is<br>fetched from arguments, and all the details of that product are fetched from<br>the database.</li><li>These details are populated in a horizontal card layout.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/31">https://github.com/SaiSumanthGoud/IS601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/admin/productDetails?id=23">https://is601-sp2927-prod-2.herokuapp.com/admin/productDetails?id=23</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208555849-fc70d252-d55a-40e3-ac1d-dd4d4167b8a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208555959-1730f30d-b9e2-4d0c-951e-f0692bb6982e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the error message of adding to cart when not logged<br>in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208556089-397314cc-4763-4b64-979a-1456553aff2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table from UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208556213-a7b6e5b4-4094-475c-8140-f27e77d570e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table from database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>The cart works as 1 cart per user where the user can add<br>multiple different products.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <ul><li>When a product is added to the cart by clicking on "+Add"&nbsp; button,<br>the corresponding id and quantity selected are passed to the cart route.</li><li>Cart inserts<br>the product id, quantity, cost, and user_id into the cart table.</li><li>If the product<br>is already present in the cart then its quantity is updated.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/32">https://github.com/SaiSumanthGoud/IS601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208556089-397314cc-4763-4b64-979a-1456553aff2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View showing each product subtotal and cart total. <br>Each product name is the link to it&#39;s product details page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208557151-ebfaf537-6426-41fb-bef8-81522b3c0e00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View with different products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <ul><li>All the details stored in the cart table are fetched and displayed</li><li>subtotal of<br>each item is calculated based on the unit price and quantity in the<br>select query.</li><li>The total is calculated by adding all the subtotals while&nbsp; rendering with<br>the namespace provided by Jinja2</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/32">https://github.com/SaiSumanthGoud/IS601-007/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/cart">https://is601-sp2927-prod-2.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208557380-6f5d993b-7e16-4645-bd82-2b404c687487.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of Cart before Quantity update - Thermal pant quantity is 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208557524-52f126a8-2115-4448-bda9-04ef0aac6656.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of Cart after Quantity update - Thermal pant quantity is updated to<br>10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208557524-52f126a8-2115-4448-bda9-04ef0aac6656.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before setting Cart Quantity to 0 - Thermal pant quantity is 10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208557742-3e7e3f83-3000-47e1-a53c-1e85b884109f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after setting Cart Quantity to 0 - Thermal pant got deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208558670-5464fe0e-5ae2-48f3-b29c-95d4c2a23479.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Negative quantity will delete the product from the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the update button is clicked the product_id is sent in the post<br>request which indicates that its an update.</li><li>The quantity is updated to the respective<br>product id.</li><li>For each update, the quantity is checked if it is greater than<br>0. If not, then the corresponding product is deleted from the card.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/32">https://github.com/SaiSumanthGoud/IS601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208558877-5cdc8084-2882-48b9-b363-bd552fcd2009.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before deleting product-1 from the Cart <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208559018-3f0571db-d26f-4286-8d82-0cf5aac50b3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after deleting product-1 from the Cart <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208559154-13d725e3-d78e-4c16-9fa8-d2077f54e48f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208559212-f9e8ef48-80a7-484c-979b-c8015fc363e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <ul><li>Deleting each product also follows the logic of the update quantity.&nbsp;</li><li>We pass a<br>negative quantity value when the delete is clicked which deletes the corresponding product<br>from the cart.</li><li>On Clear all, I send action clear in the post request,<br>when that condition meets it deletes all the products of that particular user<br>from the database by matching user id</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/32">https://github.com/SaiSumanthGoud/IS601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I have tried to implement file upload for images while adding new products,<br>and it did work fine locally but not on Heroku. I took an<br>alternate approach of adding host image URLs to render images. Learnt and practiced<br>how to efficiently reuse the code for similar actions like deletion and updating<br>quantity to 0 or lesser.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/login">https://is601-sp2927-prod-2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/sp2927" target="_blank">Grading</a></td></tr></table>