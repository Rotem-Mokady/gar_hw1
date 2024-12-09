from flask import Flask, render_template, request, url_for

from utils import validate_fixed_matrix, convert_raw_matrix_to_real_matrix, matrices_calc, convert_to_integer


app = Flask(__name__)


@app.errorhandler(404)
def invalid_route(e):
    return """
        <head>
            <title>Error</title>
        </head>
        <body>
            <h1>You have inserted an invalid path</h1>
            <a class="return-home" href="{home_page_url}">Return to home page</a>
        </body>
        """.format(home_page_url=url_for('home_page'))


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/calculate')
def calculate():
    operation, mat1, mat2 = request.args.get('operation'), request.args.get('mat1'), request.args.get('mat2')
    error_message, table = None, None

    # Handle inappropriate inputs

    if not operation or operation.lower() not in ['add', 'multiply']:
        error_message = "Unavailable operation entered"

    elif not (validate_fixed_matrix(mat1) and validate_fixed_matrix(mat2)):
        error_message = "Matrix should be passed as a list of number, and it's must be squared"

    elif len(mat1.split(',')) != len(mat2.split(',')):
        error_message = "The two matrices must be on the same size"

    if not error_message:
        # Convert the raw input matrices to numpy objects
        fixed_mat1, fixed_mat2 = convert_raw_matrix_to_real_matrix(mat1), convert_raw_matrix_to_real_matrix(mat2)
        # final matrix after calculation
        result_matrix = matrices_calc(operation=operation, mat1=fixed_mat1, mat2=fixed_mat2)
        # create table for final presentation in the HTML template
        table = [[convert_to_integer(element) for element in line] for line in result_matrix]

    return render_template("calculation_result.html", error_message=error_message, table=table)


if __name__ == '__main__':
    app.run(debug=True)
