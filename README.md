# Hack for the Sea Data Lake

> Repository for Hack for the Sea data. Sponsored by [Microshare](https://microshare.io).

## Table of Contents

* [Installation / Getting Started](#installation--getting-started)
  * [I. Register a new Hack for the Sea Application](#i-register-a-new-hack-for-the-sea-application)
  * [II. Construct an Authorization URL and Obtain an Authorization Code](#ii-construct-an-authorization-url-and-obtain-an-authorization-code)
  * [III. Authenticate Your Application](#iii-authenticate-your-application)
* [Usage](#usage)
* [Data Lake Schema](#data-lake-schema)
* [Maintainers](#maintainers)
* [Contribute](#contribute)
* [License](#license)

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

### II. Construct an Authorization URL and Obtain an Authorization Code

1. Visit this URL: https://hackforthesea.tech/oauth/authorize/?response_type=code&state=random_state_string&client_id=[YOUR_CLIENT_ID], substituting YOUR_CLIENT_ID with the client ID of the application you created.
2. Review the permissions requested by the application, and click "Approve"
3. You will then be redirected to your applications Redirect URI, which will have a "code" parameter, like this: https://[REDIRECT_URI]/?state=random_state_string&code=j7SAsPilPPIWHmJ05tiEd02t4hWQAJ

### III. Authenticate Your Application

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

## Usage

Here are some jQuery AJAX requests that work.

### Listing and Retrieving Data
```javascript
// List
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals?access_token=[ACCESS_TOKEN]"
});

// List with tags - as many as you want
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/tags/tag1/tag2/etc?access_token=[ACCESS_TOKEN]"
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

### Posting Data
```javascript
$.ajax({
  type: "POST",
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals?access_token=[ACCESS_TOKEN]",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({ hellp: "world" })
});

// With tags
$.ajax({
  type: "POST",
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/tags/tag1/tag2/etc?access_token=[ACCESS_TOKEN]",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({ hellp: "world" })
});
```

### Deleting Data
```javascript
$.ajax({
  url: "https://hackforthesea-aphelionz.c9users.io/data/com.hackforthesea.globals/5a0e315b46e0fb002866b437?access_token=[ACCESS_TOKEN]",
  type: "DELETE"
});
```

## Data Lake Schema

Objects in the data lake are stored in dot-notated keys, all beginning with `com.hackforthesea`. There are global objects, and project-spefific keys. The global objects are enumerated below, with links out to the individual projects as they are appropriate. Note that keys are **singular** - location, beach, animal, etc.

`com.hackforthesea.global.location` - Terrestrial locations with geodata included. Currently beaches in MA.

## Maintainers

* Mark Henderson (mark@mrh.io)
* Sponsored by http://microshare.io

## Contribute

The best thing you can do to contribute to the data lake is to **put data into it!** That means following the example set in the [Usage](#usage) section to create an app and send data to it.

## License

Coming Soon
