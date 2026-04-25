from src.custom_exception import CustomException

try:
    x=10/0

except Exception as e:
    raise CustomException(" 1 divide by zero not allowed",e)


    







