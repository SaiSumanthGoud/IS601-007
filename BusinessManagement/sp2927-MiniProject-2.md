<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Sai Sumanth Goud Parakala (sp2927)</td></tr>
<tr><td> <em>Generated: </em> 04/12/2022 23:44:43</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/sp2927" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205521844-e841bac9-85bb-48b2-bebf-664e36f55dfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the index page being displayed from dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205522323-9c44f852-58fb-4bb3-b98b-8f2561ff1e49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of IS601_MP2_Companies table from DB extension of VS Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205522531-167731be-3dd0-4f5a-86c1-05e6cf36a6e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of IS601_MP2_Employees table from DB extension of VS Code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525004-4381991c-98fa-48d3-b0f5-3ff93a32f05f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the code snippet checking for .csv file type<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525145-39441856-224e-4567-8c1d-7cd57a64448d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the code snippet reading CSV file stream as a dictionary and<br>extracting companies, employees data and appending them to the respective arrays.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525346-42ca8c93-12f9-429b-8195-34e22b9a0f01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the code snippet to flash a message noting how many records<br>were processed and also to a flash message when the list is empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205522724-829842de-952b-47d8-9185-d296621c5096.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the flash message rejecting a file which is not of type<br>.CSV<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205522963-3013b0a1-12a0-4b0b-aa02-b2f100d7b862.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing how many successful records are processed on a successful CSV file<br>upload<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205524172-3f58d298-174c-4fb7-b19c-5e8885dda519.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the error message when the form was submitted without a file<br>attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525644-0f5874f1-172e-4ed6-aae1-6100849cef02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some company data uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525690-c51c8358-4205-48a4-8ecc-60152ecccd9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some employee data uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525856-319b48c2-e3a3-4c43-af45-490acb820f8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Code retrieving first_name, last_name, company (id), email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205525959-ffd2f5b6-ae94-4df8-98ca-b50de14f3e00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Code to flash message for all the required fields and setting<br>an empty company to None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205526249-a667afde-b31c-493b-a862-2780be20f957.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the INSERT query and a user friendly flash and print message<br>for an exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205526394-953db2aa-8111-418e-ac8f-02ac7550054f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Employee Form - Filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205528574-42f89d70-4e5e-496d-a564-db945c98ab21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success flash message for adding employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205528826-c1b966cd-0bc8-4ef6-902f-83200d5d4471.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205528983-abd50913-215f-4670-8f98-8982dd023f5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205529080-d0bda94c-4610-47bc-b478-3caeac9e172d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205529497-adccd32a-1959-45e6-a372-05e0089c0578.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>new employee DB record from VS Code highlighting the newly added employee record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205530466-e3e37954-8d0b-4d06-8cba-3f9f9e476b3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query to pull employ id, first_name, last_name, email, company_id, company_name via a<br>LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205530728-680bd3b6-335c-4f60-b4bd-d1bb9cbc251d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>fetching fn, ln, email, company, column, order, limit from request args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205530873-1e656592-d689-41a3-995a-5d2a2c611b51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Like filter for fn, ln and email if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205531061-710a880b-154d-4fa0-8bba-c10ce7029a06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Equality filter for company_id if provided and sorting if column and order are<br>provided and within the allowed columns and order options respectively<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205531336-226ff6cf-8292-46ff-b8ec-60aa69617c95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending limit and providing a proper error message if limit isn&#39;t a number<br>or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205531727-46926007-601d-4d50-bdd3-8aa2b1c541bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user friendly message flashed and print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205532343-f5442e4e-0fc5-408c-bec9-be9fd52a83b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205532475-d36821ee-39d5-4d7d-8e22-d22123ac872a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205532871-30ea4732-b232-4392-a945-6be984cd8244.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205533069-775b030f-9e89-429d-807b-ba2f2e5f3529.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205533268-062b046f-68dc-4ac3-998f-cf5f8fb9c595.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one asc filter applied with column first_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205533430-2103cc38-d573-40c5-8bb1-b5bdd6680622.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one desc filter applied with column last_name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205535065-88ae2215-bf6a-441b-82e5-38345dc09669.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieving id (from request args) and first_name, last_name, company (id), email from<br>form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205535834-4ea893f2-ffd8-431f-88d5-2ed55d57d3f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash messages for first_name, last_name and email. Empty company is set to None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205536732-2a0af738-86c0-438f-8a38-6d3df46ed780.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Query. Proper user friendly flash and print message for it&#39;s exception.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205537403-3791dcf6-b139-4bff-b462-bb2c92fa8c23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT Query and a user friendly flash and print message for it&#39;s exception.<br>Employee data is passed to the wtforms with the help of form.process()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205538818-cd6fd0e1-a18b-46ba-b859-afe700cf043a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee record in the page before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205538983-10f6d614-16b3-48b3-adc1-c840cdeffb47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205539119-66ce97e0-c6e6-4c0a-bb7a-3828a5141008.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205539257-dc9753b1-7120-4a28-8429-5d612f7bd7d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee record in the page after an edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205529497-adccd32a-1959-45e6-a372-05e0089c0578.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of DB data before employee data edit from VS Code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205539615-ca4ebc91-ebca-46a7-b64a-69040bccb6a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of DB data after employee data edit from VS Code <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205540884-0aa84bef-8c44-43e0-a77e-2b1e34a3d2e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code retrieving form data for name, address, city, state, country, zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205540986-7dde4b22-6cae-457f-b048-0503016c8e82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper flash messages for all the required fields. Website is set to None<br>if empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205541314-4970aac3-61ca-4255-a578-afe40e6cd47c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>INSERT Query and a User friendly flash and print message for it&#39;s exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205542174-bb25bc6c-c14f-4107-81ed-4692e97df46e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> filled in valid data in add company prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205542552-4806a6f0-ca6b-4126-a8f6-f557e946133a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message for adding the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205542669-a5e65680-2260-437a-8966-f2e6b5ac56fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205542879-9a7b6e1d-791e-4bc9-aadf-3a85fa8b4511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205542973-8b58e567-bb15-4919-b515-a4115fdbac22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205543092-d17126f2-4cdf-4d84-98c8-4e760c65a57e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205543456-bb7d1665-8d56-49a7-968a-b529ad90d2c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205544056-35f2ece9-8779-41eb-a2dd-01db2329e6df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of new company DB record from VS Code with valid company data<br>shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205544811-9ec31a39-3a91-4896-aff7-b93f65e39e7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query fetching id, name, address, city, country, state, zip, website, employee count<br>for the company. Note: Highlighted the required query part as it is divided<br>and written at two places <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205544970-d5f1ce21-248f-4d50-988f-7394c40e1859.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Fetching name, country, state, column, order, limit from request args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205545125-3c153ec9-7bb0-427e-9071-c5226a3ed7bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Like filter for name. Equality filter for country and state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205545523-199855ac-1909-486f-8eb0-4586bf9f2349.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Sorting if column and order are provided and within the allows columns<br>and allowed order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205545701-590d811c-3027-4d0a-b9e9-eab6c05eb62c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending limit and providing a proper error message if limit isn&#39;t a number<br>or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205545955-472fc9b5-045f-48fd-a638-6e6054cbf7df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Print and flash messages for the select query<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205546674-77bf37bb-51ee-4efc-a5aa-a79f083078c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205546849-0f5c6256-5aaa-41de-b4fd-0790ad041219.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205546949-3d340b3d-9bdc-4eeb-8093-67e7a02b522a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205547069-b9155ad3-92e8-4a48-84cc-65fc1c30bc1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one asc filter applied with name column chosen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205547313-4e4ae23e-479e-4668-835e-0e5b09623545.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one desc filter applied with name column chosen<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205547539-ff4e889e-c95d-4aab-a213-d7b12ce7951f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieving id (from request args) name, address, city, state, country, zip, website<br>from form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205547678-81e1a33e-d02c-464f-b200-bc0dd0035900.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash messages for all the required fields and Webiste is set to None<br>if empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205547925-af666a78-7336-493f-bd68-183d997fd265.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UPDATE Query. Proper flash and print message for it&#39;s exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205548424-bb45d388-8f18-4e93-81e4-d4c16cf83ec1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT Query. Proper flash and print message for it&#39;s exception. Company data is<br>passed to wtforms with form.process(). Remaining state and country is passed through render<br>template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205548698-8f22ea7b-32e2-4717-a714-cd64f1f3ef99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page showing company data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205548994-e2e26edb-ef2b-4d60-9da8-60172881df2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205549127-d95cb605-4acc-48e0-a60b-d515be9379bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205549222-1dc8eb0e-e04a-46d6-80a8-a354911ca634.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page showing company data after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205548852-44dd8457-84a4-4824-a7d3-cc70c77ec09a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data before company data edit from VS Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205549336-899ca200-f12a-4d92-841b-50efb8ab10c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data after company data edit from VS Code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205549479-7711e509-284d-4155-b0f2-9946362b7515.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Query to delete by id. Redirected to employee search. All request args<br>(minus id) are passed to the redirect route. Flash message for successful deletion<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550054-87062b28-02c7-4698-8107-3419769686ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before deleting an employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550103-e45c17a7-9127-4bb4-8a54-ecd1492372f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after deleting an employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550205-421467f5-b16d-4bcf-9b80-1e83388b2bd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Query to delete by id. Redirected to company search. All request args<br>(minus id) are passed to the redirect route. Flash message for successful deletion<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550303-f2d21b86-3fc3-45b7-b97f-b48bf45c1be2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550385-1b86357e-3b4e-4ddf-9d8e-04f595036d8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after deleting a company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550580-e9f65ea8-4340-4130-8569-632cb5ab9bde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test cases passing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/205550655-89ab28b5-7f93-4cbd-bb0c-992f85e3a887.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test cases passing from console<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I have learned how to handle GET and POST calls to perform actions<br>like add, edit, sort, and delete. Learned how to use wtforms and pass<br>arguments to it. Learned to write SQL queries in a pythonic way. Learned<br>to handle a data(CSV) file and parse it. Learned to handle exceptions and<br>flash massages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/sp2927" target="_blank">Grading</a></td></tr></table>