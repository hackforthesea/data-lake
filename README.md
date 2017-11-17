# Hack for the Sea Data Lake

> Repository for Hack for the Sea data. Sponsored by [Microshare](https://microshare.io).

## Installation / Getting Started

Coming soon

## Usage

This document assumes you are working with a web application or a medium that supports HTTP.

Instructions for embedded hardware code and CLI tools coming soon.

### I. Register a new Hack for the Sea Application

The Data Lake requires oAuth to use. Here's how to get credentials

1. Register a new Hack for the Sea account at http://hackforthesea.tech/accounts/register
2. For now, please email mark@mrh.io to activate your account.
3. Once your account is activated, log in and you will be redirected to https://hackforthesea.tech/oauth/applications/
4. Create a new application with the following values.
   * **Name:** Choose your own name of your application i.e. _Bathymetry Explorer_
   * **Client id:** Leave as is
   * **Client secret:** Leave as is
   * **Client type** Select _Confidential_ for now.
   * **Authorization grant type**: Select _Authorization Code_ for now.
   * **Redirect uris** The URL that you wish to be redirected back to after authentication is complete. Typically the URL of your application itself.
   
### II. Authenticate Your Application

jQuery Example:
```
function getCookie(name)
  {
    var re = new RegExp(name + "=([^;]+)");
    var value = re.exec(document.cookie);
    return (value != null) ? unescape(value[1]) : null;
  }

$.ajax({
  url: "https://hackforthesea.tech/oauth/token/",
  method: "POST",
  data: {
    csrfmiddlewaretoken: getCookie('csrftoken'),
    grant_type: "authorization_code",
    code: "AUTH_CODE_FROM_PREVIOUS_STEP",
    client_id: "YOUR_CLIENT_ID",
    client_secret: "YOUR_CLIENT_SECRET",
    redirect_uri: "REDIRECT_URI_MUST_MATCH_YOUR_APP"
  }
})
```

## Maintainers

Mark Henderson
Sponsored by http://microshare.io

## Contribute

The best thing you can do to contribute to the data lake is to **put data into it!* That means following the example set in the [Usage](#usage) section to create an app and send data to it.

## License

Coming Soon
