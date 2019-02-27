from . import test
from app import *
from flask import jsonify,request
import re

# Test API
@test.route('/tes', methods=['GET'])
def tes():
    return jsonify({"msg": "welcome to password validation"})



# API for validation of comma separated passwords
# API link for localhost postman testing
# localhost:5000/validate/validate_password?query=suman*12A,suman
@test.route('/validate_password' , methods=['GET'])
def validate_password():
    passwords = request.args['query']

    try:
        p = passwords.split(',')
        SpecialSymbol = ['*', '$','_','#','=','@']
        negateSymbol = ['%','!',')','(']
        filtered_result = []

        for pwd in p:
            fina = {}
            if not any(char in SpecialSymbol for char in pwd):
                fina[pwd] = " Faliure, Password must contain at least 1 of these special symbols [*$_#=@]"
            elif any(char in negateSymbol for char in pwd):
                fina[pwd] = "Faliure, Password cannot contain %!))"
            elif len(pwd) < 6:
                fina[pwd] = "Faliure, Password must be at least 6 character long"
            elif len(pwd) > 12:
                fina[pwd] = "Faliure, Password must be at 12 character long"
            elif re.search('[0-9]', pwd) is None:
                fina[pwd] = "Faliure, Password must contain at least 1 Digit from [0-9]"
            elif re.search('[a-z]', pwd) is None:
                fina[pwd] = "Faliure, Password must contain at least 1 letter from [a-z]"
            elif re.search('[A-Z]', pwd) is None:
                fina[pwd] = "Faliure, Password must contain at least 1 upper case letter from [A-Z]"
            else:
                fina[pwd] = "Success"

            filtered_result.append(fina)
        return jsonify({"result":filtered_result})
    except Exception as e:
        print str(e)
        return jsonify({"response":"failure","error": str(e)})