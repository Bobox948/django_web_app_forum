# django_web_app_forum

My project is a "Calisthenics Forum" where the users can register and then make new threads asking questions to other users. Along with the question, the user can also provide an image attachment to be more precise. Other users can reply to this thread to give some answers.

Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.

I believe my project satisfies the distinctiveness and complexity requirements mentioned in the rules because I had to make a lot more addtionnal research for features. For instance, I wanted users to be able to upload their own images from their computer not from an internet link (models.ImageField in the model). For that I found the python libraby pillow, I installed it and I managed to make this happen after a few tries and debugging phases. Also, I had to do a lot of research about django templates, like for example how to display "x minutes ago" instead of the datefield for the latest forum posts, and more importantly how to display a ForeignKey field count in the template (for number of posts in each thread). I also made possible for the user to modify his "account settings" adding a profile picture, specifying his birth date etc, and he can do this multiple times, each time erasing the previous input in the model. I managed to find how to display the user's last login to the website, because in a Forum this is an interresting feature, along with the date of the account creation (via auto_now_add=True in the datefield). In the models, I've replaced the charfield fields which are limited to 254 chars by TextField fields. For the style, I had to find how to be totaly mobile responsive and for that I had to put a @media in the css style for this special case (with max width parameter of 600).

What’s contained in each file you created.

finalproject/static/images/ : This is the folder where the uploaded images by the users go (for their profile picture). Also there is some default images like the default N/A profile picture, the attachment icon and the star rating for the most active users in the forum.

finalproject/forum/ ->

myjs.js : There you can find the reply, save and close functions, with some DOM manipulation (not needing to refresh the page to see the changes).

styles.css : All the style of the web app, from full screen on computer to mobile device.

account.html : This is the page with the form to add informations to your account (date of birth, origin, profile picture, gender and bio/about).

index.html : The index page where all the Threads of the forum are block displayed.

layout.html : The layout document for the structure (header, navbar, footer).

login.html : The login page.

new.html : The "new thread" page with a form to create a new thread (login required).

profile.html : The page that displays the profile of the user.

register.html : Page for registering.

search.html : Page to display the results of the searchbar if the matching isn't directly found.

thread.html : The page of each thread, with the reply posts.

And of course models.py where you can find the models with relations and urls.py where you can find the paths.

How to run your application.

You run my application with -> python (or python3) manage.py runserver, making sure to makemigrations before and to migrate, and enjoy, it's an Django web app so it's running like all the applications we've seen so far in the class.

Any other additional information the staff should know about your project.

I already specified this in the requirements.txt file in the root but I've added the python library Pillow tu allow the user to upload local images. https://pillow.readthedocs.io/en/stable/reference/index.html
