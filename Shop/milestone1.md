<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Sai Sumanth Goud Parakala (sp2927)</td></tr>
<tr><td> <em>Generated: </em> 11/12/2022 23:22:42</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/sp2927" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920291-096bbe53-f9bc-404a-abc4-12412b252fce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing invalid email and password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920350-4f94b43d-38c7-47a6-840a-14fbd802270b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing passwords do not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920588-305dfa19-ef5c-4b60-8eda-11925c6d279f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920689-4156ee1c-9dfd-4c1a-b725-4b79b26a8d7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920921-df5faede-8d87-4b9a-ab28-dad9e1bfbfdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the form with valid data filled in before the form is<br>submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206921012-2464e6b6-889f-42b2-ba3d-b8138e39080a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the valid user data from Task 1. Clearly highlighted which row<br>it is.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/24">https://github.com/SaiSumanthGoud/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><li>Form is handled with wtforms and each field has its own validation. The<br>form can only be submitted successfully once all the fields have met the<br>requirement.</li><li>Validation is done with the help wtforms validators which work for both frontend<br>and backend. The following validators are used:&nbsp; DataRequired() is used to mark the<br>field as required, EqualTo() is used to check if the password and confirm-password<br>match and Email() is used to check for valid email format. Username is<br>checked to match "^[a-z0-9_-]{2,30}$" this regex. Duplicate username and email values are checked<br>during the inserting into the database. A flash message is populated for a<br>duplicate entry exception.</li><li>Password is hashed with bcrypt and then saved into the database.</li><li>All<br>the form data is saved in the users table&nbsp; which is created in<br>the database along with the created and modified timestamp.<br></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206929814-55ddcbb3-422c-47cc-8a0e-4a87fe7f5164.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206929880-e39134e2-7d54-4181-852c-ffb0554d26b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing non-existing user validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206930260-2c8c975c-29bf-4624-9210-1281b35641ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/25">https://github.com/SaiSumanthGoud/IS601-007/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><li>Form is handled with wtforms and each field has its own validation. The<br>form can only be submitted successfully once all the fields have met the<br>requirement.</li><li>Validation is done with the help wtforms validators which work for both front-end<br>and back-end.&nbsp; The "Email or Username" field accepts either email or username and<br>is validated based on the input. If the username or email is not<br>present in the database then a flash message saying "Invalid User" is displayed.<br>If the username&nbsp; matches but not the password then a flash message saying<br>"Invalid Password" is displayed</li><li>Password entered is matched with the hashed password which is<br>already present in the database. A function bcrypt.check_password_hash() does this matching with the<br>help of salt value.</li><li>Both password and email or username are matched with the<br>tuples in the database from users table which holds the data while registering.</li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206932440-83dbe371-50c8-4445-ab4f-ef588cdeaf67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206932522-ebdc3ae0-519e-4749-8c28-ed6cf7dab6b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/25">https://github.com/SaiSumanthGoud/IS601-007/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>When the user logs in, the User object is stored in the session.<br>When the page reloads, that User object in the session is used to<br>authenticate instead of calling the database. Which helps in avoiding the overhead. If<br>the User object is not present in the session then it loads from<br>the database.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939528-56eb60b9-4c28-40a8-9138-466d9daf6669.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939633-e729c688-51ce-4b33-865c-1feb760a220f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing a user without an appropriate role can&#39;t access the role-protected<br>page Checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939727-51a2ef63-f9e3-4477-a570-d3e899b23443.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939811-b724d679-3232-487f-88db-667a82e2d10d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the UserRoles table with valid data. My admin user is a<br>user with username &quot;admin&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/26">https://github.com/SaiSumanthGoud/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Login-protected pages are protected with the @login_required decorator provided by flask_login. This triggers<br>the user_loader for each page request. The user will be loaded from the<br>session if exists to avoid repeated database calls. If not present in the<br>session then it loads from the database.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Role-protected pages are protected with the help of flask_principal. We define permission with<br>the role needed for it. This permission can be imposed on the desired<br>pages by prepending it with the permission decorators. The identity is loaded into<br>the session with the user name and authentication type.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206941849-fbc2b35b-ede7-4e18-a275-405328050f9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing styles navigation and register form. All the forms follow the same<br>theme<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206942008-a63f0a74-7ec1-47d2-bf41-f04afb24b527.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing styles of tables<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/26">https://github.com/SaiSumanthGoud/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>I have followed a dark theme for the website. Chose a sample Navigation<br>from the bootstrap where the login, register, and log out will be to<br>the right extreme separated from the main nav. Have chosen a card layout<br>for all the forms with limited width so that the text fields will<br>be within the required length. Have given some inline styles to order the<br>filter and apply the roles layout. Applied custom colors through inline styling<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939633-e729c688-51ce-4b33-865c-1feb760a220f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing a user without an appropriate role can&#39;t access the role-protected<br>page Checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206939528-56eb60b9-4c28-40a8-9138-466d9daf6669.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206920588-305dfa19-ef5c-4b60-8eda-11925c6d279f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206943068-e5aff7c0-6099-4cfa-b70b-5e10f2fed5fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing page not found for loading non existing pages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/26">https://github.com/SaiSumanthGoud/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>For the HTTP server error messages like 401, 403, and 404 I have<br>created separate pages with custom and user-friendly messages being displayed. If any of<br>those errors occur it will be redirected to render its respective HTML page.<br>For duplicate entry exceptions which occur for username or email, I extracted the<br>field name from the exception message and displayed a flash message that it<br>is not available.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206949496-e7782e01-497e-4566-aff0-1f8dbca5a620.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the User Profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/26">https://github.com/SaiSumanthGoud/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>When the profile page is loaded, the user id is fetched from the<br>current_user. With that user id email and username of that user is fetched<br>from the database and is populated to the respective fields.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206951322-6bbf0f15-c944-4fa9-9b65-ce500cc0bede.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the username and email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206952116-39468a52-a7a1-4057-ad1c-1e7620713234.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206952440-75688cf3-02c9-43eb-80df-4a7836a30ff3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206952676-5f94479b-4237-4156-b192-5901a54fb08d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the chosen username is not available validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206952989-18ea5307-9cc1-452d-8e28-4d9b2b039e1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the chosen email is not available validation message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206953977-c0732aa7-7341-4b29-a651-4cbc2df89eb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the Users table before editing profile. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/206954288-d2a67441-b0ee-417f-ab95-584cdc345687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username &quot;john&quot; is updated to &quot;john-updated&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/26">https://github.com/SaiSumanthGoud/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The username and email fields are updated for each update request. Before updating<br>the username and email values, they checked if they match the required respective<br>format. If yes then it checks if either of the values are already<br>being used by other users in the database. If yes, then a flash<br>message is populated that the respective value is not available for use. For<br>updating the password, we check if the new password match with confirm password<br>and then check if the current password is the same as the existing<br>password in the database. If these conditions are satisfied then the password is<br>updated.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><li>I have faced "jinja2.exceptions.UndefinedError: 'flask_login.mixins.AnonymousUserMixin object' has no attribute 'has_role'" this error while<br>checking for the user role to populate user-specific navigation link for admin. Figured<br>out that it is being caused as I was checking for the current<br>user before checking if the user is authenticated. Resolved it by adding an<br>authentication check&nbsp; before checking the role.&nbsp;</li><li>Tried to send the user object to the<br>wtforms with form.process() to populate, but realized that the User object cannot be<br>iterated. So reverted it to the convention assigning approach.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2927-prod-2.herokuapp.com/">https://is601-sp2927-prod-2.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/sp2927" target="_blank">Grading</a></td></tr></table>