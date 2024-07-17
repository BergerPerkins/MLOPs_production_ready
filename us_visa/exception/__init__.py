import os  # Import the OS module for interacting with the operating system
import sys  # Import the sys module to access system-specific parameters and functions

def error_message_detail(error, error_detail: sys):
    # Function to generate a detailed error message
    _, _, exc_tb = error_detail.exc_info()  # Extract exception information
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the exception occurred
    error_message = "Error occured python script name [{0}] line number [{1}] erroe message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )  # Format the error message with the filename, line number, and error message
    return error_message  # Return the formatted error message



class USvisaException(Exception):
    # Custom exception class for handling specific errors
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)  # Initialize the base Exception class with the error message
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )  # Generate a detailed error message and store it in the instance variable

    def __str__(self):
        return self.error_message  # Return the detailed error message when the exception is converted to a string
