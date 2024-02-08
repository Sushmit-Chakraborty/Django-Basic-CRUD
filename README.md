# Django-Basic-CRUD
Basic CRUD functionality using django

Implemented this project to review the basics of django.

Project contains a post model containing a title and content fields. The following url functionalities are present - 

1) /posts/create -> Create a post
2) /posts/view -> View all of your posts
3) /posts/update/**<id>** -> Update your post (**<id>** refers to the primary key of your post e.g:- If you want to update the post having primary key '2' you would hit the URL "/posts/update/2" and provide the new title and content field and your post will be updated)
4) /posts/delete/**<id>** -> Delete your post (**<id>** refers to the primary key of the post you want to delete)
