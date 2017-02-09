Title: Proposed scheme for per-user database field encryption.
Date: 2011-06-17 16:06
Author: slacy
Category: General
Status: published

I've been thinking a lot about hackers, stolenpasswords, rainbow tables,
and credit card numbers in databases.

But, the question remains:  "**How should I store credit card numbers in
a database for maximum user security?**"

Typically, user authentication for web sites looks like this:

1.  User types username & password into text box on a web page.
2.  username & password and sent (ideally, via https) to the web server.
3.  The server hashes the password with a known secret (salt) to
    generate a password hash.
4.  The server compares the password hash the same hash value stored in
    the database.  If successful, a random session ID is generated and
    sent back to the client as an HTTP header, as well as stored in a
    local store for referencing in future requests.

<span style="font-size: small;">Key points:  Plain text passwords aren't
stored in the database.  Passwords are never sent unencrypted (if using
https) and session ID's are "unguessable" because they're randomly
chosen from a large space.</span>

<span style="font-size: small;">If your web application needs to store
sensitive user information, like credit card numbers, how should you do
it?  I propose using per-user encryption keys that are based on a salted
hash of the plain-text password.</span>

<span style="font-size: small;">How do you compute the correct keys and,
where should you store them?  One possibility is to use another secure
hash of the user's plain text password and some *other* salt value
that's not the same as the one used for password checking.   Let's call
the resultant value our *user encryption key*.  It should **never** be
stored in persistent storage, but should be sent back to the user as an
HTTP header.</span>

<span style="font-size: small;">The user, with every request, will then
be sending to the server a random session ID as well as their current
*user encryption key* value.  The *user encryption key* would be used
with a symmetric encryption algorithm to store any sensitive database
values.  (Home address, credit card numbers, other site credentials,
etc.)  When the user changes their password, then the encrypted database
fields need to be re-encrypted with their new values.</span>

<span style="font-size: small;">As the developer of the server software,
you need to be extra careful to only store unencrypted sensitive
information in RAM, and only use it for the minimum duration possible.  
For example, it would be difficult to impossible to implement offline
billing with such a system in place.</span>

<span style="font-size: small;">With this scheme in place, your
customer's data will be completely secure, even if your server is hacked
and even if your entire database replicated.  Even if the hackers had
access to your source code, they could, at most, get the unencrypted
data for users who were currently visiting the site (through net
sniffing the user encryption key values) or from users whose PCs have
been compromised.   That feels pretty secure to me.</span>

<span style="font-size: small;">The resultant flow for user sign-in
looks like this:</span>

1.  <span style="font-size: small;">Receive plaintext username and
    password</span>
2.  <span style="font-size: small;">Hash password with "password salt"
    and check against stored value for user authentication and
    session generation.</span>
3.  <span style="font-size: small;">Hash password with "user key salt"
    and set an HTTP header with this value as the user
    encryption key.</span>
4.  <span style="font-size: small;">When user reads or writes sensitive
    information, encrypt/decrypt it with the user encryption key.</span>
5.  <span style="font-size: small;">Never store decrypted values in
    persistent storage. (some asynchronous task queues may violate this
    constraint, so be careful)</span>

