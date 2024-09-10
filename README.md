# Building a Course Platform

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