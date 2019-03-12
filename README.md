# Assingment 5: Creating and polling a website
This assignment trains you in:

1. installing and using a new Python framework
2. running Python code from the terminal
3. scrape web requests

The code in this assignment is based on the requests module and the flask framework (see links). Don't forget to use Python 3 for the assignment. Scary things might happen if you don't

## Part 1: Writing a server
The first part of the assignment is to write a very simple server. It needs to do three things:

1. Expose an HTTP POST method at /, that accepts and decodes a JSON data body. That is the only method you have to expose.
2. Get the request JSON data (using request.get_json()) and assume it's a dictionary. Now extract the value inside the dictionary under the key password. We will call this password for client_password.
3. Choose a two-letter password (in ASCII) that is fixed for the server. Just choose two random letters/numbers. We will call this password SERVER_PASSWORD. If the decoded value for the password field is the same as your chosen password (client_password == SERVER_PASSWORD), return an HTTP code 200 OK. Otherwise return the HTTP code 403 Forbidden status code. You don't have to return a body.

Hand in:

- The code for your server copied into a Jupyter Notebook
    - This should not be much more than 20 lines of code

## Part 2: Hack the server!
Now we want to hack the server. But not just hack it once. We want to automate hacking the server! Before you start on this part, make sure your server from part 1 is running.

1. Find a list of all the possible ASCII characters in Python (hint: look in the string module)
2. Generate all possible combinations of two ASCII characters and save them into the variable `
    - This will be 52 * 52 = 2704 elements. If you're smart you can create this as a generator
3. Write a method that takes a string password as its input, calls your server from part 1 (running on localhost), and return the status code of the request. Make sure that you:
    - Call the website at the correct port and URL with the correct HTTP verb
    - Inject data correctly. Remember that the body should be a str containing a JSON dictionary
4. Use your list of combinations from step 2 to call the sever 2704 times and find out when the status code it 200. When that happened you cracked the code!

Hand in:

- The code for your hack in your Jupyter Notebook
- The password you found

## Part 3 (optional): Make it go fast!
This was probably pretty slow, because we made ~2704 sequential requests. Now implement this asynchronously by using a pool like this:
``` python
from multiprocessing import Pool
pool = Pool(processes=12)
```

Hand in:

- The code for parallelising your server hacking
- The runtimes of the sequential and parallel version using %%timeit
- A line of code explaining what happened. Was it faster? If so, why? Was it slower or the same? If so, why?
