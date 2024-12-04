from flask import Flask, render_template, request

from utils import validate_fixed_matrix, convert_raw_matrix_to_real_matrix, matrices_calc


app = Flask(__name__)


@app.errorhandler(404)
def invalid_route(e):
    return "You have inserted an invalid path", 404


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
        # Convert the raw matrices to numpy objects and calc
        fixed_mat1, fixed_mat2 = convert_raw_matrix_to_real_matrix(mat1), convert_raw_matrix_to_real_matrix(mat2)
        result_matrix = matrices_calc(operation=operation, mat1=fixed_mat1, mat2=fixed_mat2)
        table = result_matrix.tolist()

    return render_template("calculation_result.html", error_message=error_message, table=table)


if __name__ == '__main__':
    app.run(debug=True)
