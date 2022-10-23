<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Sai Sumanth Goud Parakala (sp2927)</td></tr>
<tr><td> <em>Generated: </em> 23/10/2022 15:41:35</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/sp2927" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197398777-411ecf73-17ab-4678-80af-0a92b8d37336.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the updated method calculate_cost()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197398961-c8325835-ccee-43f9-8b87-f9a9706ce299.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the input() message displaying the value in currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ul><li>I have iterated through the inprogress_icecream array(which contains the list of choices) to<br>add up the cost of each choice and stored the sum in a<br>variable "cost".</li><li>The cost is formatted to the currency format while returning the value<br>with the help of the format() function.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197400960-a3a8a0ca-6450-49e9-8062-c8bdeb71badf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the OutOfStockException is handled with proper user feedback and continued program<br>flow<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197402711-bd7789c3-c660-4e56-b3fd-c45b9cfe0ec0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the NeedsCleaningException is handled with proper user feedback and continued program<br>flow. New input() process is highlighted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197403263-19c673c6-6659-4cb8-98c5-a3d353fe50c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the various InvalidChoiceExceptions are handled with proper user feedback and continued<br>program flow<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197402342-8fc1cd4c-6f90-4ea8-95d2-393b8e0a6371.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the ExceededRemainingChoicesExceptions is handled for toppings with proper user feedback and<br>continued program flow<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197402393-d2399991-b3e8-4609-b2a9-7033a51c4944.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the ExceededRemainingChoicesExceptions is handled for flavors with proper user feedback and<br>continued program flow<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197402521-227b0ab4-9ea6-479d-b57f-0ec85cd8d5f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the InvalidPaymentException is handled with proper user feedback and continued program<br>flow<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ul><li><span style="font-size: 13px;">OutOfStockException is handled by printing a statement that the choice is<br>out of stock and to choose from the available options shown.</span><br></li><li><span style="font-size: 13px;">NeedsCleaningException<br>is handled by letting the user know that "the machine has reached its<br>maximum usage and it needs cleaning before any more ice creams can be<br>made. The user is also asked to confirm if he/she would like to<br>proceed with the cleaning and then continue selecting or else quit.</span></li><li><span style="font-size: 13px;">InvalidChoiceException<br>is handled by&nbsp;prompting the users that their choice is invalid, choose only from<br>the options show below.</span></li><li><span style="font-size: 13px;">ExceededRemainingChoicesExceptions is handled by prompting that the maximum<br>remaining choices has reached, now proceed to the next step. The user will<br>also be moved to the next following step( either topping or pay)<br></span></li><li><span style="font-size:<br>13px;">InvalidPaymentException is handled by prompting that "the amount entered didn't match with the<br>total, please re-enter".&nbsp;<br></span></li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197405612-824fe9e0-87af-4f51-bb0f-d4d514037b31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if container is the first selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197405838-d285d006-b450-4391-af38-fe1f58fead98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if we can only add flavors if they&#39;re in<br>stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197405898-2357c1e7-c84f-4f8c-9d4e-6a2bd29db7b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if we can only add toppings if they&#39;re in<br>stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197406025-52543cd5-ad56-4cdc-9e56-9b7fabb7b640.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if we can add up to maximum allowed number<br>of flavors/scoops<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197406187-742a4a24-1c78-4582-a929-fdc6a3179965.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if we can add up to maximum allowed number<br>of toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197406213-89e23ef6-6cfb-4b6f-a2b3-a09de18bbf62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if cost is calculated properly based on the choices.<br>The calculated cost is matched with the currency format of the actual cost<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197407266-9b4de624-9edd-473d-8b75-48fafbddd5f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if total sales is calculated properly<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197407616-770f0b17-ba7a-4944-bc62-644609f697ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case to check if total ice creams is properly incremented for each<br>purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197407723-7a0fe0a5-59b3-4d89-b12e-c5afa4fc6402.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <ul><li>Test 1 -&nbsp; checking if the value of currently_selecting is "Container" in the<br>first selection.</li><li>Test 2 - testing if a flavor quantity is equal to -1(out<br>of stock) when the flavor is out of stock.</li><li>Test 3 - testing if<br>a topping quantity is equal to -1(out of stock) when the topping&nbsp;is out<br>of stock.</li><li>Test 4 - testing if the remaining_scoops is equal to 0 when<br>the maximum number of scoops is chosen.</li><li>Test 5 - testing if the remaining_toppings<br>is equal to 0 when the maximum number of toppings is chosen.<br></li><li>Test 6<br>- testing if the cost is calculated properly based on the choices. The<br>calculated cost is matched with the currency format of the actual cost to<br>test formatting.</li><li>Test 7 -&nbsp;testing if&nbsp;the&nbsp;total_sales&nbsp;is calculated properly by matching it with the sum<br>of individual ice cream costs.<br></li><li>Test 8 - testing if&nbsp;the total_icecreams is properly incremented<br>for each purchase by comparing it with the expected value.<br></li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiSumanthGoud/IS601-007/pull/4">https://github.com/SaiSumanthGoud/IS601-007/pull/4</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ul><li>Was facing issues while trying to handle exceptions in the IcecreamExceptions.py file but<br>then figured out that the exceptions have to be handled directly in the<br>code where the exceptions occur.</li><li>Faced a calculation error in the testing file due<br>to a state issue. Resolved it by resetting the state with the reset()<br>function.</li><li>&nbsp;Learned how to handle exceptions and write test cases in python.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197412227-3e18649e-e5eb-4e6b-b2e1-aa214496564b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful program execution showcasing InvalidChoiceException and InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197413238-d11e1040-1d48-42a4-bda3-448982d3d114.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful program execution showcasing ExceededRemainingChoicesException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113568928/197413898-6401300f-b1f3-4f8a-bb6e-6e6ad0d86224.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful program execution.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/sp2927" target="_blank">Grading</a></td></tr></table>
