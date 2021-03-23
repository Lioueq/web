from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/carousel')
def carousel():
    return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                  <title>Пейзажи Марса</title>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                  <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                <div class="container">
                  <h1>Пейзажи Марса</h1>  
                  <div id="myCarousel" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                      <li data-target="#myCarousel" data-slide-to="1"></li>
                      <li data-target="#myCarousel" data-slide-to="2"></li>
                    </ol>
                    <div class="carousel-inner">
                      <div class="item active">
                        <img src="static/img/mars1.jpg" alt="1" style="width:1600px; height:600px;">
                      </div>
                      <div class="item">
                        <img src="static/img/mars2.jpg" alt="2" style="width:1600px; height:600px;">
                      </div>
                      <div class="item">
                        <img src="static/img/mars3.jpg" alt="3" style="width:1600px; height:600px;">
                      </div>
                    </div>
                    <!-- Left and right controls -->
                    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                      <span class="glyphicon glyphicon-chevron-left"></span>
                      <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#myCarousel" data-slide="next">
                      <span class="glyphicon glyphicon-chevron-right"></span>
                      <span class="sr-only">Next</span>
                    </a>
                  </div>
                </div>
                </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
