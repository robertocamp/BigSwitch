BigSwitch API documentation.

1. authentication

2. settings
3. session
3. "bcf.ops"
4. deployment file
5. data file


1.  authentication

Authentication to the BigSwitch API in this project is done via username and password.
Access to the BigSwitch API will be done via a local account that is configured on the controller.
This account may or may not be the 'admin' account. 

testing authentication: run the bcf_session.py file

2. settings

The settings file is currently named after the active POD.
The setting file contains:
* pod name
* an encryption function that pulls an encrypted password from a password store.
(The password encryption mechanism is beyond the scope of this repo)
* POD base url ( the API uses port 8443)
* API username



3. session

A "session" to the BigSwitch API is achieved by passing accepted logon credentials to the API and getting a session token back
You can use the access-token command to create a long-lived token that can be used for authentication with external scripting,
such as RESTful API. The access token value returned by the CLI command is used in place of the session cookie that is typically generated when a user completes a login process.

In this repo, session cookie is created by calling 'bcf_sesion' function from the 'bcf_session.py' file.

To test:
python bcf_session.py 

should return an access token.

3. bcf.ops

bcf_ops.py ('bcf' in code) is Python script which defines various methods and fucntions for connecting to the BigSwitch API

4. deployment file
5. data file

