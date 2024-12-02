# Instructions for running application
1. Navigate to Project folder
2. Build a docker image
    * `docker build --tag python-docker .`
    * `docker images`
3. Run the docker image to start project
    * `docker run <image ID>`
    * `docker run -p 5000:5000 python-docker`
4. Get started with CRUD operations in client at localhost:5000 or with the following CURL commands:
* SET: `curl -X POST http://127.0.0.1:5000/set_element -d "namespace=param1&key=param2&value=param3"`
* GET: `curl -X POST http://127.0.0.1:5000/get_element -d "namespace=param1&key=param2"`
* DELETE: `curl -X POST http://127.0.0.1:5000/delete_element -d "namespace=param1&key=param2"`
* COUNT: `curl -X POST http://127.0.0.1:5000/count_element -d "namespace=param1&value=param2"`
* COUNT GLOBAL: `curl -X POST http://127.0.0.1:5000/count_global_element -d "value=param1"`

# CURL command examples
## Scenario 1
```
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=a&key=b&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=z&key=b&value=d"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/get_element -d "namespace=a&key=b"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Namespace: a </text>
        <br>
        <br>

        <center> <text> Key: b </text>
        <br>
        <br>

        <center> <text> Value: c </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/get_element -d "namespace=z&key=b"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Namespace: z </text>
        <br>
        <br>

        <center> <text> Key: b </text>
        <br>
        <br>

        <center> <text> Value: d </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/delete_element -d "namespace=a&key=b"
<!DOCTYPE html>

<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been deleted! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/get_element -d "namespace=a&key=b"
<!DOCTYPE html>
<html>

    <head>
        <meta charset="multipart/form-data">
        <title> CRUD App </title>
    </head>

    <style>
        html {
            color: white;
            background-color: black;
        }

        text {
            font-size: 24px;
        }
    </style>

    <body>

        <center> <h1>CRUD Application</h1> </center>
        <center> <text>Dictionary entry not found. Return to the Home Page </text> </center>
        <br>


        <center> <button onclick="window.location.replace('/')">Return to Home Page</button> </center>
    </body>

    </script>

</html>%
```
## Scenario 2
```
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=a&key=b&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=z&key=b&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=z&key=bb&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/count_element -d "namespace=a&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Namespace: a </text>
        <br>
        <br>

        <center> <text> Value: c </text>
        <br>
        <br>

        <center> <text> Count: 1 </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/count_element -d "namespace=z&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Namespace: z </text>
        <br>
        <br>

        <center> <text> Value: c </text>
        <br>
        <br>

        <center> <text> Count: 2 </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/count_global_element -d "value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Value: c </text>
        <br>
        <br>

        <center> <text> Count: 3 </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
```

## Scenario 3
```
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=a&key=b&value=c"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/set_element -d "namespace=a&key=b&value=d"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> The data has been updated! </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
(.venv) miabaker@Jonahs-MacBook-Pro flask-crud-app % curl -X POST http://127.0.0.1:5000/get_element -d "namespace=a&key=b"
<html>
    <head>
        <style>
            html {
                color: white;
                background-color: black;
            }

            text {
                font-size: 24px;
            }
        </style>
    </head>

    <body>
        <center> <h1> CRUD Application </h1></center>

        <center> <text> Namespace: a </text>
        <br>
        <br>

        <center> <text> Key: b </text>
        <br>
        <br>

        <center> <text> Value: d </text>
        <br>
        <br>

        <center> <button onclick="window.location.replace('/')">Home Page</button> </center>
    </body>
</html>%
```
