# python-emailer

A small script to send dog pictures to myself every hour via email.

## E-Mail Sample

![image](https://user-images.githubusercontent.com/47525983/101314776-44ba6380-387f-11eb-8913-a22669a7f497.png)

## Automated with Github Actions

The email.yml file builds a python 3.8 environment and runs the emailer.py script to send out dog pictures every hour.

## API Used
Dog pictures are fetched from the following API.

[The dog API](https://dog.ceo/dog-api/)

[Github Repo for dog API](https://github.com/ElliottLandsborough/dog-ceo-api)

## Planned Improvements

- [ ] Open up email list to public
- [ ] Create workflow to add email from pull request to email list.

## Contributing

If you can help with any of the tasks in the Planned Improvements section (they are also open issues) feel free to make a pull request with your code.

## Set up

### Google Set up

Go to the following link to set up an app password for your google account.

[Link](https://myaccount.google.com/apppasswords)

You may have to set up 2FA if you have not already (Two factor authentication is highly recommended. Not everyone on the Internet wants to send you dog pictures every hour, some people want your bank details).

### Repository Set up
1. Clone the repository

    `$ git clone https://github.com/tintindas/python-emailer.git`

1. Navigate into directory

    `$ cd python-emailer`

1. Set up Python virtual environment

    `$ python3 -m venv .venv`
  
    .venv is what I usually name my virtual environment folder. 

1. Activate environment
  
    `$ source .venv/bin/activate`

1. Install dependencies
  
    `$ pip install -r requirements.txt`

 1. Edit email list
 
 Edit the line below. Reset the array with your email addresses.
 
 [`msg['To'] = ['upamanyudas16@gmail.com', to_email]`](https://github.com/tintindas/python-emailer/blob/574924b646a8fdcbe13043bed32374f4136a9be4/emailer.py#L44)
 
 1. Run script
 
 `$ python emailer.py`
