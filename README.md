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

The password can be stored and encrypted using the Imp Common "encrypt" function.  This code is now included in this project ( see "settings" section)

2. settings



3. session

a "session" to the BigSwitch API is achieved by passing accepted logon credentials to the API and getting a session token back
You can use the access-token command to create a long-lived token that can be used for authentication with external scripting,
such as RESTful API. The access token value returned by the CLI command is used in place of the session cookie that is typically generated when a user completes a login process.

3. bcf.ops

bcf_ops.py ('bcf' in code) is Python script which defines various methods and fucntions for connecting to the BigSwitch API

4. deployment file
5. data file

Appendix:

clone branch:
git clone -b robert_27_sept_imp_common_encrypt_password --single-branch https://sfgitlab.opr.statefarm.org/cloud9/BigSwitch.git
git clone -b Robert_29_sept_caas_interface_group --single-branch https://sfgitlab.opr.statefarm.org/cloud9/BigSwitch.git



