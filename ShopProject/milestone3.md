<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Sai Sumanth Goud Parakala (sp2927)</td></tr>
<tr><td> <em>Generated: </em> 22/12/2022 18:36:46</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-shop-project/grade/sp2927" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208727626-b58f3d04-c78c-4d04-885d-909e9e7f802e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Orders table with valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208727813-c2bd4719-f610-44f8-a5f0-fcf7c737039b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of OrderItems table with validate data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208728689-9656a698-8974-4c34-a963-55bd81defb8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the purchase form UI<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208728965-d875a1bd-2590-42f4-a5ef-348226a6cf53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the items pending purchase, total purchase price and a link back<br>to cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208729511-12a92aa1-fc79-4d18-81a2-6bad90647365.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing % price change to the user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208730476-b27a9b4f-c806-4fe7-9f31-1b229ef0f4e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the Order Process validations for payment, address and zip code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208730743-e863e59e-8867-4668-af14-9d0dc58585bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the Order Process validations for paid amount vs cart amount, stock<br>and price of items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208731317-c6652578-bbb9-4720-bb63-e9c7ebd6db1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the Price difference message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208731678-686c35ed-7f20-4249-ab60-7ad038f02bd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208731878-1a3b5601-a9ac-411c-9694-8fe35343ba03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing invalid &quot;Money Received&quot; message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ul><li>After adding products to the cart, we have a button to checkout.</li><li>On clicking<br>checkout, it is redirected to the checkout page where the same cart details<br>are fetched from the cart table&nbsp;and rendered as pending items to be purchased.<br>A shipping address form will be populated below it.</li><li>On entering details and clicking<br>on place order, each item quantity is checked if it is within the<br>stock available. Then if the cart cost of the product matches the product<br>cost in the database.</li><li>The amount paid is matched with cart server value to<br>validate.</li><li>If the above validations are satisfied then the shipping details are inserted into<br>the orders table and cart details are inserted into the orderItems table else<br>redirected to the cart page flashing the corresponding error message.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/33">https://github.com/SaiSumanthGoud/IS601-007/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/checkout">https://is601-sp2927-prod-2.herokuapp.com/checkout</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208732506-78a5203d-9113-4bd9-97d3-e0f5ba8f69af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the order details from the purchase form and the related items<br>that were purchased with a thank you message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <ul><li>During the purchase the cart details fetched for validation are also passed to<br>render on the order summary page.</li><li>When the order was confirmed and the data<br>was inserted on to orders table, the details were also saved in an<br>array and passed to oder_summary to render</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/33">https://github.com/SaiSumanthGoud/IS601-007/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/purchase">https://is601-sp2927-prod-2.herokuapp.com/purchase</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208751288-b27885d6-ad28-4f08-8f9c-95834d53d1f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing purchase history for a user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208751401-d6146313-03be-47d0-ac38-6482429fc0b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <ul><li>The order details saved on the orders table are fetched for that user_id<br>and displayed with a view button.</li><li>On clicking the view button the order id<br>is passed to the order details page, all the details shown in the<br>order_summary page are fetched by joining the products and order_items table for product<br>details, and shipping details are fetched from the orders table.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/33">https://github.com/SaiSumanthGoud/IS601-007/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/orders">https://is601-sp2927-prod-2.herokuapp.com/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208758892-2b00fb04-f8f1-4cb2-b05d-187a679f2115.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing purchase history from multiple users - two users with username admin<br>and john-updated can be seen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208759143-363776c7-4c8d-44a3-b128-15b0a0613a12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase made by user - &quot;john-updated&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>It is mostly similar to the&nbsp;<span style="letter-spacing: 0.09996px;">user&#39;s purchase history feature, the difference<br>is that the user_id filter is not applied while fetching the orders list<br>so that the result includes orders of all the users.</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/34">https://github.com/SaiSumanthGoud/IS601-007/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/admin/orders">https://is601-sp2927-prod-2.herokuapp.com/admin/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/208759461-f9697422-8442-485f-b370-54368cd3dcaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart page showing the button to checkout or place an<br>order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned what all to be included in server-side validations for a safe purchase<br>by referring to the sample SHOP project given in the class. Faced issues<br>while fetching the order details by clicking the view button. Resolved it by<br>executing a static query and debugging it in the database.<div><br></div><div>Note: At places where<br>I used the same pull request, it has separate commits for each feature.<br>I forgot to merge the pull request after developing each feature which resulted<br>in a pull request with multiple commits.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-shop-project/grade/sp2927" target="_blank">Grading</a></td></tr></table>