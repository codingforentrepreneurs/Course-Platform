# Building a Course Platform

Watch the tutorial [here](https://youtu.be/I_IchaIdmnA)

## Tech Stack

Tech Stack:

- [Django](https://djangoproject.com) v5.1
- [Python](https://python.org) v3.12 
- [HTMX](https://htmx.org)
- [django-htmx](https://github.com/adamchainz/django-htmx)
- [tailwind](https://tailwindcss.com)
- [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)
- [Flowbite](https://flowbite.com)
- [Cloudinary](https://cld.media/cfe)

## Overview
What we are building

- Courses:
	- Title
	- Description
	- Thumbnail/Image
	- Access:
		- Anyone
		- Email required
        - Purchase required
		- User required (n/a)
	- Status: 
		- Published
		- Coming Soon
		- Draft
	- Lessons
		- Title
		- Description
		- Video
		- Status: Published, Coming Soon, Draft


- Email verification for short-lived access
	- Views:
		- Collect user email
		- Verify user email
			- Activate session
	- Models:
		- Email
		- EmailVerificationToken
