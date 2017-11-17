# Hack for the Sea Data Lake

> Repository for Hack for the Sea data. Sponsored by [Microshare](https://microshare.io).

## Installation / Getting Started

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
```javascript
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

## Use the Data Lake!

Here are some jQuery AJAX requests that work.

GET:
```javascript
// List
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals?access_token=[ACCESS_TOKEN]"
});

/******
Available query string params for list view
- details: boolean
  Will return matching objects with their details, false will only return main information

- page: int
  Specifies the requested page, defaults to 1

- perPage int
  Specifies the number of objects to be returned per page, defaults to 999

- sort: string
  Specifies if sorting needs to be applied and to which field in the data
********/

// Detail
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/5a0e304946e0fb0022f6f40d?access_token=[ACCESS_TOKEN]"
});
```

POST:
```javascript
$.ajax({
  type: "POST",
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals?access_token=[ACCESS_TOKEN]",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({ hellp: "world" })
});
```

DELETE:
```javascript
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/5a0e315b46e0fb002866b437?access_token=[ACCESS_TOKEN]",
  type: "DELETE"
});
```

## Maintainers

Mark Henderson
Sponsored by http://microshare.io

## Contribute

The best thing you can do to contribute to the data lake is to **put data into it!* That means following the example set in the [Usage](#usage) section to create an app and send data to it.

## License

Coming Soon
